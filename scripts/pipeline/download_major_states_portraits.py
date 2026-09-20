import os
import requests
from PIL import Image

HEADERS = {
    'User-Agent': 'NetaPulseBot/1.0 (santosh.verma01073@gmail.com) Python-requests/2.31'
}

DEST_DIR = "public/assets/candidates"
os.makedirs(DEST_DIR, exist_ok=True)

WIKI_LEADERS = {
    "mohan_charan_majhi.jpg": "Mohan Charan Majhi",
    "naveen_patnaik.jpg": "Naveen Patnaik",
    "mohan_yadav.jpg": "Mohan Yadav",
    "shivraj_singh_chouhan.jpg": "Shivraj Singh Chouhan",
    "kamal_nath.jpg": "Kamal Nath",
    "pushkar_singh_dhami.jpg": "Pushkar Singh Dhami",
    "harish_rawat.jpg": "Harish Rawat"
}

def download_portraits():
    print("[PORTRAITS] Downloading authentic portraits from Wikipedia API...")
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
                if resp.status_code == 200 and len(resp.content) > 4096:
                    with open(filepath, 'wb') as f:
                        f.write(resp.content)
                    im = Image.open(filepath)
                    print(f"  [SUCCESS] {filename} ({im.width}x{im.height}, {os.path.getsize(filepath)//1024} KB)")
                else:
                    print(f"  [FAIL CONTENT] {filename}")
            else:
                print(f"  [NO THUMB] {title}")
        except Exception as e:
            print(f"  [ERROR] {filename}: {e}")

if __name__ == "__main__":
    download_portraits()
