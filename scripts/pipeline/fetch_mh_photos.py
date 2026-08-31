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

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower().strip())

def download_image(url, dest_path):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return True
    try:
        res = requests.get(url, headers=HEADERS, timeout=6)
        if res.status_code == 200 and len(res.content) > 1000:
            with open(dest_path, 'wb') as f:
                f.write(res.content)
            return True
    except Exception:
        pass
    return False

def clean_politician_name(name):
    # Remove titles
    n = re.sub(r'^(adv\.?|dr\.?|prof\.?|ca\.?|col\.?|capt\.?|captain)\s+', '', name, flags=re.IGNORECASE).strip()
    # Remove parenthetical nicknames e.g. "Suresh Damu Bhole (Rajumama)" -> "Suresh Damu Bhole"
    n = re.sub(r'\s*\([^)]*\)', '', n).strip()
    return n

def search_wikipedia_photo(person_name, state_name=""):
    clean = clean_politician_name(person_name)
    
    queries = [
        clean,
        f"{clean} (politician)",
        f"{clean} ({state_name} politician)" if state_name else None,
        f"{clean} MLA",
        f"{clean} MP"
    ]
    
    for q in filter(None, queries):
        try:
            url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(q)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            r = requests.get(url, headers={'User-Agent': 'NetaPulseBot/1.0'}, timeout=4)
            if r.status_code == 200:
                pages = r.json().get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != "-1" and 'thumbnail' in pdata:
                        src = pdata['thumbnail']['source']
                        if src and ('svg' not in src.lower() or 'flag' not in src.lower()):
                            return src
        except Exception:
            pass
            
    # Also try wikipedia search API for top match
    try:
        search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(clean + ' ' + state_name + ' politician')}&format=json"
        sr = requests.get(search_url, headers={'User-Agent': 'NetaPulseBot/1.0'}, timeout=4)
        if sr.status_code == 200:
            hits = sr.json().get('query', {}).get('search', [])
            if hits:
                top_title = hits[0]['title']
                url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(top_title)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
                r2 = requests.get(url, headers={'User-Agent': 'NetaPulseBot/1.0'}, timeout=4)
                pages = r2.json().get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != "-1" and 'thumbnail' in pdata:
                        return pdata['thumbnail']['source']
    except Exception:
        pass
        
    return None

def fetch_mh_missing():
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    mh_missing = []
    for r in records:
        if r['state'] == 'Maharashtra':
            photo = r['photo_source_url']
            clean_path = photo.replace("/my-leader/", "").lstrip("/")
            local_file = os.path.join(PUBLIC_DIR, clean_path)
            if not photo or "placeholder-avatar" in photo or not os.path.exists(local_file) or os.path.getsize(local_file) < 1000:
                mh_missing.append(r)
                
    print(f"Total Maharashtra Missing Candidates to check: {len(mh_missing)}\n")
    
    found_count = 0
    not_found_list = []
    
    for idx, cand in enumerate(mh_missing):
        name = cand['elected_person']
        constituency = cand['constituency_name']
        code = cand['constituency_code']
        print(f"[{idx+1}/{len(mh_missing)}] Searching for: {name} ({constituency}, MH)...")
        
        photo_url = search_wikipedia_photo(name, "Maharashtra")
        if photo_url:
            filename = f"mh_{sanitize_filename(name)}.jpg"
            dest = os.path.join(IMG_DIR, filename)
            if download_image(photo_url, dest):
                cand['photo_source_url'] = f"/my-leader/assets/candidates/{filename}"
                print(f"  [FOUND] Downloaded: {photo_url}")
                found_count += 1
                continue
                
        print(f"  [NOT FOUND] Not found online (Wikipedia/Commons)")
        not_found_list.append(cand)
        time.sleep(0.3)
        
    # Update CSV with newly found
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        
    print("\n=======================================================")
    print(f"Maharashtra Photo Search Results:")
    print(f"Total Audited Missing: {len(mh_missing)}")
    print(f"Successfully Found & Downloaded: {found_count}")
    print(f"Needs Manual Intervention / Not Available: {len(not_found_list)}")
    print("=======================================================\n")
    
    return not_found_list

if __name__ == "__main__":
    fetch_mh_missing()
