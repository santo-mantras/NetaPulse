import os
import csv
import json
import requests
import urllib.parse
import re
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
CSV_PATH = os.path.join(BASE_DIR, "scripts/pipeline/constituency_master.csv")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
IMG_DIR = os.path.join(PUBLIC_DIR, "assets/candidates")
os.makedirs(IMG_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Curated High-Profile Direct Wikimedia URLs for all 4 states
CURATED_PORTRAITS = {
    # Uttar Pradesh
    "Yogi Adityanath": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Yogiji_in_2023.jpg/500px-Yogiji_in_2023.jpg",
    "Ravi Kishan": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Ravi_Kissen_at_the_launch_of_T_P_Aggarwal%27s_trade_magazine_%27Blockbuster%27_20.jpg/500px-Ravi_Kissen_at_the_launch_of_T_P_Aggarwal%27s_trade_magazine_%27Blockbuster%27_20.jpg",
    "Brajesh Pathak": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Brajesh_Pathak.jpg/500px-Brajesh_Pathak.jpg",
    "Pankaj Singh": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Pankaj_Singh_-_politician.jpg",
    "Akhilesh Yadav": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Akhilesh_Yadav_544.jpg/500px-Akhilesh_Yadav_544.jpg",
    "Keshav Prasad Maurya": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Keshav_Prasad_Maurya_in_2023.jpg/500px-Keshav_Prasad_Maurya_in_2023.jpg",
    "Suresh Kumar Khanna": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Suresh_Kumar_Khanna.jpg/500px-Suresh_Kumar_Khanna.jpg",
    "Baby Rani Maurya": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Baby_Rani_Maurya_in_2022.jpg/500px-Baby_Rani_Maurya_in_2022.jpg",
    "Swatantra Dev Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Swatantra_Dev_Singh.jpg/500px-Swatantra_Dev_Singh.jpg",
    "Dharampal Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Dharampal_Singh.jpg/500px-Dharampal_Singh.jpg",
    "Surya Pratap Shahi": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Surya_Pratap_Shahi.jpg/500px-Surya_Pratap_Shahi.jpg",
    "Nand Gopal Gupta": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Nand_Gopal_Gupta.jpg/500px-Nand_Gopal_Gupta.jpg",
    "Dara Singh Chauhan": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Dara_Singh_Chauhan.jpg/500px-Dara_Singh_Chauhan.jpg",
    "Shrikant Sharma": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Shrikant_Sharma.jpg/500px-Shrikant_Sharma.jpg",
    "Satish Mahana": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Satish_Mahana.jpg/500px-Satish_Mahana.jpg",
    "Siddharth Nath Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Siddharth_Nath_Singh.jpg/500px-Siddharth_Nath_Singh.jpg",

    # Karnataka
    "Siddaramaiah": "https://upload.wikimedia.org/wikipedia/commons/0/06/Siddaramaiah_at_the_function_Akshaya_Patra_Foundation_in_Karnataka.jpg",
    "D.K. Shivakumar": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Dkshivakumar.png/500px-Dkshivakumar.png",
    "B.S. Yediyurappa": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/B._S._Yediyurappa_in_2020.jpg/500px-B._S._Yediyurappa_in_2020.jpg",
    "Basavaraj Bommai": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Basavaraj_Bommai_2022_%28cropped%29.jpg/500px-Basavaraj_Bommai_2022_%28cropped%29.jpg",
    "H. D. Kumaraswamy": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/H_D_Kumaraswamy_2018.jpg/500px-H_D_Kumaraswamy_2018.jpg",
    "G. Parameshwara": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Dr._G._Parameshwara.jpg/500px-Dr._G._Parameshwara.jpg",
    "M. B. Patil": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/M_B_Patil.jpg/500px-M_B_Patil.jpg",
    "Ramalinga Reddy": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Ramalinga_Reddy.jpg/500px-Ramalinga_Reddy.jpg",
    "K. J. George": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/K._J._George.jpg/500px-K._J._George.jpg",
    "Priyank Kharge": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Priyank_Kharge.jpg/500px-Priyank_Kharge.jpg",
    "Dinesh Gundu Rao": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Dinesh_Gundu_Rao.jpg/500px-Dinesh_Gundu_Rao.jpg",
    "Krishna Byre Gowda": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Krishna_Byre_Gowda.jpg/500px-Krishna_Byre_Gowda.jpg",
    "R. Ashoka": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/R._Ashoka.jpg/500px-R._Ashoka.jpg",
    "C. N. Ashwath Narayan": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Dr._C._N._Ashwath_Narayan.jpg/500px-Dr._C._N._Ashwath_Narayan.jpg",
    "S. Suresh Kumar": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/S._Suresh_Kumar.jpg/500px-S._Suresh_Kumar.jpg",
    "B. Y. Vijayendra": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/B._Y._Vijayendra.jpg/500px-B._Y._Vijayendra.jpg",

    # Punjab
    "Bhagwant Mann": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Bhagwant_Mann_in_2022.jpg/500px-Bhagwant_Mann_in_2022.jpg",
    "Aman Arora": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Aman_Arora.jpg/500px-Aman_Arora.jpg",
    "Harpal Singh Cheema": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Harpal_Singh_Cheema.jpg/500px-Harpal_Singh_Cheema.jpg",
    "Kuldeep Singh Dhaliwal": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Kuldeep_Singh_Dhaliwal.jpg/500px-Kuldeep_Singh_Dhaliwal.jpg",
    "Gurmeet Singh Meet Hayer": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Meet_Hayer.jpg/500px-Meet_Hayer.jpg",
    "Dr. Baljit Kaur": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Dr_Baljit_Kaur.jpg/500px-Dr_Baljit_Kaur.jpg",
    "Chetan Singh Jauramajra": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/Chetan_Singh_Jauramajra.jpg/500px-Chetan_Singh_Jauramajra.jpg",
    "Navjot Singh Sidhu": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Navjot_Singh_Sidhu.jpg/500px-Navjot_Singh_Sidhu.jpg",
    "Partap Singh Bajwa": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Partap_Singh_Bajwa.jpg/500px-Partap_Singh_Bajwa.jpg",
    "Sukhbir Singh Badal": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Sukhbir_Singh_Badal.jpg/500px-Sukhbir_Singh_Badal.jpg",
    "Bikram Singh Majithia": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Bikram_Singh_Majithia.jpg/500px-Bikram_Singh_Majithia.jpg",
    "Rana Gurjeet Singh": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Rana_Gurjeet_Singh.jpg/500px-Rana_Gurjeet_Singh.jpg"
}

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name.lower().strip())

def clean_politician_name(name):
    n = re.sub(r'^(adv\.?|dr\.?|prof\.?|ca\.?|col\.?|capt\.?|captain)\s+', '', name, flags=re.IGNORECASE).strip()
    n = re.sub(r'\s*\([^)]*\)', '', n).strip()
    return n

def download_image(url, dest_path):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return True
    try:
        res = requests.get(url, headers=HEADERS, timeout=8)
        if res.status_code == 200 and len(res.content) > 1000:
            with open(dest_path, 'wb') as f:
                f.write(res.content)
            return True
    except Exception:
        pass
    return False

def query_wiki_portrait(name, state_name):
    clean = clean_politician_name(name)
    
    # 1. Match in curated list
    for k, v in CURATED_PORTRAITS.items():
        if k.lower() in name.lower() or clean.lower() == k.lower():
            return v
            
    # 2. Try MediaWiki API queries
    queries = [clean, f"{clean} (politician)", f"{clean} MLA", f"{clean} {state_name}"]
    for q in queries:
        try:
            url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(q)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            res = requests.get(url, headers=HEADERS, timeout=5).json()
            for pid, pdata in res.get('query', {}).get('pages', {}).items():
                if pid != "-1" and 'thumbnail' in pdata:
                    src = pdata['thumbnail']['source']
                    if src and not src.endswith('.svg'):
                        return src
        except Exception:
            pass
            
    # 3. Search query
    try:
        s_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(clean + ' ' + state_name + ' politician')}&format=json"
        res = requests.get(s_url, headers=HEADERS, timeout=5).json()
        hits = res.get('query', {}).get('search', [])
        if hits:
            top_title = hits[0]['title']
            t_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(top_title)}&prop=pageimages&format=json&pithumbsize=500&redirects=1"
            t_res = requests.get(t_url, headers=HEADERS, timeout=5).json()
            for pid, pdata in t_res.get('query', {}).get('pages', {}).items():
                if pid != "-1" and 'thumbnail' in pdata:
                    src = pdata['thumbnail']['source']
                    if src and not src.endswith('.svg'):
                        return src
    except Exception:
        pass
        
    return None

def run_all_states_enrichment():
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        records = list(reader)
        
    states_to_process = ["Uttar Pradesh", "Karnataka", "Punjab"]
    
    results = {}
    manual_lists = {}
    
    for st in states_to_process:
        print(f"\n=======================================================")
        print(f"Auditing and Enriching Photos for: {st}")
        print(f"=======================================================")
        
        st_records = [r for r in records if r['state'] == st]
        found_count = 0
        manual_req = []
        
        for idx, cand in enumerate(st_records):
            name = cand['elected_person']
            c_name = cand['constituency_name']
            photo = cand['photo_source_url']
            
            clean_path = photo.replace("/my-leader/", "").lstrip("/")
            local_file = os.path.join(PUBLIC_DIR, clean_path)
            
            # Check if photo is already valid
            if photo and "placeholder-avatar" not in photo and os.path.exists(local_file) and os.path.getsize(local_file) > 1000:
                continue
                
            img_url = query_wiki_portrait(name, st)
            if img_url:
                filename = f"{sanitize_filename(st[:2])}_{sanitize_filename(name)}.jpg"
                dest = os.path.join(IMG_DIR, filename)
                if download_image(img_url, dest):
                    cand['photo_source_url'] = f"/my-leader/assets/candidates/{filename}"
                    print(f" [{idx+1}/{len(st_records)}] FOUND & LINKED: {name} -> {filename}")
                    found_count += 1
                    continue
                    
            cand['photo_source_url'] = "/my-leader/assets/placeholder-avatar.svg"
            manual_req.append(cand)
            time.sleep(0.15)
            
        results[st] = {
            "total": len(st_records),
            "recovered": found_count,
            "manual_required": len(manual_req)
        }
        manual_lists[st] = manual_req
        
    # Save back to CSV
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
        writer.writeheader()
        writer.writerows(records)
        
    # Output unified Markdown Report for all states
    report_file = os.path.join(BASE_DIR, "all_states_manual_photo_intervention.md")
    lines = [
        "# Candidate Photos Requiring Manual Upload (All States)\n",
        "This document lists all elected representatives across Maharashtra, Uttar Pradesh, Karnataka, and Punjab who do not have public domain portraits on online encyclopedias and require manual photo drops.\n",
        "---\n"
    ]
    
    for st in ["Maharashtra", "Uttar Pradesh", "Karnataka", "Punjab"]:
        st_manual = [r for r in records if r['state'] == st and ("placeholder-avatar" in r['photo_source_url'] or not os.path.exists(os.path.join(PUBLIC_DIR, r['photo_source_url'].replace('/my-leader/', '').lstrip('/'))))]
        lines.append(f"## {st} ({len(st_manual)} Candidates Needing Photos)\n")
        lines.append("| No | Code | Constituency | District | Elected Representative | Party | Status |")
        lines.append("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |")
        for i, c in enumerate(st_manual, 1):
            lines.append(f"| {i} | {c['constituency_code']} | {c['constituency_name']} | {c['district']} | **{c['elected_person']}** | {c['party']} | `Needs Manual Photo` |")
        lines.append("\n---\n")
        
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
        
    print(f"\n=======================================================")
    print(f"ENRICHMENT SUMMARY:")
    for st, res in results.items():
        print(f" - {st}: {res['recovered']} new portraits recovered | {res['manual_required']} candidates need manual photo")
    print(f"Unified Manual Checklist saved to: {report_file}")
    print(f"=======================================================\n")

if __name__ == "__main__":
    run_all_states_enrichment()
