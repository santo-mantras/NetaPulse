import os
import requests
import time
from PIL import Image

HEADERS = {
    'User-Agent': 'NetaPulseBot/1.0 (santosh.verma01073@gmail.com) Python-requests/2.31'
}

DEST_DIR = "public/assets/candidates"
os.makedirs(DEST_DIR, exist_ok=True)

WIKI_LEADERS = {
    "hemant_soren.jpg": "Hemant Soren",
    "babulal_marandi.jpg": "Babulal Marandi",
    "champai_soren.jpg": "Champai Soren",
    "kalpana_soren.jpg": "Kalpana Soren",
    "sukhvinder_singh_sukhu.jpg": "Sukhvinder Singh Sukhu",
    "mukesh_agnihotri.jpg": "Mukesh Agnihotri",
    "jairam_thakur.jpg": "Jai Ram Thakur",
    "vikramaditya_singh.jpg": "Vikramaditya Singh (Himachal Pradesh politician)",
    "chandrababu_naidu.jpg": "N. Chandrababu Naidu",
    "pawan_kalyan.jpg": "Pawan Kalyan",
    "jagan_mohan_reddy.jpg": "Y. S. Jagan Mohan Reddy",
    "nara_lokesh.jpg": "Nara Lokesh",
    "n_rangasamy.jpg": "N. Rangaswamy",
    "manish_tewari.jpg": "Manish Tewari",
    "rahul_gandhi.jpg": "Rahul Gandhi"
}

def download_via_api():
    for filename, title in WIKI_LEADERS.items():
        filepath = os.path.join(DEST_DIR, filename)
        try:
            api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={requests.utils.quote(title)}&prop=pageimages&format=json&pithumbsize=500"
            r = requests.get(api_url, headers=HEADERS, timeout=10).json()
            pages = r.get('query', {}).get('pages', {})
            thumb_url = None
            for p in pages.values():
                if 'thumbnail' in p:
                    thumb_url = p['thumbnail']['source']
                    break
            
            if thumb_url:
                resp = requests.get(thumb_url, headers=HEADERS, timeout=12)
                if resp.status_code == 200 and len(resp.content) > 4000:
                    with open(filepath, 'wb') as f:
                        f.write(resp.content)
                    with Image.open(filepath) as img:
                        print(f"SUCCESS: {filename} from {title} ({img.size[0]}x{img.size[1]}, {len(resp.content)} bytes)")
                else:
                    print(f"FAILED fetch image for {title}: status={resp.status_code}, len={len(resp.content)}")
            else:
                print(f"NO THUMBNAIL for {title}")
            time.sleep(0.5)
        except Exception as e:
            print(f"ERROR {filename}: {e}")

if __name__ == "__main__":
    download_via_api()
