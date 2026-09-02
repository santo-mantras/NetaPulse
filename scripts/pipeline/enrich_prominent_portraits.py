import csv
import json
import os
import requests
import re

CANDIDATE_IMG_DIR = "public/assets/candidates"
CSV_PATH = "scripts/pipeline/constituency_master.csv"

# Target key leaders mapped to their exact Wikipedia article titles
PROMINENT_WIKI_PAGES = {
    # Goa
    "Digambar Kamat": "Digambar_Kamat",
    "Michael Lobo": "Michael_Lobo_(politician)",
    "Vijai Sardesai": "Vijai_Sardesai",
    "Sudin Dhavalikar": "Sudin_Dhavalikar",
    
    # Chhattisgarh
    "Vishnu Deo Sai": "Vishnu_Deo_Sai",
    "Bhupesh Baghel": "Bhupesh_Baghel",
    "Raman Singh": "Raman_Singh",
    "Brijmohan Agrawal": "Brijmohan_Agrawal",
    
    # Tamil Nadu
    "Edappadi K. Palaniswami": "Edappadi_K._Palaniswami",
    "O. Panneerselvam": "O._Panneerselvam",
    "Durai Murugan": "Durai_Murugan",
    "V. Senthilbalaji": "V._Senthilbalaji",
    
    # Karnataka
    "Basavaraj Bommai": "Basavaraj_Bommai",
    "G. Parameshwara": "G._Parameshwara",
    "H. D. Revanna": "H._D._Revanna",
    
    # Uttar Pradesh
    "Keshav Prasad Maurya": "Keshav_Prasad_Maurya",
    "Suresh Khanna": "Suresh_Khanna"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower())

def download_and_enrich():
    os.makedirs(CANDIDATE_IMG_DIR, exist_ok=True)
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    headers = {'User-Agent': 'NetaPulseBot/2.0 (info@netapulse.org)'}
    downloaded = 0

    for r in rows:
        name = r['elected_person'].strip()
        matched_title = None
        for leader_name, wiki_title in PROMINENT_WIKI_PAGES.items():
            if leader_name.lower() in name.lower() or name.lower() in leader_name.lower():
                matched_title = wiki_title
                break

        if matched_title:
            try:
                # Fetch fresh working thumbnail from Wikipedia REST API
                api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{matched_title}"
                s_resp = requests.get(api_url, headers=headers, timeout=8)
                if s_resp.status_code == 200:
                    thumb_url = s_resp.json().get('thumbnail', {}).get('source')
                    if thumb_url:
                        fname = f"{sanitize_filename(name)}.jpg"
                        dest = os.path.join(CANDIDATE_IMG_DIR, fname)
                        img_resp = requests.get(thumb_url, headers=headers, timeout=10)
                        if img_resp.status_code == 200 and len(img_resp.content) > 1000:
                            with open(dest, "wb") as f_out:
                                f_out.write(img_resp.content)
                            r['photo_source_url'] = f"/assets/candidates/{fname}"
                            downloaded += 1
                            print(f"Downloaded portrait for {name} ({r['state']}) -> {fname}")
            except Exception as e:
                print(f"Error fetching {name}: {e}")

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSuccessfully enriched {downloaded} prominent leader portraits!")

if __name__ == "__main__":
    download_and_enrich()
