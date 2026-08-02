import json
import os
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import time

DATA_FILE = "scripts/pipeline/raw_maharashtra_real.json"
OUTPUT_DIR = "public/assets/candidates"

HEADERS = {
    'User-Agent': 'JumlebaazBot/1.0 (Contact: admin@jumlebaaz.app) python-requests/2.x'
}

def fetch_wiki_photo(candidate):
    if not candidate.get('wikiUrl'):
        return candidate
        
    # Skip if we already have a valid local photo and the file exists
    existing_photo = candidate.get('photoLocalPath')
    if existing_photo and existing_photo.startswith('/assets/candidates/'):
        filename = existing_photo.split('/')[-1]
        if os.path.exists(os.path.join(OUTPUT_DIR, filename)):
            return candidate
            
    print(f"Fetching photo for {candidate['name']}...")
    try:
        time.sleep(0.5) # Be nice to Wikipedia
        resp = requests.get(candidate['wikiUrl'], headers=HEADERS, timeout=10)
        
        if resp.status_code != 200:
            print(f"Failed to fetch {candidate['wikiUrl']} - Status {resp.status_code}")
            return candidate
            
        soup = BeautifulSoup(resp.content, 'lxml')
        
        # Find all infoboxes
        infoboxes = soup.find_all('table', class_='infobox')
        img_url = None
        
        for infobox in infoboxes:
            img = infobox.find('img')
            if img and 'src' in img.attrs:
                img_src = img['src']
                if img_src.startswith('//'):
                    img_url = 'https:' + img_src
                elif img_src.startswith('/'):
                    img_url = 'https://en.wikipedia.org' + img_src
                else:
                    img_url = img_src
                break # Found the first image in an infobox
                
        if img_url:
            # Increase resolution if it's a thumb
            img_url = img_url.replace('220px-', '500px-').replace('150px-', '500px-')
            
            img_resp = requests.get(img_url, headers=HEADERS, timeout=10)
            if img_resp.status_code == 200:
                filename = f"wiki_{candidate['id']}.jpg"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, 'wb') as f:
                    f.write(img_resp.content)
                candidate['photoLocalPath'] = f"/assets/candidates/{filename}"
                print(f"Success: {candidate['name']}")
            else:
                print(f"Failed to download image for {candidate['name']}")
        else:
            print(f"No image found in infobox for {candidate['name']}")
            
    except Exception as e:
        print(f"Error for {candidate['name']}: {e}")
        
    return candidate

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)
        
    print(f"Starting Profile Pics Pipeline for {len(candidates)} candidates...")
    
    # Using 5 workers to avoid hitting limits too hard
    enriched = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(fetch_wiki_photo, candidates)
        for c in results:
            enriched.append(c)
            
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
        
    print("Pipeline Complete! Updated raw_maharashtra_real.json")

if __name__ == "__main__":
    main()
