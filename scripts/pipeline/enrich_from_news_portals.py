import os
import csv
import json
import requests
import urllib.parse
import re
import time
from bs4 import BeautifulSoup

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

def clean_politician_name(name):
    n = re.sub(r'^(adv\.?|dr\.?|prof\.?|ca\.?|col\.?|capt\.?|captain)\s+', '', name, flags=re.IGNORECASE).strip()
    n = re.sub(r'\s*\([^)]*\)', '', n).strip()
    return n

def download_image(url, dest_path):
    try:
        if not url.startswith('http'):
            url = 'https://' + url.lstrip('/')
        res = requests.get(url, headers=HEADERS, timeout=8)
        if res.status_code == 200 and len(res.content) > 2000:
            with open(dest_path, 'wb') as f:
                f.write(res.content)
            return True
    except Exception:
        pass
    return False

def search_news_and_portals(name, state_name, constituency_name):
    clean = clean_politician_name(name)
    slug = re.sub(r'[^a-z0-9]+', '-', clean.lower()).strip('-')
    
    # 1. Try Rajkaran.in politician page direct probe
    try:
        raj_url = f"https://rajkaran.in/{slug}"
        r = requests.get(raj_url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            for img in soup.find_all('img'):
                src = img.get('src', '')
                if '/uploads/' in src and (slug in src.lower() or any(p in src.lower() for p in slug.split('-'))):
                    if src.startswith('/'):
                        src = "https://rajkaran.in" + src
                    return src
    except Exception:
        pass

    # 2. Try DuckDuckGo targeted news and profile portal search
    search_queries = [
        f"{clean} {constituency_name} MLA {state_name} profile",
        f"{clean} MLA Maharashtra Indian Express",
        f"{clean} MLA Lokmat Marathi"
    ]
    
    for q in search_queries:
        try:
            ddg_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(q)}"
            r = requests.get(ddg_url, headers=HEADERS, timeout=5)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                links = []
                for a in soup.find_all('a', class_='result__url'):
                    href = a.get('href', '')
                    if 'uddg=' in href:
                        actual = urllib.parse.unquote(href.split('uddg=')[1].split('&')[0])
                        links.append(actual)
                    elif href.startswith('http'):
                        links.append(href)
                        
                for l in links[:3]:
                    # Probe portal page for lead news/profile image
                    if any(domain in l for domain in ['rajkaran.in', 'indianexpress.com', 'loksatta.com', 'esakal.com', 'abplive.com', 'ndtv.com']):
                        try:
                            pr = requests.get(l, headers=HEADERS, timeout=5)
                            if pr.status_code == 200:
                                psoup = BeautifulSoup(pr.text, 'html.parser')
                                for meta in psoup.find_all('meta', property=['og:image', 'twitter:image']):
                                    msrc = meta.get('content', '')
                                    if msrc and ('logo' not in msrc.lower() and 'default' not in msrc.lower() and 'placeholder' not in msrc.lower()):
                                        return msrc
                        except Exception:
                            pass
        except Exception:
            pass
        time.sleep(0.2)
        
    return None

def run_news_portal_enrichment():
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
                
    print(f"Auditing {len(mh_missing)} missing Maharashtra MLAs across Popular News & Regional Portals...")
    
    found_count = 0
    still_missing = []
    
    for idx, cand in enumerate(mh_missing):
        name = cand['elected_person']
        c_name = cand['constituency_name']
        state = cand['state']
        
        print(f"[{idx+1}/{len(mh_missing)}] News search for: {name} ({c_name})...")
        photo_url = search_news_and_portals(name, state, c_name)
        
        if photo_url:
            filename = f"mh_{sanitize_filename(name)}.jpg"
            dest = os.path.join(IMG_DIR, filename)
            if download_image(photo_url, dest):
                cand['photo_source_url'] = f"/my-leader/assets/candidates/{filename}"
                print(f"  [RECOVERED] Downloaded from news/portal: {photo_url[:80]}...")
                found_count += 1
                continue
                
        print(f"  [UNAVAILABLE] No photo found on news media.")
        still_missing.append(cand)
        time.sleep(0.3)
        
    # Save back to CSV
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        
    print("\n=======================================================")
    print(f"NEWS & MEDIA PORTAL AUDIT RESULTS (MH):")
    print(f"Candidates Checked: {len(mh_missing)}")
    print(f"Photos Recovered from News/Portals: {found_count}")
    print(f"Remaining Missing: {len(still_missing)}")
    print("=======================================================\n")

if __name__ == "__main__":
    run_news_portal_enrichment()
