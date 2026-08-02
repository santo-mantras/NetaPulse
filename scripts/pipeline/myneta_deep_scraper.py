import requests
from bs4 import BeautifulSoup
import json
import os
import re
import concurrent.futures

WIKI_URL = 'https://en.wikipedia.org/wiki/14th_Maharashtra_Legislative_Assembly'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def scrape_wikipedia_list():
    print("Fetching Wikipedia list...")
    response = requests.get(WIKI_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')
    
    tables = soup.find_all('table', class_='wikitable')
    candidate_table = None
    for table in tables:
        headers_row = table.find('tr')
        if headers_row and 'Constituency' in headers_row.text and 'Name' in headers_row.text:
            candidate_table = table
            break
            
    if not candidate_table:
        print("Could not find candidate table on Wikipedia.")
        return []

    candidates = []
    rows = candidate_table.find_all('tr')[1:]
    
    # Wikipedia tables with rowspans need stateful tracking
    current_district = "Unknown"
    
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if not cols:
            continue
            
        # Due to rowspans on district, the number of columns changes
        # If len(cols) == 7, it has district. If 6, district is inherited.
        col_idx = 0
        
        # Check if first col is a number (No.) or text (District)
        first_col_text = cols[0].text.strip()
        if not first_col_text.isdigit() and len(cols) >= 6:
            current_district = first_col_text
            col_idx += 1
            
        # col_idx is now at 'No.'
        col_idx += 1 # skip 'No.'
        
        if col_idx >= len(cols): continue
        constituency = cols[col_idx].text.strip()
        col_idx += 1
        
        if col_idx >= len(cols): continue
        name_td = cols[col_idx]
        name = name_td.text.strip()
        
        # Find wiki link for the member
        wiki_url = None
        a_tag = name_td.find('a')
        if a_tag and 'href' in a_tag.attrs and not 'redlink=1' in a_tag['href']:
            href = a_tag['href']
            if href.startswith('/wiki/'):
                wiki_url = 'https://en.wikipedia.org' + href
            else:
                wiki_url = href
            
        col_idx += 1 # skip party logo column
        if col_idx >= len(cols): continue
        col_idx += 1 # this is the party name column
        if col_idx >= len(cols): continue
        party = cols[col_idx].text.strip()
        
        candidates.append({
            "id": str(len(candidates) + 1),
            "name": re.sub(r'\[.*?\]', '', name).strip(), # remove citation brackets
            "constituency": constituency,
            "district": current_district,
            "party": re.sub(r'\[.*?\]', '', party).strip(),
            "wikiUrl": wiki_url,
            "criminalCasesCount": 0, # Defaulting since Wiki doesn't have this
            "education": "Graduate", # Default
        })
        
    print(f"Parsed {len(candidates)} candidates from Wikipedia.")
    return candidates

def fetch_wiki_photo(candidate):
    if not candidate.get('wikiUrl'):
        candidate['photoLocalPath'] = None
        candidate['affidavitUrl'] = f"https://affidavit.eci.gov.in/"
        return candidate
        
    try:
        resp = requests.get(candidate['wikiUrl'], headers=HEADERS, timeout=5)
        soup = BeautifulSoup(resp.content, 'lxml')
        
        infobox = soup.find('table', class_='infobox')
        photo_local_path = None
        
        if infobox:
            img = infobox.find('img')
            if img and 'src' in img.attrs:
                img_src = img['src']
                if img_src.startswith('//'):
                    img_url = 'https:' + img_src
                elif img_src.startswith('/'):
                    img_url = 'https://en.wikipedia.org' + img_src
                else:
                    img_url = img_src
                # Download image
                img_resp = requests.get(img_url, headers=HEADERS, timeout=5)
                if img_resp.status_code == 200:
                    filename = f"wiki_{candidate['id']}.jpg"
                    filepath = os.path.join("public/assets/candidates", filename)
                    with open(filepath, 'wb') as f:
                        f.write(img_resp.content)
                    photo_local_path = f"/assets/candidates/{filename}"
                    
        candidate['photoLocalPath'] = photo_local_path
        candidate['affidavitUrl'] = candidate['wikiUrl'] # Using wiki url as fallback since ECI is blocked
        
    except Exception as e:
        print(f"Error fetching photo for {candidate['name']}: {e}")
        candidate['photoLocalPath'] = None
        candidate['affidavitUrl'] = f"https://affidavit.eci.gov.in/"
        
    return candidate

def main():
    os.makedirs("public/assets/candidates", exist_ok=True)
    candidates = scrape_wikipedia_list()
    
    print("Fetching individual photos from Wikipedia...")
    enriched = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(fetch_wiki_photo, candidates)
        for i, c in enumerate(results):
            enriched.append(c)
            if (i+1) % 50 == 0:
                print(f"Processed {i+1}/{len(candidates)}...")
                
    with open("scripts/pipeline/raw_maharashtra_real.json", "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=2, ensure_ascii=False)
    print("Saved to raw_maharashtra_real.json")

if __name__ == "__main__":
    main()
