import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_state(url, state_name):
    print(f"Fetching data for {state_name}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    
    # MyNeta tables don't always have a clean id. Find all tables.
    tables = soup.find_all('table')
    candidates = []
    
    for table in tables:
        rows = table.find_all('tr')
        if not rows or len(rows) < 5:
            continue
            
        header = rows[0].text.lower()
        # Look for the table that has Candidate and Constituency columns
        if 'candidate' in header and 'constituency' in header and 'party' in header:
            for row in rows[1:]: # Skip header
                cols = row.find_all('td')
                if len(cols) >= 6:
                    name = cols[1].text.strip()
                    constituency = cols[2].text.strip()
                    party = cols[3].text.strip()
                    criminal_cases = cols[4].text.strip()
                    education = cols[5].text.strip()
                    
                    try:
                        cases = int(criminal_cases)
                    except:
                        cases = 0
                        
                    candidates.append({
                        "name": name,
                        "constituency": constituency,
                        "party": party,
                        "criminalCasesCount": cases,
                        "education": education
                    })
            break # We found the right table
            
    print(f"Successfully scraped {len(candidates)} candidates from {state_name}")
    return candidates

def main():
    # MyNeta "All Candidates" pages
    urls = {
        "Maharashtra": "https://myneta.info/maharashtra2019/index.php?action=show_candidates&dir=ASC",
        "Punjab": "https://myneta.info/Punjab2022/index.php?action=show_candidates&dir=ASC"
    }
    
    all_data = {}
    for state, url in urls.items():
        data = scrape_state(url, state)
        all_data[state] = data
        time.sleep(2) # Be polite
        
    with open("scripts/pipeline/raw_myneta.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)
        
if __name__ == "__main__":
    main()
