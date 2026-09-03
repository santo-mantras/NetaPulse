import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_kerala_official():
    url = 'https://en.wikipedia.org/wiki/2021_Kerala_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    
    table = soup.find_all('table', {'class': 'wikitable'})[13]
    
    current_district = "Kasaragod"
    results = []

    party_map = {
        'CPI(M)': 'Communist Party of India (Marxist)',
        'CPM': 'Communist Party of India (Marxist)',
        'CPI': 'Communist Party of India',
        'INC': 'Indian National Congress',
        'IUML': 'Indian Union Muslim League',
        'KC(M)': 'Kerala Congress (M)',
        'KEC(M)': 'Kerala Congress (M)',
        'JD(S)': 'Janata Dal (Secular)',
        'JDS': 'Janata Dal (Secular)',
        'NCP': 'Nationalist Congress Party',
        'KC(B)': 'Kerala Congress (B)',
        'KC(J)': 'Kerala Congress (Jacob)',
        'RSP': 'Revolutionary Socialist Party',
        'CPO': 'Congress (Secular)',
        'NSC': 'National Secular Conference',
        'IND': 'Independent'
    }

    rows = table.find_all('tr')
    for tr in rows[2:]:
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue

        # Check for single cell row indicating District
        if len(tds) == 1 and ('district' in tds[0].text.lower() or 'division' in tds[0].text.lower()):
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('district', '').replace('District', '').strip()
            current_district = raw_d or current_district
            continue

        # Check for district spanning cell
        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('district', '').replace('District', '').strip()
            current_district = raw_d or current_district
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 9:
            raw_d = re.sub(r'\[.*?\]', '', tds[0].text).replace('district', '').replace('District', '').strip()
            current_district = raw_d or current_district
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5 or not cols[0].text.strip().isdigit():
            continue

        cno = cols[0].text.strip()
        raw_cname = re.sub(r'\[.*?\]', '', cols[1].text.strip()).strip()
        cname = re.sub(r'\s*\((?:SC|ST)\)', '', raw_cname, flags=re.IGNORECASE).strip()
        
        # cols[3] = Candidate name
        cand_name = re.sub(r'\[.*?\]', '', cols[3].text.strip()).strip()
        # cols[5] = Party acronym (swatch column at 4)
        party_short = re.sub(r'\[.*?\]', '', cols[5].text.strip()).strip()
        if party_short not in party_map and cols[4].text.strip() in party_map:
            party_short = cols[4].text.strip()
            
        party_full = party_map.get(party_short, party_short or 'Communist Party of India (Marxist)')

        results.append({
            'state': 'Kerala',
            'district': current_district,
            'constituency_code': f"AC-KL-{cno}",
            'constituency_name': cname,
            'winner': cand_name,
            'party': party_full
        })

    print(f"Scraped {len(results)} Kerala assembly constituencies!")
    dists = set(r['district'] for r in results)
    print(f"Districts covered: {len(dists)}")
    for r in results[:5]:
        print(f"  {r['constituency_code']} {r['constituency_name']} ({r['district']}): {r['winner']} | {r['party']}")

    return results

if __name__ == "__main__":
    res = scrape_kerala_official()
    with open("scripts/pipeline/kl_scraped_140.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2, ensure_ascii=False)
