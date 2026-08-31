import os
import csv
import json
import requests
import urllib.parse
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CSV_PATH = os.path.join(BASE_DIR, "scripts/pipeline/constituency_master.csv")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
IMG_DIR = os.path.join(PUBLIC_DIR, "assets/candidates")
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Verified high-res direct Wikimedia Commons URLs
VERIFIED_MH_LEADERS = {
    "Devendra Fadnavis": "https://upload.wikimedia.org/wikipedia/commons/b/be/Shri_Devendra_Gangadharrao_Fadnavis.jpg",
    "Eknath Shinde": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Eknath_Shinde_SS.jpg/500px-Eknath_Shinde_SS.jpg",
    "Ajit Pawar": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Shri_Ajit_Anantrao_Pawar.jpg",
    "Girish Mahajan": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Girish_Mahajan_in_2023.jpg/500px-Girish_Mahajan_in_2023.jpg",
    "Gulabrao Patil": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Gulabrao_Patil_2023.jpg/500px-Gulabrao_Patil_2023.jpg",
    "Prashant Thakur": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Prashant_Thakur_MLA.jpg/500px-Prashant_Thakur_MLA.jpg"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower().strip())

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

def sync_mh_photos():
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    for r in records:
        if r['state'] == 'Maharashtra':
            name = r['elected_person']
            for v_name, v_url in VERIFIED_MH_LEADERS.items():
                if v_name.lower() in name.lower() or name.lower() in v_name.lower():
                    fname = f"mh_{sanitize_filename(v_name)}.jpg"
                    dest = os.path.join(IMG_DIR, fname)
                    if download_image(v_url, dest):
                        r['photo_source_url'] = f"/my-leader/assets/candidates/{fname}"
                        print(f"Successfully linked verified portrait for: {name} -> {fname}")
                        
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)

if __name__ == "__main__":
    sync_mh_photos()
