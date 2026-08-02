import json
import os
import requests
import urllib.parse
from datetime import datetime

DATA_FILE = "src/data/realGovernanceData.json"
WIKI_API_URL = "https://en.wikipedia.org/w/api.php"

def get_latest_wiki_revisions(titles):
    """Batch fetch latest revision timestamps for a list of Wikipedia titles."""
    titles_str = "|".join(titles)
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "timestamp",
        "titles": titles_str,
        "format": "json"
    }
    
    headers = {"User-Agent": "JumlebaazVerifier/1.0"}
    try:
        resp = requests.get(WIKI_API_URL, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        
        results = {}
        pages = data.get("query", {}).get("pages", {})
        for page_id, page_info in pages.items():
            title = page_info.get("title")
            if "revisions" in page_info:
                results[title] = page_info["revisions"][0]["timestamp"]
        return results
    except Exception as e:
        print(f"Error fetching wiki API for batch: {e}")
        return {}

def verify_data():
    print("=== Jumlebaaz Data Verification Pipeline ===")
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Please run compile.py first.")
        return
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    candidates = data.get("candidates", [])
    print(f"Loaded {len(candidates)} candidates.")
    
    # 1. Verify Basic Data Integrity
    missing_logos = sum(1 for c in candidates if not c.get("partyLogoUrl"))
    missing_names = sum(1 for c in candidates if not c.get("name"))
    print(f"Integrity Check: {missing_logos} missing party logos, {missing_names} missing names.")
    
    # 2. Verify Freshness using Wikipedia API
    # We will check the 14th_Maharashtra_Legislative_Assembly page itself for updates!
    # Because checking 288 individual pages takes too long for a quick script, checking the main assembly page is a great proxy.
    
    main_assembly_page = "14th_Maharashtra_Legislative_Assembly"
    print(f"\nChecking freshness of master list ({main_assembly_page})...")
    revs = get_latest_wiki_revisions([main_assembly_page])
    
    if main_assembly_page.replace("_", " ") in revs:
        last_modified = revs[main_assembly_page.replace("_", " ")]
        print(f"Master List Last Modified on Wikipedia: {last_modified}")
        
        # We can store a metadata file locally to track when we last scraped
        meta_file = "scripts/pipeline/.last_verified"
        last_scraped = None
        if os.path.exists(meta_file):
            with open(meta_file, "r") as mf:
                last_scraped = mf.read().strip()
                
        if last_scraped:
            print(f"Our Data Last Scraped:     {last_scraped}")
            if last_modified > last_scraped:
                print("⚠️ WARNING: The Wikipedia master list has been updated since our last scrape! You should run `python scripts/pipeline/myneta_deep_scraper.py` again.")
            else:
                print("✅ Data is up to date with Wikipedia.")
        else:
            print("First time verification run. Saving current scrape timestamp.")
            with open(meta_file, "w") as mf:
                mf.write(datetime.utcnow().isoformat() + "Z")
                
    else:
        print("Failed to get Wikipedia timestamp.")

if __name__ == "__main__":
    verify_data()
