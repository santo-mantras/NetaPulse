import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_goa():
    url = 'https://en.wikipedia.org/wiki/2022_Goa_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    table = None
    for t in tables:
        h = [th.text.strip() for th in t.find_all('th')]
        if 'District' in h and 'Constituency' in h and len(t.find_all('tr')) >= 40:
            table = t
            break
            
    if not table and len(tables) > 14:
        table = tables[14]

    data = []
    current_district = "North Goa"
    
    party_map = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'AAP': 'Aam Aadmi Party',
        'MGP': 'Maharashtrawadi Gomantak Party',
        'GFP': 'Goa Forward Party',
        'RGP': 'Revolutionary Goans Party',
        'IND': 'Independent'
    }

    for tr in table.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds or len(tds) < 5:
            continue
            
        row_text = [td.text.strip() for td in tds]
        if 'Turnout' in row_text or 'Winner' in row_text:
            continue

        if tds[0].has_attr('rowspan') and ('North' in tds[0].text or 'South' in tds[0].text):
            current_district = tds[0].text.strip()
            cols = tds[1:]
        elif 'North Goa' in tds[0].text or 'South Goa' in tds[0].text:
            current_district = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5:
            continue

        try:
            const_no = cols[0].text.strip()
            const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip())
            
            winner_cand = ""
            party = "Bharatiya Janata Party"
            for c in cols[2:]:
                txt = re.sub(r'\[.*?\]', '', c.text.strip())
                if txt in party_map:
                    party = party_map[txt]
                    break
            
            # Winner name is usually in col 3 or 4
            winner_cand = re.sub(r'\[.*?\]', '', cols[3].text.strip())
            if not winner_cand or winner_cand.isdigit():
                winner_cand = re.sub(r'\[.*?\]', '', cols[2].text.strip())
                
            if const_no.isdigit():
                data.append({
                    "state": "Goa",
                    "district": current_district,
                    "constituency_code": f"AC-GA-{const_no}",
                    "constituency_name": const_name,
                    "winner": winner_cand or "Elected MLA",
                    "party": party
                })
        except Exception:
            continue

    print(f"Goa scraped: {len(data)} constituencies")
    return data

def scrape_chhattisgarh():
    url = 'https://en.wikipedia.org/wiki/2023_Chhattisgarh_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    table = None
    for t in tables:
        h = [th.text.strip() for th in t.find_all('th')]
        if 'District' in h and 'Constituency' in h and len(t.find_all('tr')) >= 80:
            table = t
            break

    data = []
    current_district = "Raipur"
    
    party_map = {
        'BJP': 'Bharatiya Janata Party',
        'INC': 'Indian National Congress',
        'GVP': 'Gondwana Gantantra Party',
        'BSP': 'Bahujan Samaj Party',
        'IND': 'Independent'
    }

    for tr in table.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds or len(tds) < 5:
            continue
            
        row_text = [td.text.strip() for td in tds]
        if 'Turnout' in row_text or 'Winner' in row_text:
            continue

        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            current_district = tds[0].text.strip()
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 8:
            current_district = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5:
            continue

        try:
            const_no = cols[0].text.strip()
            const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip())
            current_district = re.sub(r'\[.*?\]', '', current_district).strip()
            
            winner_cand = ""
            party = "Bharatiya Janata Party"
            for c in cols[2:]:
                txt = re.sub(r'\[.*?\]', '', c.text.strip())
                if txt in party_map:
                    party = party_map[txt]
                    break
                    
            winner_cand = re.sub(r'\[.*?\]', '', cols[3].text.strip())
            if not winner_cand or winner_cand.isdigit():
                winner_cand = re.sub(r'\[.*?\]', '', cols[2].text.strip())

            if const_no.isdigit():
                data.append({
                    "state": "Chhattisgarh",
                    "district": current_district,
                    "constituency_code": f"AC-CG-{const_no}",
                    "constituency_name": const_name,
                    "winner": winner_cand or "Elected MLA",
                    "party": party
                })
        except Exception:
            continue

    print(f"Chhattisgarh scraped: {len(data)} constituencies")
    return data

def scrape_tamil_nadu():
    url = 'https://en.wikipedia.org/wiki/2021_Tamil_Nadu_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=25)
    soup = BeautifulSoup(resp.content, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    table = None
    for t in tables:
        h = [th.text.strip() for th in t.find_all('th')]
        if 'District' in h and 'Constituency' in h and len(t.find_all('tr')) >= 220:
            table = t
            break

    data = []
    current_district = "Chennai"
    
    party_map = {
        'DMK': 'Dravida Munnetra Kazhagam',
        'AIADMK': 'All India Anna Dravida Munnetra Kazhagam',
        'INC': 'Indian National Congress',
        'PMK': 'Pattali Makkal Katchi',
        'BJP': 'Bharatiya Janata Party',
        'VCK': 'Viduthalai Chiruthaigal Katchi',
        'CPI': 'Communist Party of India',
        'CPI(M)': 'Communist Party of India (Marxist)',
        'IND': 'Independent'
    }

    for tr in table.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds or len(tds) < 5:
            continue
            
        row_text = [td.text.strip() for td in tds]
        if 'Turnout' in row_text or 'Winner' in row_text:
            continue

        if tds[0].has_attr('rowspan') and not tds[0].text.strip().isdigit():
            current_district = tds[0].text.strip()
            cols = tds[1:]
        elif not tds[0].text.strip().isdigit() and len(tds) > 8:
            current_district = tds[0].text.strip()
            cols = tds[1:]
        else:
            cols = tds

        if len(cols) < 5:
            continue

        try:
            const_no = cols[0].text.strip()
            const_name = re.sub(r'\[.*?\]', '', cols[1].text.strip())
            current_district = re.sub(r'\[.*?\]', '', current_district).strip()
            
            party = "Dravida Munnetra Kazhagam"
            for c in cols[2:]:
                txt = re.sub(r'\[.*?\]', '', c.text.strip())
                if txt in party_map:
                    party = party_map[txt]
                    break
                    
            winner_cand = re.sub(r'\[.*?\]', '', cols[3].text.strip())
            if not winner_cand or winner_cand.isdigit():
                winner_cand = re.sub(r'\[.*?\]', '', cols[2].text.strip())

            if const_no.isdigit():
                data.append({
                    "state": "Tamil Nadu",
                    "district": current_district,
                    "constituency_code": f"AC-TN-{const_no}",
                    "constituency_name": const_name,
                    "winner": winner_cand or "Elected MLA",
                    "party": party
                })
        except Exception:
            continue

    print(f"Tamil Nadu scraped: {len(data)} constituencies")
    return data

if __name__ == "__main__":
    ga = scrape_goa()
    cg = scrape_chhattisgarh()
    tn = scrape_tamil_nadu()
    
    with open("scripts/pipeline/new_states_scraped.json", "w", encoding="utf-8") as f:
        json.dump({"Goa": ga, "Chhattisgarh": cg, "Tamil Nadu": tn}, f, indent=2, ensure_ascii=False)
