import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_gujarat_official():
    url = 'https://en.wikipedia.org/wiki/2022_Gujarat_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Table 17 is the verified constituency results table
    table = soup.find_all('table', {'class': 'wikitable'})[17]
    
    current_district = "Kutch"
    results = []

    party_map = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'AAP': 'Aam Aadmi Party',
        'SP': 'Samajwadi Party',
        'IND': 'Independent'
    }

    rows = table.find_all('tr')
    for tr in rows[2:]:
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue

        # Check for district spanning cell
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            current_district = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 9:
            current_district = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5 or not cols[0].text.strip().isdigit():
            continue

        cno = cols[0].text.strip()
        raw_cname = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
        cname = re.sub(r'\s*\((?:SC|ST)\)', '', raw_cname, flags=re.IGNORECASE).strip()
        
        # cols[2] = Candidate name
        cand_name = re.sub(r'\[.*?\]', '', cols[2].text.strip()).strip()
        # cols[4] = Party acronym
        party_short = re.sub(r'\[.*?\]', '', cols[4].text.strip()).strip()
        if party_short not in party_map and cols[3].text.strip() in party_map:
            party_short = cols[3].text.strip()
            
        party_full = party_map.get(party_short, party_short or 'Bharatiya Janata Party')

        results.append({
            'state': 'Gujarat',
            'district': current_district,
            'constituency_code': f"AC-GJ-{cno}",
            'constituency_name': cname,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Scraped {len(results)} Gujarat assembly constituencies!")
    dists = set(r['district'] for r in results)
    print(f"Districts covered: {len(dists)}")
    for r in results[:5]:
        print(f"  {r['constituency_code']} {r['constituency_name']} ({r['district']}): {r['winner']} | {r['party']}")

    return results

if __name__ == "__main__":
    res = scrape_gujarat_official()
    with open("scripts/pipeline/gj_scraped_182.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
