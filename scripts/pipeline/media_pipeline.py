import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import time
import os

DATA_FILE = "scripts/pipeline/raw_maharashtra_real.json"

def fetch_news(candidate_name):
    query = urllib.parse.quote(candidate_name + " Maharashtra MLA")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
    
    news = []
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # The structure is rss -> channel -> item
            items = root.findall('.//item')
            for i, item in enumerate(items[:5]): # Get top 5
                title = item.findtext('title')
                link = item.findtext('link')
                pubDate = item.findtext('pubDate')
                source = item.find('source').text if item.find('source') is not None else "News"
                
                # Google News titles are usually "Headline - Source". Let's clean it.
                if title and " - " in title:
                    title = title.rsplit(" - ", 1)[0]
                    
                news.append({
                    "id": f"news_{i+1}",
                    "title": title,
                    "source": source,
                    "date": pubDate,
                    "url": link,
                    "sentiment": "neutral" # Simple default
                })
    except Exception as e:
        print(f"Failed to fetch news for {candidate_name}: {e}")
        
    return news

def main():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found")
        return
        
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        candidates = json.load(f)
        
    print(f"Starting Media Pipeline for {len(candidates)} candidates...")
    
    # We will do this sequentially to avoid being IP banned by Google News
    for i, c in enumerate(candidates):
        print(f"[{i+1}/{len(candidates)}] Fetching news for {c['name']}...")
        news_items = fetch_news(c['name'])
        c['mediaSpotlight'] = news_items
        time.sleep(0.3)
        
        # Save incrementally every 10 candidates just in case
        if (i+1) % 10 == 0:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(candidates, f, indent=2, ensure_ascii=False)
                
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(candidates, f, indent=2, ensure_ascii=False)
        
    print("Media Pipeline Complete! Updated raw_maharashtra_real.json")

if __name__ == "__main__":
    main()
