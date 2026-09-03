import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_assam_official():
    url = 'https://en.wikipedia.org/wiki/2021_Assam_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    table = soup.find_all('table', {'class': 'wikitable'})[11]
    
    current_district = "Karimganj"
    results = []

    party_map = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'AIUDF': 'All India United Democratic Front',
        'AGP': 'Asom Gana Parishad',
        'UPPL': 'United People\'s Party Liberal',
        'BPF': 'Bodoland People\'s Front',
        'CPI(M)': 'Communist Party of India (Marxist)',
        'IND': 'Independent',
        'RD': 'Raijor Dal'
    }

    rows = table.find_all('tr')
    for tr in rows[2:]:
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue

        # Check for single cell row indicating District
        if len(tds) == 1 and ('District' in tds[0].text or 'division' in tds[0].text.lower()):
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            current_district = raw_d or current_district
            continue

        # Check for district spanning cell
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            current_district = raw_d or current_district
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 9:
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            current_district = raw_d or current_district
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
            'state': 'Assam',
            'district': current_district,
            'constituency_code': f"AC-AS-{cno}",
            'constituency_name': cname,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Scraped {len(results)} Assam assembly constituencies!")
    dists = set(r['district'] for r in results)
    print(f"Districts covered: {len(dists)}")
    for r in results[:5]:
        print(f"  {r['constituency_code']} {r['constituency_name']} ({r['district']}): {r['winner']} | {r['party']}")

    return results

if __name__ == "__main__":
    res = scrape_assam_official()
    with open("scripts/pipeline/as_scraped_126.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
