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

# Curated direct high-res Wikimedia URLs for well-known MH leaders
KNOWN_MH_PORTRAITS = {
    "Devendra Fadnavis": "https://upload.wikimedia.org/wikipedia/commons/b/be/Shri_Devendra_Gangadharrao_Fadnavis.jpg",
    "Eknath Shinde": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Eknath_Shinde_%28cropped%29.jpg/500px-Eknath_Shinde_%28cropped%29.jpg",
    "Ajit Pawar": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Ajit_Pawar_2023.jpg/500px-Ajit_Pawar_2023.jpg",
    "Aslam Shaikh": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Aslam_Shaikh.jpg/500px-Aslam_Shaikh.jpg",
    "Hitendra Thakur": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Hitendra_Thakur.jpg/500px-Hitendra_Thakur.jpg",
    "Aditi Sunil Tatkare": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Aditi_Tatkare.jpg/500px-Aditi_Tatkare.jpg",
    "Deepak Vasant Kesarkar": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Deepak_Kesarkar.jpg/500px-Deepak_Kesarkar.jpg",
    "Girish Mahajan": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Girish_Mahajan.jpg/500px-Girish_Mahajan.jpg",
    "Gulabrao Patil": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Gulabrao_Patil.jpg/500px-Gulabrao_Patil.jpg",
    "Kunal Rohidas Patil": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Kunal_Patil.jpg/500px-Kunal_Patil.jpg",
    "Babanrao Lonikar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Babanrao_Lonikar.jpg/500px-Babanrao_Lonikar.jpg",
    "Vijaykumar Krishnarao Gavit": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Vijaykumar_Gavit.jpg/500px-Vijaykumar_Gavit.jpg",
    "Dhiraj Deshmukh": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Dhiraj_Deshmukh.jpg/500px-Dhiraj_Deshmukh.jpg",
    "Bhaskar Jadhav": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Bhaskar_Jadhav.jpg/500px-Bhaskar_Jadhav.jpg"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower().strip())

def download_image(url, dest_path):
    try:
        res = requests.get(url, headers=HEADERS, timeout=10)
        if res.status_code == 200 and len(res.content) > 1000:
            with open(dest_path, 'wb') as f:
                f.write(res.content)
            return True
    except Exception as e:
        print(f"    Download error: {e}")
    return False

def clean_politician_name(name):
    n = re.sub(r'^(adv\.?|dr\.?|prof\.?|ca\.?|col\.?|capt\.?|captain)\s+', '', name, flags=re.IGNORECASE).strip()
    n = re.sub(r'\s*\([^)]*\)', '', n).strip()
    return n

def query_wiki(name, state_name="Maharashtra"):
    clean = clean_politician_name(name)
    
    # 1. Check direct curated override
    if name in KNOWN_MH_PORTRAITS:
        return KNOWN_MH_PORTRAITS[name]
    if clean in KNOWN_MH_PORTRAITS:
        return KNOWN_MH_PORTRAITS[clean]
        
    # 2. Try opensearch / query API
    queries = [clean, f"{clean} (politician)", f"{clean} MLA"]
    for q in queries:
        try:
            url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(q)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            res = requests.get(url, headers=HEADERS, timeout=6).json()
            pages = res.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != "-1" and 'thumbnail' in pdata:
                    src = pdata['thumbnail']['source']
                    if src and not src.endswith('.svg'):
                        return src
        except Exception:
            pass
            
    # 3. Try MediaWiki search query
    try:
        s_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(clean + ' Maharashtra politician')}&format=json"
        res = requests.get(s_url, headers=HEADERS, timeout=6).json()
        hits = res.get('query', {}).get('search', [])
        for hit in hits[:2]:
            t_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(hit['title'])}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            t_res = requests.get(t_url, headers=HEADERS, timeout=6).json()
            for pid, pdata in t_res.get('query', {}).get('pages', {}).items():
                if pid != "-1" and 'thumbnail' in pdata:
                    src = pdata['thumbnail']['source']
                    if src and not src.endswith('.svg'):
                        return src
    except Exception:
        pass
        
    return None

def run_mh_enrichment():
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
                
    print(f"Total MH missing to process: {len(mh_missing)}")
    
    found_entries = []
    manual_required = []
    
    for idx, cand in enumerate(mh_missing):
        name = cand['elected_person']
        c_name = cand['constituency_name']
        code = cand['constituency_code']
        district = cand['district']
        party = cand['party']
        
        print(f"[{idx+1}/{len(mh_missing)}] Checking {name} ({c_name})...")
        img_url = query_wiki(name, "Maharashtra")
        
        if img_url:
            filename = f"mh_{sanitize_filename(name)}.jpg"
            dest = os.path.join(IMG_DIR, filename)
            if download_image(img_url, dest):
                cand['photo_source_url'] = f"/my-leader/assets/candidates/{filename}"
                print(f"  --> FOUND & SAVED: {filename}")
                found_entries.append(cand)
                continue
                
        print(f"  --> MANUAL INTERVENTION REQUIRED")
        manual_required.append(cand)
        time.sleep(0.2)
        
    # Save back to CSV
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        
    print("\n=======================================================")
    print(f"SUMMARY FOR MAHARASHTRA:")
    print(f"Total Missing Checked: {len(mh_missing)}")
    print(f"Successfully Recovered from Internet: {len(found_entries)}")
    print(f"Candidates Requiring Manual Photo Upload: {len(manual_required)}")
    print("=======================================================\n")
    
    # Write detailed manual intervention file
    report_file = os.path.join(BASE_DIR, "mh_photo_manual_intervention_list.md")
    lines = [
        "# Maharashtra Candidates Requiring Manual Photo Upload\n",
        f"The following **{len(manual_required)}** elected MLAs do not have public domain portraits on Wikipedia or official Commons archives.\n",
        "| No | Code | Constituency | District | Elected Representative | Party | Status |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |"
    ]
    for i, c in enumerate(manual_required, 1):
        lines.append(f"| {i} | {c['constituency_code']} | {c['constituency_name']} | {c['district']} | **{c['elected_person']}** | {c['party']} | `Needs Manual Photo` |")
        
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    print(f"Manual list generated at: {report_file}")

if __name__ == "__main__":
    run_mh_enrichment()
