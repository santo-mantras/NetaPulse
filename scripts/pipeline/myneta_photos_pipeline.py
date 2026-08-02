import json
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import time

RAW_DATA_PATH = "scripts/pipeline/raw_maharashtra_real.json"
IMAGE_DIR = os.path.join("public", "assets", "candidates")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

def main():
    if not os.path.exists(RAW_DATA_PATH):
        print("raw_maharashtra_real.json not found.")
        return

    with open(RAW_DATA_PATH, 'r', encoding='utf-8') as f:
        candidates = json.load(f)

    missing_candidates = [c for c in candidates if not c.get('photoLocalPath')]
    print(f"Found {len(missing_candidates)} candidates missing photos. Searching MyNeta...")

    session = requests.Session()
    session.headers.update(HEADERS)

    for i, c in enumerate(missing_candidates):
        name = c['name']
        print(f"[{i+1}/{len(missing_candidates)}] Searching MyNeta for {name}...")
        
        # 1. Search MyNeta
        try:
            search_url = f"https://myneta.info/search_myneta.php?q={quote_plus(name)}"
            resp = session.get(search_url, timeout=10)
            soup = BeautifulSoup(resp.content, 'lxml')
            
            # Find the first link that belongs to maharashtra2019 or Maharashtra2024
            links = soup.find_all('a', href=lambda h: h and 'candidate.php' in h and 'maharashtra' in h.lower())
            
            if not links:
                print("  No candidate profile found on MyNeta.")
                continue
                
            profile_link = "https://myneta.info" + links[0]['href']
            
            # 2. Fetch Profile Page
            resp2 = session.get(profile_link, timeout=10)
            soup2 = BeautifulSoup(resp2.content, 'lxml')
            
            # Find image
            img = soup2.find('img', src=lambda s: s and ('uploads' in s or 'images_candidate' in s))
            if not img:
                print("  No photo found on MyNeta profile.")
                continue
                
            img_url = img['src']
            if not img_url.startswith('http'):
                img_url = "https://myneta.info" + img_url
                
            # 3. Download image
            img_resp = session.get(img_url, timeout=10)
            if img_resp.status_code == 200:
                # Save it
                c_id = c['id']
                file_ext = img_url.split('.')[-1].split('?')[0]
                if file_ext.lower() not in ['jpg', 'jpeg', 'png', 'gif']:
                    file_ext = 'jpg'
                filename = f"myneta_{c_id}.{file_ext}"
                filepath = os.path.join(IMAGE_DIR, filename)
                
                with open(filepath, 'wb') as img_f:
                    img_f.write(img_resp.content)
                    
                c['photoLocalPath'] = f"/jumlabaaz/assets/candidates/{filename}"
                print(f"  Success! Downloaded photo for {name}")
            else:
                print(f"  Failed to download image. Status {img_resp.status_code}")
                
        except Exception as e:
            print(f"  Error processing {name}: {str(e)}")
            
        # polite delay
        time.sleep(1)
        
    with open(RAW_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)
        
    print("MyNeta Photo Pipeline Complete! Updated raw_maharashtra_real.json")

if __name__ == "__main__":
    main()
