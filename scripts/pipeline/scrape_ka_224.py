import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_karnataka_fixed():
    url = 'https://en.wikipedia.org/wiki/2023_Karnataka_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    target_table = None
    for t in tables:
        headers = [th.text.strip() for th in t.find_all('th')]
        if 'District' in headers and 'Constituency' in headers:
            target_table = t
            break

    data = []
    current_district = ""

    party_map = {
        'INC': 'Indian National Congress',
        'BJP': 'Bharatiya Janata Party',
        'JD(S)': 'Janata Dal (Secular)',
        'JDS': 'Janata Dal (Secular)',
        'IND': 'Independent',
        'KRPP': 'Kalyana Rajya Pragathi Paksha',
        'SKP': 'Sarvodaya Karnataka Paksha'
    }

    for tr in target_table.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue
            
        row_text = [td.text.strip() for td in tds]
        if 'Turnout' in row_text or 'Runner-up' in row_text or ('Candidate' in row_text and 'Winner' not in row_text):
            continue

        # Check if first element is district or number
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            current_district = tds[0].text.strip()
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 10:
            current_district = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 6:
            continue

        try:
            const_no = cols[0].text.strip()
            const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
            
            if not const_no.isdigit():
                continue

            # In this table structure:
            # cols[0] = No.
            # cols[1] = Name
            # cols[2] = Turnout %
            # cols[3] = Winner Candidate Name
            # cols[4] = empty (color swatch)
            # cols[5] = Winner Party
            candidate_name = re.sub(r'\[.*?\]', '', cols[3].text.strip()).strip()
            party_short = re.sub(r'\[.*?\]', '', cols[5].text.strip()).strip()
            
            # Fallback if swatch column was absent
            if party_short not in party_map and cols[4].text.strip() in party_map:
                party_short = cols[4].text.strip()
                
            party_full = party_map.get(party_short, party_short or 'Independent')

            if candidate_name and const_name:
                data.append({
                    "state": "Karnataka",
                    "district": current_district,
                    "constituency_code": f"AC-KA-{const_no}",
                    "constituency_name": const_name,
                    "winner": candidate_name,
                    "party": party_full
                })
        except Exception:
            continue

    print(f"Scraped {len(data)} Karnataka constituencies with ACTUAL winner names!")
    for s in data[:5]:
        print(f"  {s['constituency_name']} ({s['district']}): {s['winner']} ({s['party']})")
    return data

if __name__ == "__main__":
    res = scrape_karnataka_fixed()
    with open("scripts/pipeline/ka_scraped_224.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
