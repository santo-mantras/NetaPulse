import csv
import json
import os
import requests
import re
import time

CANDIDATE_IMG_DIR = "public/assets/candidates"
CSV_PATH = "scripts/pipeline/constituency_master.csv"

# Target key leaders and ministers in Goa, Chhattisgarh, Tamil Nadu, Karnataka, and UP
TARGET_LEADERS = {
    # Goa
    "Digambar Kamat": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Digambar_Kamat_%28cropped%29.jpg/500px-Digambar_Kamat_%28cropped%29.jpg",
    "Michael Lobo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Michael_Lobo.jpg/500px-Michael_Lobo.jpg",
    "Vijai Sardesai": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Vijai_Sardesai_%28cropped%29.jpg/500px-Vijai_Sardesai_%28cropped%29.jpg",
    "Vishwajit Pratapsingh Rane": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Vishwajit_Rane_%28cropped%29.jpg/500px-Vishwajit_Rane_%28cropped%29.jpg",
    "Atanasio Monserrate": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Atanasio_Babush_Monserrate.jpg/500px-Atanasio_Babush_Monserrate.jpg",
    "Sudin Dhavalikar": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Sudin_Dhavalikar_%28cropped%29.jpg/500px-Sudin_Dhavalikar_%28cropped%29.jpg",
    
    # Chhattisgarh
    "Vishnu Deo Sai": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Vishnu_Deo_Sai_in_2023.jpg/500px-Vishnu_Deo_Sai_in_2023.jpg",
    "Bhupesh Baghel": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bhupesh_Baghel_%28cropped%29.jpg/500px-Bhupesh_Baghel_%28cropped%29.jpg",
    "T. S. Singh Deo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/T._S._Singh_Deo.jpg/500px-T._S._Singh_Deo.jpg",
    "Brijmohan Agrawal": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Brijmohan_Agrawal.jpg/500px-Brijmohan_Agrawal.jpg",
    "Raman Singh": "https://upload.wikimedia.org/wikipedia/commons/9/98/Raman_Singh_2016.jpg",
    
    # Tamil Nadu
    "Edappadi K. Palaniswami": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Edappadi_K._Palaniswami_%28cropped%29.jpg/500px-Edappadi_K._Palaniswami_%28cropped%29.jpg",
    "O. Panneerselvam": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/O_Panneerselvam_in_2021.jpg/500px-O_Panneerselvam_in_2021.jpg",
    "V. Senthilbalaji": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/V._Senthil_Balaji.jpg/500px-V._Senthil_Balaji.jpg",
    "K. N. Nehru": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/K._N._Nehru_%28cropped%29.jpg/500px-K._N._Nehru_%28cropped%29.jpg",
    "Thangam Thennarasu": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Thangam_Thenarasu.jpg/500px-Thangam_Thenarasu.jpg",
    "P. T. R. Palanivel Thiagarajan": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/P.T.R.Palanivel_Thiagarajan.jpg/500px-P.T.R.Palanivel_Thiagarajan.jpg",
    
    # Karnataka & UP
    "Basavaraj Bommai": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Basavaraj_Bommai_2021_%28cropped%29.jpg/500px-Basavaraj_Bommai_2021_%28cropped%29.jpg",
    "G. Parameshwara": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/G_Parameshwara.jpg/500px-G_Parameshwara.jpg",
    "H. D. Revanna": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/H_D_Revanna.jpg/500px-H_D_Revanna.jpg",
    "B. Y. Vijayendra": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/B_Y_Vijayendra.jpg/500px-B_Y_Vijayendra.jpg",
    "Keshav Prasad Maurya": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Keshav_Prasad_Maurya_%28cropped%29.jpg/500px-Keshav_Prasad_Maurya_%28cropped%29.jpg",
    "Suresh Khanna": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Suresh_Kumar_Khanna.jpg/500px-Suresh_Kumar_Khanna.jpg"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower())

def enrich_state_portraits():
    os.makedirs(CANDIDATE_IMG_DIR, exist_ok=True)
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    downloaded = 0

    for r in rows:
        name = r['elected_person'].strip()
        matched_url = None
        for target_name, url in TARGET_LEADERS.items():
            if target_name.lower() in name.lower() or name.lower() in target_name.lower():
                matched_url = url
                break

        if matched_url:
            fname = f"{sanitize_filename(name)}.jpg"
            dest = os.path.join(CANDIDATE_IMG_DIR, fname)
            try:
                res = requests.get(matched_url, headers=headers, timeout=12)
                if res.status_code == 200 and len(res.content) > 1000:
                    with open(dest, "wb") as img_file:
                        img_file.write(res.content)
                    r['photo_source_url'] = f"/assets/candidates/{fname}"
                    downloaded += 1
                    print(f"Downloaded portrait: {name} -> {fname}")
            except Exception as e:
                print(f"Failed {name}: {e}")

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nEnriched {downloaded} key minister portraits across expanded states!")

if __name__ == "__main__":
    enrich_state_portraits()
