import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_bihar_official():
    url = 'https://en.wikipedia.org/wiki/2020_Bihar_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    # Table 9 is the official constituency results table
    table = soup.find_all('table', {'class': 'wikitable'})[9]
    
    current_district = "West Champaran"
    results = []

    party_map = {
        'RJD': 'Rashtriya Janata Dal',
        'BJP': 'Bharatiya Janata Party',
        'JD(U)': 'Janata Dal (United)',
        'JDU': 'Janata Dal (United)',
        'INC': 'Indian National Congress',
        'CPI(ML)L': 'Communist Party of India (Marxist-Leninist) Liberation',
        'AIMIM': 'All India Majlis-e-Ittehadul Muslimeen',
        'VIP': 'Vikassheel Insaan Party',
        'HAM(S)': 'Hindustani Awam Morcha (Secular)',
        'CPI': 'Communist Party of India',
        'CPI(M)': 'Communist Party of India (Marxist)',
        'BSP': 'Bahujan Samaj Party',
        'LJP': 'Lok Janshakti Party',
        'IND': 'Independent'
    }

    rows = table.find_all('tr')
    for tr in rows[2:]:
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue

        # Check for district spanning cell
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            raw_dist = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            # Clean compound words like WestChamparan -> West Champaran, EastChamparan -> East Champaran
            current_district = re.sub(r'([a-z])([A-Z])', r'\1 \2', raw_dist)
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 9:
            raw_dist = re.sub(r'\[.*?\]', '', tds[0].text).replace('District', '').strip()
            current_district = re.sub(r'([a-z])([A-Z])', r'\1 \2', raw_dist)
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
        # cols[4] = Party acronym (swatch column in between)
        party_short = re.sub(r'\[.*?\]', '', cols[4].text.strip()).strip()
        if party_short not in party_map and cols[3].text.strip() in party_map:
            party_short = cols[3].text.strip()
            
        party_full = party_map.get(party_short, party_short or 'Rashtriya Janata Dal')

        results.append({
            'state': 'Bihar',
            'district': current_district,
            'constituency_code': f"AC-BR-{cno}",
            'constituency_name': cname,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Scraped {len(results)} Bihar assembly constituencies!")
    dists = set(r['district'] for r in results)
    print(f"Districts covered: {len(dists)}")
    for r in results[:5]:
        print(f"  {r['constituency_code']} {r['constituency_name']} ({r['district']}): {r['winner']} | {r['party']}")

    return results

if __name__ == "__main__":
    res = scrape_bihar_official()
    with open("scripts/pipeline/br_scraped_243.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
