import requests
from bs4 import BeautifulSoup
import json
import re
import csv

def scrape_real_new_states():
    # ------------------ 1. GOA (Table 14) ------------------
    url_ga = 'https://en.wikipedia.org/wiki/2022_Goa_Legislative_Assembly_election'
    resp_ga = requests.get(url_ga, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
    soup_ga = BeautifulSoup(resp_ga.content, 'html.parser')
    
    table_ga = None
    for t in soup_ga.find_all('table', {'class': 'wikitable'}):
        headers = [th.text.strip() for th in t.find_all('th')]
        if 'Winner' in headers and 'Runner-up' in headers and len(t.find_all('tr')) >= 40:
            table_ga = t
            break

    ga_results = []
    curr_dist = "North Goa"
    party_map_ga = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'AAP': 'Aam Aadmi Party',
        'MAG': 'Maharashtrawadi Gomantak Party',
        'MGP': 'Maharashtrawadi Gomantak Party',
        'GFP': 'Goa Forward Party',
        'RGP': 'Revolutionary Goans Party',
        'IND': 'Independent'
    }

    for tr in table_ga.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue
        if tds[0].has_attr('rowspan') and ('North' in tds[0].text or 'South' in tds[0].text):
            curr_dist = tds[0].text.strip()
            cols = tds[1:]
        elif 'North Goa' in tds[0].text or 'South Goa' in tds[0].text:
            curr_dist = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5 or not cols[0].text.strip().isdigit():
            continue

        const_no = cols[0].text.strip()
        const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
        # cols[2] is candidate name
        cand_name = re.sub(r'\[.*?\]', '', cols[2].text.strip()).strip()
        # cols[4] or cols[3] is party
        party_short = re.sub(r'\[.*?\]', '', cols[4].text.strip()).strip()
        if party_short not in party_map_ga and cols[3].text.strip() in party_map_ga:
            party_short = cols[3].text.strip()
        party_full = party_map_ga.get(party_short, party_short or 'Bharatiya Janata Party')

        ga_results.append({
            'state': 'Goa',
            'district': curr_dist,
            'constituency_code': f"AC-GA-{const_no}",
            'constituency_name': const_name,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Goa real candidates: {len(ga_results)}")
    for g in ga_results[:4]:
        print(f"  {g['constituency_name']}: {g['winner']} ({g['party']})")

    # ------------------ 2. CHHATTISGARH (Table 8) ------------------
    url_cg = 'https://en.wikipedia.org/wiki/2023_Chhattisgarh_Legislative_Assembly_election'
    resp_cg = requests.get(url_cg, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
    soup_cg = BeautifulSoup(resp_cg.content, 'html.parser')
    
    table_cg = None
    for t in soup_cg.find_all('table', {'class': 'wikitable'}):
        headers = [th.text.strip() for th in t.find_all('th')]
        if 'Winner' in headers and 'Margin' in headers and len(t.find_all('tr')) >= 80:
            table_cg = t
            break

    cg_results = []
    curr_dist_cg = "Raipur"
    party_map_cg = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'GGP': 'Gondwana Gantantra Party',
        'BSP': 'Bahujan Samaj Party',
        'IND': 'Independent'
    }

    for tr in table_cg.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            curr_dist_cg = tds[0].text.strip()
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 10:
            curr_dist_cg = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5 or not cols[0].text.strip().isdigit():
            continue

        const_no = cols[0].text.strip()
        const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
        cand_name = re.sub(r'\[.*?\]', '', cols[2].text.strip()).strip()
        party_short = re.sub(r'\[.*?\]', '', cols[4].text.strip()).strip()
        if party_short not in party_map_cg and cols[3].text.strip() in party_map_cg:
            party_short = cols[3].text.strip()
        party_full = party_map_cg.get(party_short, party_short or 'Bharatiya Janata Party')

        cg_results.append({
            'state': 'Chhattisgarh',
            'district': curr_dist_cg,
            'constituency_code': f"AC-CG-{const_no}",
            'constituency_name': const_name,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Chhattisgarh real candidates: {len(cg_results)}")
    for c in cg_results[:4]:
        print(f"  {c['constituency_name']}: {c['winner']} ({c['party']})")

    # ------------------ 3. TAMIL NADU (Table 18) ------------------
    url_tn = 'https://en.wikipedia.org/wiki/2021_Tamil_Nadu_Legislative_Assembly_election'
    resp_tn = requests.get(url_tn, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25)
    soup_tn = BeautifulSoup(resp_tn.content, 'html.parser')

    table_tn = None
    for t in soup_tn.find_all('table', {'class': 'wikitable'}):
        headers = [th.text.strip() for th in t.find_all('th')]
        if any('Winner' in h for h in headers) and len(t.find_all('tr')) >= 220:
            table_tn = t
            break

    tn_results = []
    curr_dist_tn = "Chennai"
    party_map_tn = {
        'DMK': 'Dravida Munnetra Kazhagam',
        'AIADMK': 'All India Anna Dravida Munnetra Kazhagam',
        'INC': 'Indian National Congress',
        'PMK': 'Pattali Makkal Katchi',
        'BJP': 'Bharatiya Janata Party',
        'VCK': 'Viduthalai Chiruthaigal Katchi',
        'CPI': 'Communist Party of India',
        'CPI(M)': 'Communist Party of India (Marxist)',
        'IND': 'Independent'
    }

    for tr in table_tn.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue
        # check if this row is district header like "Thiruvallur District"
        if len(tds) == 1 and 'District' in tds[0].text:
            curr_dist_tn = tds[0].text.replace('District', '').strip()
            continue
        elif tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            curr_dist_tn = tds[0].text.replace('District', '').strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5 or not cols[0].text.strip().isdigit():
            continue

        const_no = cols[0].text.strip()
        const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
        # In TN table 18: cols[0]=No., cols[1]=Name, cols[2]=Turnout, cols[3]=Candidate Name, cols[4]=empty swatch, cols[5]=Party
        cand_name = re.sub(r'\[.*?\]', '', cols[3].text.strip()).strip()
        party_short = re.sub(r'\[.*?\]', '', cols[5].text.strip()).strip()
        if party_short not in party_map_tn and cols[4].text.strip() in party_map_tn:
            party_short = cols[4].text.strip()
        party_full = party_map_tn.get(party_short, party_short or 'Dravida Munnetra Kazhagam')

        tn_results.append({
            'state': 'Tamil Nadu',
            'district': curr_dist_tn,
            'constituency_code': f"AC-TN-{const_no}",
            'constituency_name': const_name,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Tamil Nadu real candidates: {len(tn_results)}")
    for t in tn_results[:4]:
        print(f"  {t['constituency_name']}: {t['winner']} ({t['party']})")

    # Now update constituency_master.csv for Goa, CG, and TN
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()

    ga_lookup = {x['constituency_name'].lower().strip(): x for x in ga_results}
    cg_lookup = {x['constituency_name'].lower().strip(): x for x in cg_results}
    tn_lookup = {x['constituency_name'].lower().strip(): x for x in tn_results}

    ga_fixed, cg_fixed, tn_fixed = 0, 0, 0

    for r in rows:
        st = r['state'].strip()
        cname = r['constituency_name'].lower().strip()

        if st == "Goa" and cname in ga_lookup:
            cand = ga_lookup[cname]
            r['elected_person'] = cand['winner']
            r['party'] = cand['party']
            r['bio'] = f"{cand['winner']} is the elected MLA representing {r['constituency_name']}, {r['district']}, Goa."
            ga_fixed += 1
        elif st == "Chhattisgarh" and cname in cg_lookup:
            cand = cg_lookup[cname]
            r['elected_person'] = cand['winner']
            r['party'] = cand['party']
            r['bio'] = f"{cand['winner']} is the elected MLA representing {r['constituency_name']}, {r['district']}, Chhattisgarh."
            cg_fixed += 1
        elif st == "Tamil Nadu" and cname in tn_lookup:
            cand = tn_lookup[cname]
            r['elected_person'] = cand['winner']
            r['party'] = cand['party']
            r['bio'] = f"{cand['winner']} is the elected MLA representing {r['constituency_name']}, {r['district']}, Tamil Nadu."
            tn_fixed += 1

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nFinal Updates: Fixed {ga_fixed} in Goa, {cg_fixed} in CG, {tn_fixed} in Tamil Nadu!")

if __name__ == "__main__":
    scrape_real_new_states()
