import os
import csv
import json
import requests
import re
import urllib.parse
import time

CANDIDATE_IMG_DIR = "public/assets/candidates"
CSV_PATH = "scripts/pipeline/constituency_master.csv"

# Curated High-Definition Official / Wikipedia Portraits for Chief Ministers & Key Leaders in expanded states
PROMINENT_PORTRAITS = {
    # Goa Leaders
    "Pramod Sawant": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Pramod_Sawant_at_the_inauguration_of_the_Chhatrapati_Shivaji_Maharaj_Chair_in_Goa_University_%28cropped%29.jpg/500px-Pramod_Sawant_at_the_inauguration_of_the_Chhatrapati_Shivaji_Maharaj_Chair_in_Goa_University_%28cropped%29.jpg",
    "Digambar Kamat": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Digambar_Kamat_%28cropped%29.jpg/500px-Digambar_Kamat_%28cropped%29.jpg",
    "Michael Lobo": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Michael_Lobo.jpg/500px-Michael_Lobo.jpg",
    "Vijai Sardesai": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Vijai_Sardesai_%28cropped%29.jpg/500px-Vijai_Sardesai_%28cropped%29.jpg",
    
    # Chhattisgarh Leaders
    "Vishnu Deo Sai": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Vishnu_Deo_Sai_in_2023.jpg/500px-Vishnu_Deo_Sai_in_2023.jpg",
    "Raman Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Raman_Singh_2016.jpg/500px-Raman_Singh_2016.jpg",
    "Bhupesh Baghel": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Bhupesh_Baghel_%28cropped%29.jpg/500px-Bhupesh_Baghel_%28cropped%29.jpg",
    "T. S. Singh Deo": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/T._S._Singh_Deo.jpg/500px-T._S._Singh_Deo.jpg",
    "Brijmohan Agrawal": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Brijmohan_Agrawal.jpg/500px-Brijmohan_Agrawal.jpg",
    "Renuka Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Renuka_Singh_Saruta_PIB_%28cropped%29.jpg/500px-Renuka_Singh_Saruta_PIB_%28cropped%29.jpg",

    # Tamil Nadu Leaders
    "M. K. Stalin": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/The_Chief_Minister_of_Tamil_Nadu%2C_Thiru_MK_Stalin.jpg/500px-The_Chief_Minister_of_Tamil_Nadu%2C_Thiru_MK_Stalin.jpg",
    "Edappadi K. Palaniswami": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Edappadi_K._Palaniswami_%28cropped%29.jpg/500px-Edappadi_K._Palaniswami_%28cropped%29.jpg",
    "O. Panneerselvam": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/O_Panneerselvam_in_2021.jpg/500px-O_Panneerselvam_in_2021.jpg",
    "Udhayanidhi Stalin": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Udhaya.jpg/500px-Udhaya.jpg",
    "Durai Murugan": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Duraimurugan.jpg/500px-Duraimurugan.jpg",

    # Karnataka & UP Leaders
    "Basavaraj Bommai": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Basavaraj_Bommai_2021_%28cropped%29.jpg/500px-Basavaraj_Bommai_2021_%28cropped%29.jpg",
    "Laxman Savadi": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Pranay_Vivek_Patil_1_%28cropped%29.jpg/500px-Pranay_Vivek_Patil_1_%28cropped%29.jpg",
    "G. Parameshwara": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/G_Parameshwara.jpg/500px-G_Parameshwara.jpg",
    "H. D. Revanna": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/H_D_Revanna.jpg/500px-H_D_Revanna.jpg",
    "Keshav Prasad Maurya": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Keshav_Prasad_Maurya_%28cropped%29.jpg/500px-Keshav_Prasad_Maurya_%28cropped%29.jpg"
}

def sanitize_name(name):
    return re.sub(r'[^a-zA-Z0-9]+', '_', name).strip('_').lower()

def download_and_assign_photos():
    os.makedirs(CANDIDATE_IMG_DIR, exist_ok=True)
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    headers = {'User-Agent': 'NetaPulse/1.0 (info@netapulse.org)'}

    updated_count = 0

    for r in rows:
        name = r['elected_person'].strip()
        current_photo = r.get('photo_source_url', '')

        # Check if prominent leader
        matched_url = None
        for p_name, p_url in PROMINENT_PORTRAITS.items():
            if p_name.lower() in name.lower() or name.lower() in p_name.lower():
                matched_url = p_url
                break

        if matched_url:
            local_filename = f"{sanitize_name(name)}.jpg"
            local_path = os.path.join(CANDIDATE_IMG_DIR, local_filename)
            try:
                resp = requests.get(matched_url, headers=headers, timeout=12)
                if resp.status_code == 200:
                    with open(local_path, "wb") as img_f:
                        img_f.write(resp.content)
                    r['photo_source_url'] = f"/assets/candidates/{local_filename}"
                    updated_count += 1
                    print(f"Downloaded portrait for: {name}")
            except Exception as e:
                print(f"Failed to fetch image for {name}: {e}")

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_count} high-profile portraits in constituency_master.csv!")

if __name__ == "__main__":
    download_and_assign_photos()
