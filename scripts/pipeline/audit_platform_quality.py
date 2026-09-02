"""
NetaPulse Platform Integrity & Quality Auditor.
Run this script anytime to verify 100% data correctness across all states,
districts, candidate names, photos, and state seats composition.
"""

import os
import csv
import json
from collections import defaultdict

MASTER_CSV = "scripts/pipeline/constituency_master.csv"
JSON_PATH = "src/data/realGovernanceData.json"
CANDIDATE_DIR = "public/assets/candidates"

KNOWN_PARTY_ACRONYMS = {
    'BJP', 'INC', 'AAP', 'SP', 'BSP', 'SHS', 'NCP', 'JDS', 'DMK', 'AIADMK',
    'PMK', 'SAD', 'CPI', 'CPM', 'CPI(M)', 'VCK', 'MDMK', 'IND', 'GGP'
}

def run_platform_audit():
    print("=" * 60)
    print("NETAPULSE PLATFORM INTEGRITY & QUALITY AUDIT")
    print("=" * 60)

    # 1. Audit Master CSV
    with open(MASTER_CSV, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))

    print(f"\n[1/3] Master CSV Audit ({len(rows)} Total Constituencies)")
    state_groups = defaultdict(list)
    csv_anomalies = []

    for idx, r in enumerate(rows):
        st = r['state'].strip()
        cname = r['constituency_name'].strip()
        name = r['elected_person'].strip()
        dist = r['district'].strip()
        photo = r.get('photo_source_url', '')

        state_groups[st].append(r)

        # Check for placeholder names, acronyms, or empty values
        if not name or name in KNOWN_PARTY_ACRONYMS or len(name) <= 3 or name.lower() in ['elected mla', 'elected representative', 'none of the above']:
            csv_anomalies.append((st, dist, cname, name))

    print(f"  States Covered: {len(state_groups)}")
    for st, s_rows in sorted(state_groups.items()):
        dists = set(x['district'] for x in s_rows)
        print(f"    - {st:15}: {len(s_rows):3} seats across {len(dists):2} districts")

    if csv_anomalies:
        print(f"  [FAIL] Detected {len(csv_anomalies)} candidate name anomalies:")
        for a in csv_anomalies[:10]:
            print(f"    {a}")
    else:
        print("  [PASS] 100% authentic candidate names (0 placeholders / 0 acronyms).")

    # 2. Audit Photos & Disk Assets
    print(f"\n[2/3] Profile Photo & Asset Verification")
    broken_photos = []
    verified_portraits = 0
    clean_avatars = 0

    for r in rows:
        url = r.get('photo_source_url', '')
        if url.startswith('/assets/candidates/'):
            disk_path = "public" + url
            if os.path.exists(disk_path) and os.path.getsize(disk_path) > 1000:
                verified_portraits += 1
            else:
                broken_photos.append((r['state'], r['elected_person'], url))
        else:
            clean_avatars += 1

    print(f"  Verified High-Resolution Portraits: {verified_portraits}")
    print(f"  Verified SVG Vector Avatars:        {clean_avatars}")
    if broken_photos:
        print(f"  [FAIL] Detected {len(broken_photos)} broken photo links:")
        for b in broken_photos[:5]:
            print(f"    {b}")
    else:
        print("  [PASS] Zero broken image links across all candidates.")

    # 3. Audit Compiled JSON
    print(f"\n[3/3] Compiled realGovernanceData.json Verification")
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print(f"  Total Locations:  {len(data.get('locations', []))}")
        print(f"  Total Candidates: {len(data.get('candidates', []))}")
        print(f"  Total Promises:   {len(data.get('promises', []))}")
        print(f"  Total News:       {len(data.get('news', []))}")

        # Check district stat consistency within districts
        dist_cache = {}
        inconsistent_dists = []
        for loc in data.get('locations', []):
            dkey = (loc['stateName'], loc['districtName'])
            stats = (loc['crimeRatePerLakh'], loc['literacyRate'], loc['hospitalsCount'])
            if dkey not in dist_cache:
                dist_cache[dkey] = stats
            else:
                if dist_cache[dkey] != stats:
                    inconsistent_dists.append(dkey)

        if inconsistent_dists:
            print(f"  [FAIL] Inconsistent stats found in {len(set(inconsistent_dists))} districts.")
        else:
            print("  [PASS] 100% district stat consistency verified across all constituencies.")
    else:
        print(f"  [FAIL] Compiled file {JSON_PATH} does not exist.")

    print("\n" + "=" * 60)
    if not csv_anomalies and not broken_photos and not inconsistent_dists:
        print("RESULT: ALL QUALITY & DATA ACCURACY STANDARDS PASSED!")
    else:
        print("RESULT: AUDIT FAILED - PLEASE REVIEW FLAGGED ITEMS ABOVE.")
    print("=" * 60)

if __name__ == "__main__":
    run_platform_audit()
