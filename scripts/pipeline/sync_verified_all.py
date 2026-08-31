import os
import csv
import json
import requests
import urllib.parse
import re
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CSV_PATH = os.path.join(BASE_DIR, "scripts/pipeline/constituency_master.csv")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
IMG_DIR = os.path.join(PUBLIC_DIR, "assets/candidates")
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Accurate direct Wikipedia live thumbnail mappings
DIRECT_HIGH_PROFILE = {
    "Brajesh Pathak": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Brajesh_Pathak.jpg/500px-Brajesh_Pathak.jpg",
    "Bhagwant Mann": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Bhagwant_Mann_2026.jpg/500px-Bhagwant_Mann_2026.jpg",
    "Navjot Singh Sidhu": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Punjab_Minister_of_Tourism_%26_Culture_Navjot_Singh_Sidhu.jpg/500px-Punjab_Minister_of_Tourism_%26_Culture_Navjot_Singh_Sidhu.jpg",
    "Sukhbir Singh Badal": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Sukhbir_Singh_Badal_%28cropped%29.jpg",
    "Basavaraj Bommai": "https://upload.wikimedia.org/wikipedia/commons/2/23/Bommai_at_the_inauguration_of_Metroline_%28cropped%29.jpg",
    "H. D. Kumaraswamy": "https://upload.wikimedia.org/wikipedia/commons/5/5b/JDS_chief_Kumaraswamy.jpg",
    "Keshav Prasad Maurya": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Shri_Keshav_Prasad_Maurya%2C_MP%2C_Phoolpur_%28U.P%29_and_Shri_Satyapal_Singh_Saini%2C_MP%2C_Sambhal_%28U.P%29_meeting_the_Minister_of_State_for_Culture_%28Independent_Charge%29%2C_Tourism_%28Independent_Charge%29_and_Civil_Aviation_%28cropped%29.jpg/500px-thumbnail.jpg",
    "Yogi Adityanath": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Yogiji_in_2023.jpg/500px-Yogiji_in_2023.jpg",
    "Ravi Kishan": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Ravi_Kissen_at_the_launch_of_T_P_Aggarwal%27s_trade_magazine_%27Blockbuster%27_20.jpg/500px-Ravi_Kissen_at_the_launch_of_T_P_Aggarwal%27s_trade_magazine_%27Blockbuster%27_20.jpg",
    "Pankaj Singh": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Pankaj_Singh_-_politician.jpg",
    "Akhilesh Yadav": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Akhilesh_Yadav_544.jpg/500px-Akhilesh_Yadav_544.jpg",
    "Devendra Fadnavis": "https://upload.wikimedia.org/wikipedia/commons/b/be/Shri_Devendra_Gangadharrao_Fadnavis.jpg",
    "Eknath Shinde": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Eknath_Shinde_SS.jpg/500px-Eknath_Shinde_SS.jpg",
    "Ajit Pawar": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Shri_Ajit_Anantrao_Pawar.jpg",
    "Siddaramaiah": "https://upload.wikimedia.org/wikipedia/commons/0/06/Siddaramaiah_at_the_function_Akshaya_Patra_Foundation_in_Karnataka.jpg",
    "D.K. Shivakumar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Dkshivakumar.png/500px-Dkshivakumar.png",
    "D. K. Shivakumar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Dkshivakumar.png/500px-Dkshivakumar.png"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower().strip())

def clean_politician_name(name):
    n = re.sub(r'^(adv\.?|dr\.?|prof\.?|ca\.?|col\.?|capt\.?|captain)\s+', '', name, flags=re.IGNORECASE).strip()
    n = re.sub(r'\s*\([^)]*\)', '', n).strip()
    return n

def download_image(url, dest_path):
    try:
        res = requests.get(url, headers=HEADERS, timeout=8)
        if res.status_code == 200 and len(res.content) > 1000:
            with open(dest_path, 'wb') as f:
                f.write(res.content)
            return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
    return False

def live_fetch_wiki_photo(name):
    clean = clean_politician_name(name)
    
    # 1. Direct dict
    for k, v in DIRECT_HIGH_PROFILE.items():
        if k.lower() == clean.lower() or k.lower() == name.lower():
            return v
            
    # 2. Live API
    for q in [clean, f"{clean} (politician)"]:
        try:
            url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(q)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            res = requests.get(url, headers=HEADERS, timeout=5).json()
            for pid, pdata in res.get('query', {}).get('pages', {}).items():
                if pid != "-1" and 'thumbnail' in pdata:
                    src = pdata['thumbnail']['source']
                    if src and not src.endswith('.svg'):
                        return src
        except Exception:
            pass
    return None

def sync_and_regenerate():
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    print(f"Auditing all {len(records)} candidate photo URLs...")
    
    updated_count = 0
    for r in records:
        name = r['elected_person']
        st = r['state']
        curr_photo = r['photo_source_url']
        
        # Check if we have a direct high profile or live wiki photo
        wiki_url = live_fetch_wiki_photo(name)
        if wiki_url:
            fname = f"{sanitize_filename(st[:2])}_{sanitize_filename(name)}.jpg"
            dest = os.path.join(IMG_DIR, fname)
            if download_image(wiki_url, dest):
                new_local_url = f"/my-leader/assets/candidates/{fname}"
                if r['photo_source_url'] != new_local_url:
                    r['photo_source_url'] = new_local_url
                    print(f"  [LINKED] {name} ({st}) -> {new_local_url}")
                    updated_count += 1
                    
    # Save CSV
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        
    print(f"\nUpdated {updated_count} candidates in Master CSV.\n")
    
    # Regenerate unified manual photo intervention markdown
    report_file = os.path.join(BASE_DIR, "all_states_manual_photo_intervention.md")
    lines = [
        "# Candidate Photos Requiring Manual Upload (All States)\n",
        "This document lists all elected representatives across Maharashtra, Uttar Pradesh, Karnataka, and Punjab who do not have public domain portraits on online encyclopedias and require manual photo drops.\n",
        "---\n"
    ]
    
    total_needing = 0
    for st in ["Maharashtra", "Uttar Pradesh", "Karnataka", "Punjab"]:
        st_manual = []
        for r in records:
            if r['state'] == st:
                photo = r['photo_source_url']
                clean_path = photo.replace("/my-leader/", "").lstrip("/")
                local_file = os.path.join(PUBLIC_DIR, clean_path)
                if not photo or "placeholder-avatar" in photo or not os.path.exists(local_file) or os.path.getsize(local_file) < 1000:
                    st_manual.append(r)
                    
        total_needing += len(st_manual)
        lines.append(f"## {st} ({len(st_manual)} Candidates Needing Photos)\n")
        lines.append("| No | Code | Constituency | District | Elected Representative | Party | Status |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        for i, c in enumerate(st_manual, 1):
            lines.append(f"| {i} | {c['constituency_code']} | {c['constituency_name']} | {c['district']} | **{c['elected_person']}** | {c['party']} | `Needs Manual Photo` |")
        lines.append("\n---\n")
        
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    print(f"Regenerated accurate checklist: {report_file} (Total: {total_needing} needing photos)")

if __name__ == "__main__":
    sync_and_regenerate()
