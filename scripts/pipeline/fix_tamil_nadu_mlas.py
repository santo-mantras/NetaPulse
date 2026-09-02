import requests
from bs4 import BeautifulSoup
import json
import re
import csv

def scrape_and_fix_tamil_nadu():
    url = 'https://en.wikipedia.org/wiki/2021_Tamil_Nadu_Legislative_Assembly_election'
    resp = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}, timeout=25)
    soup = BeautifulSoup(resp.content, 'html.parser')

    # Table 9 is the clean alliance candidates table with:
    # [District, No., Name, swatch, Party, Candidate, swatch, Party, Candidate]
    # In TN 2021, the SPA (DMK+INC+VCK+CPI+CPM) won 159 seats, NDA won 75 seats.
    # Also table 18 has the official winners. Let's build from Table 18 first (the actual election results with votes and winners)
    
    t18 = soup.find_all('table', {'class': 'wikitable'})[18]

    party_map = {
        'DMK': 'Dravida Munnetra Kazhagam',
        'AIADMK': 'All India Anna Dravida Munnetra Kazhagam',
        'ADMK': 'All India Anna Dravida Munnetra Kazhagam',
        'INC': 'Indian National Congress',
        'PMK': 'Pattali Makkal Katchi',
        'BJP': 'Bharatiya Janata Party',
        'VCK': 'Viduthalai Chiruthaigal Katchi',
        'CPI': 'Communist Party of India',
        'CPI(M)': 'Communist Party of India (Marxist)',
        'CPM': 'Communist Party of India (Marxist)',
        'IND': 'Independent'
    }

    # Also build lookup from Table 9 for fallback
    t9 = soup.find_all('table', {'class': 'wikitable'})[9]
    t9_candidates = {}
    curr_dist_t9 = "Chennai"
    for tr in t9.find_all('tr'):
        tds = [td.text.strip() for td in tr.find_all(['td', 'th'])]
        if not tds:
            continue
        if tds[0] and not tds[0].isdigit() and len(tds) > 6:
            curr_dist_t9 = tds[0].replace('District', '').strip()
            cols = tds[1:]
        else:
            cols = tds
        if len(cols) >= 5 and cols[0].isdigit():
            cno = cols[0]
            cname = re.sub(r'\[.*?\]', '', cols[1]).strip()
            # In table 9: cols[0]=No, cols[1]=Name, cols[2]='', cols[3]=Party, cols[4]=Candidate
            p1 = re.sub(r'\[.*?\]', '', cols[3]).strip() if len(cols) > 3 else ''
            cand1 = re.sub(r'\[.*?\]', '', cols[4]).strip() if len(cols) > 4 else ''
            t9_candidates[cname.lower()] = (cand1, p1)
            # also normalized without (SC)/(ST)
            clean_name = re.sub(r'\s*\((?:SC|ST)\)', '', cname, flags=re.IGNORECASE).strip().lower()
            t9_candidates[clean_name] = (cand1, p1)

    # Now parse Table 18 (Results Table)
    tn_winners = {}
    curr_dist = "Chennai"

    for tr in t18.find_all('tr'):
        tds = tr.find_all(['td', 'th'])
        if not tds:
            continue
        if len(tds) == 1 and 'District' in tds[0].text:
            curr_dist = tds[0].text.replace('District', '').strip()
            continue
        
        row_txt = [re.sub(r'\[.*?\]', '', td.text.strip()) for td in tds]
        if not row_txt or not row_txt[0].isdigit():
            continue

        c_no = row_txt[0]
        c_name = row_txt[1]
        
        # Look for the winner name and party in the row
        # In Table 18, row format is:
        # ['1', 'Gummidipoondi', '78.84', 'T. J. Govindrajan', '', 'DMK', '126,452', ...]
        winner_name = ""
        winner_party = ""

        if len(row_txt) >= 6:
            # check candidate name and party
            cand = row_txt[3]
            party = row_txt[5] if row_txt[5] in party_map else row_txt[4]
            if cand and party in party_map and cand not in party_map:
                winner_name = cand
                winner_party = party_map.get(party, party)

        # If winner wasn't extracted cleanly, fall back to table 9
        clean_cname = re.sub(r'\s*\((?:SC|ST)\)', '', c_name, flags=re.IGNORECASE).strip().lower()
        if not winner_name or winner_name in party_map:
            if clean_cname in t9_candidates:
                cand, p = t9_candidates[clean_cname]
                if cand and cand not in party_map:
                    winner_name = cand
                    winner_party = party_map.get(p, p)

        if winner_name and winner_name not in party_map:
            clean_key = clean_cname
            tn_winners[clean_key] = {
                'constituency_code': f"AC-TN-{c_no}",
                'constituency_name': c_name,
                'district': curr_dist,
                'winner': winner_name,
                'party': winner_party
            }

    print(f"Scraped {len(tn_winners)} accurate Tamil Nadu winners!")
    for k, v in list(tn_winners.items())[:5]:
        print(f"  {v['constituency_name']} ({v['district']}): {v['winner']} | {v['party']}")

    # Apply to constituency_master.csv
    csv_path = "scripts/pipeline/constituency_master.csv"
    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    fieldnames = rows[0].keys()
    updated_tn = 0

    for r in rows:
        if r['state'] == "Tamil Nadu":
            cname = r['constituency_name'].strip()
            clean_key = re.sub(r'\s*\((?:SC|ST)\)', '', cname, flags=re.IGNORECASE).strip().lower()
            
            if clean_key in tn_winners:
                w_info = tn_winners[clean_key]
                if r['elected_person'] != w_info['winner']:
                    r['elected_person'] = w_info['winner']
                    if w_info['party']:
                        r['party'] = w_info['party']
                    r['bio'] = f"{w_info['winner']} is the elected MLA representing {cname}, {r['district']}, Tamil Nadu."
                    updated_tn += 1

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nUpdated {updated_tn} Tamil Nadu candidate names in constituency_master.csv!")

if __name__ == "__main__":
    scrape_and_fix_tamil_nadu()
