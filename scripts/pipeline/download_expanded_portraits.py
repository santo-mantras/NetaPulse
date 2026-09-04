import os
import requests
import time

CANDIDATE_IMG_DIR = "public/assets/candidates"
os.makedirs(CANDIDATE_IMG_DIR, exist_ok=True)

HEADERS = {'User-Agent': 'NetaPulseBot/1.0 (https://netapulse.in; contact@netapulse.in)'}

PORTRAITS = {
    # Haryana
    "nayab_singh_saini.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Nayab_Singh_Saini_October_2024.jpg",
    "bhupinder_singh_hooda.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Bhupinder_Singh_Hooda_in_WEF%2C_2010.jpg/500px-Bhupinder_Singh_Hooda_in_WEF%2C_2010.jpg",
    "anil_vij.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Anil_Vij_-_Kolkata_2016-10-07_8232.JPG/500px-Anil_Vij_-_Kolkata_2016-10-07_8232.JPG",
    "dushyant_chautala.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Dushyant_chautala_at_public_meeting_2014-05-21_13-02.jpeg/500px-Dushyant_chautala_at_public_meeting_2014-05-21_13-02.jpeg",
    "vinesh_phogat.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/da/Vinesh_Phogat.jpg",
    
    # Telangana
    "revanth_reddy.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Portrait_of_Telangana_CM_Revanth_Reddy.png/500px-Portrait_of_Telangana_CM_Revanth_Reddy.png",
    "mallu_bhatti_vikramarka.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Portrait_of_Telangana_Deputy_CM_Bhatti_Vikramarka_Mallu_%284_July_2024%29.png/500px-Portrait_of_Telangana_Deputy_CM_Bhatti_Vikramarka_Mallu_%284_July_2024%29.png",
    "kcr.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Kalvakuntla_Chandrashekar_Rao.png",
    "ktr.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Kalvakuntla_Taraka_Rama_Rao.jpg/500px-Kalvakuntla_Taraka_Rama_Rao.jpg",
    "t_harish_rao.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Harish_Rao_PROFILE.jpg/500px-Harish_Rao_PROFILE.jpg",
    "akbaruddin_owaisi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Akbaruddin_Owaisi_Picture.jpg/500px-Akbaruddin_Owaisi_Picture.jpg",
    "asaduddin_owaisi.jpg": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Asaduddin.jpg/500px-Asaduddin.jpg",

    # Jammu & Kashmir
    "omar_abdullah.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/68/Omar_Abdullah%2C_Chief_Minister_of_Jammu_%26_Kashmir.jpg",
    "mehbooba_mufti.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Mehbooba_Mufti_addressing_a_press_conference_in_Srinagar.jpg"
}

for fname, url in PORTRAITS.items():
    dest = os.path.join(CANDIDATE_IMG_DIR, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 3000:
        print(f"Skipping {fname} (already downloaded)")
        continue
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code == 200 and len(r.content) > 1000:
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"Downloaded {fname} ({len(r.content)} bytes)")
        else:
            print(f"Failed {fname}: Status {r.status_code}")
        time.sleep(0.5)
    except Exception as e:
        print(f"Error {fname}: {e}")
