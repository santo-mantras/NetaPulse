import csv
import re
import os

CSV_PATH = "scripts/pipeline/constituency_master.csv"

# Definite female first names and full names in Indian politics
KNOWN_FEMALE_LEADERS = {
    # Prominent National & State Leaders
    "rekha gupta", "atishi", "atishi marlena", "mamata banerjee", "diya kumari", "sunetra pawar",
    "bansuri swaraj", "nirmala sitharaman", "k. k. shailaja", "k.k. shailaja", "shailaja teacher",
    "dimple yadav", "hema malini", "mahua moitra", "smriti irani", "anupriya patel", "supriya sule",
    "praniti shinde", "yashomati thakur", "varsha gaikwad", "sulabha khodke", "manda mhatre",
    "devyani pharande", "seema bhele", "shweta mahale", "monica rajale", "saroj ahire",
    "lata sonawane", "yamini jadhav", "manisha chaudhari", "vidya thakur", "namita mundada",
    "aditi tatkare", "chhaya varma", "renu jogi", "dr. lakshmi hebbalkar", "lakshmi hebbalkar",
    "roopa shashi", "sowmya reddy", "anita kumaraswamy", "shashikala jolle", "k. poornima",
    "kanimozhi karunanidhi", "thamizhachi thangapandian", "geetha jeevan", "kayalvizhi selvaraj",
    "n. kayalvizhi selvaraj", "p. geetha jeevan", "s. vijayadharani", "vanathi srinivasan",
    "chandrima bhattacharya", "dr. shashi panja", "shashi panja", "birbaha hansda", "lovely maitra",
    "agnimitra paul", "shikha chatterjee", "ratna de nag", "sabina yeasmin", "debasree chaudhuri",
    "anita bhadel", "kalpana devi", "siddhi kumari", "shobharani kushwah", "vasundhara raje",
    "dr. ragini sonkar", "aditi singh", "gulabo devi", "pinki singh", "aruna kori", "ketki singh",
    "neelam sonkar", "anjula singh mahaur", "archana pandey", "anupama jaiswal", "swati singh",
    "rani pakshalika singh", "manju tyagi", "pramila pandey", "sushma swaraj", "sheila dikshit",
    "kamla beniwal", "anandiben patel", "nimaben acharya", "bhanuben babariya", "sangita patil",
    "darshana jardosh", "poornima rathod", "malti maheshwari", "geetaba jadeja", "reena kashyap"
}

# Female name markers (first names, middle tokens, suffixes)
FEMALE_NAME_TOKENS = {
    "rekha", "atishi", "mamata", "diya", "sunetra", "bansuri", "nirmala", "dimple", "hema", "mahua",
    "supriya", "praniti", "yashomati", "varsha", "sulabha", "manda", "devyani", "shweta", "monica",
    "saroj", "lata", "yamini", "manisha", "vidya", "namita", "aditi", "chhaya", "renu", "lakshmi",
    "laxmi", "roopa", "sowmya", "anita", "anitha", "shashikala", "poornima", "kanimozhi", "thamizhachi",
    "geetha", "geeta", "kayalvizhi", "vijayadharani", "vanathi", "chandrima", "shashi", "birbaha",
    "agnimitra", "shikha", "sabina", "siddhi", "shobharani", "vasundhara", "ragini", "gulabo", "pinki",
    "pinky", "ketki", "neelam", "anjula", "archana", "anupama", "swati", "pakshalika", "manju", "pramila",
    "anandi", "nimaben", "bhanuben", "sangita", "sangeeta", "darshana", "pooja", "puja", "ritu", "neha",
    "priyanka", "sonia", "sonya", "pratibha", "pushpa", "savita", "deepa", "dipa", "seema", "sima",
    "shanti", "kamala", "kamla", "vimla", "vimala", "sushma", "asha", "radha", "anjali", "meenakshi",
    "sudha", "poonam", "shakuntala", "kamlesh", "krishna", "rajni", "rajani", "maya", "sumitra",
    "tara", "lalita", "lalitha", "parvati", "vidyavati", "chitra", "aarti", "arti", "alka", "bhavna",
    "bhavana", "rashmi", "shilpa", "snehal", "jaya", "jayashree", "jayshree", "meena", "kavita", "sarita",
    "mamta", "usha", "sunita", "uma", "renuka", "shobha", "radhika", "preethi", "priti", "sujatha",
    "sujata", "rupa", "kiran", "babita", "sarla", "sarala", "sheela", "shila", "kanta", "santosh",
    "indira", "sonal", "payal", "komal", "sweta", "monika", "anuradha", "madhuri", "madhu", "shubha",
    "kalpana", "sharda", "sharada", "leela", "lila", "kusum", "kamlesh", "basanti", "ganga", "jamuna",
    "menaka", "menoka", "shampa", "rupal", "rupali", "shital", "sheetal", "shilpi", "tanuja", "rashmika",
    "bharti", "bharati", "ambika", "daksha", "dharshini", "dhanalakshmi", "meenakshi", "saraswati",
    "padma", "padmaja", "parvathi", "mallika", "manjula", "savithri", "savitri", "suguna", "selvi",
    "kalavathi", "kalavanti", "hemlata", "hemalatha", "snehlata", "prem", "premlata", "omwati",
    "bhagwati", "ramwati", "durgawati", "chandrawati", "vidyawati", "leelavati", "shanti", "kanti",
    "kaur", # In Sikh/Punjabi naming, Kaur is female
    "begum", "khatoon", "bibi", "bano", "fatima", "zainab", "ayesha", "naseem", "parveen", "shabana",
    "razia", "asima", "mumtaz", "rehana", "yasmin", "shahnaz", "firoza", "tahira", "jahanara"
}

MALE_DISAMBIGUATION_NAMES = {
    "santosh bangar", "santosh danve", "santosh lad", "santosh gangwar", "santosh pandey",
    "santosh singh", "santosh verma", "santosh kumar", "krishna khopde", "krishna pal",
    "krishnapal gurjar", "krishna murari", "krishna kumar", "krishna kishore",
    "laxmi narayan chaudhary", "laxminarayan", "kiran lahamate", "dr. kiran lahamate",
    "radha mohan singh", "radhamohan", "prem singh", "prem kumar", "prem rawat",
    "kanti lal", "kantilal", "shanti lal", "shantilal", "kailash choudhary", "madhu bangarappa"
}

FEMALE_PREFIXES = ["smt", "smt.", "shrimati", "kumari", "km.", "km", "dr. (mrs.)", "mrs.", "mrs", "ms.", "ms"]

def determine_gender(name: str) -> str:
    cleaned = re.sub(r'[^\w\s\.]', ' ', name.lower()).strip()
    words = cleaned.split()
    
    if not words:
        return 'Male'
        
    full_name_clean = " ".join([w for w in words if w not in ['adv.', 'adv', 'dr.', 'dr', 'shri', 'mr.', 'mr']])

    # Check male disambiguation first
    for male_name in MALE_DISAMBIGUATION_NAMES:
        if male_name in full_name_clean:
            return 'Male'

    # Check known full names or aliases
    for known in KNOWN_FEMALE_LEADERS:
        if known in full_name_clean or full_name_clean == known:
            return 'Female'
            
    # Check prefix
    first_word = words[0]
    if first_word in FEMALE_PREFIXES:
        return 'Female'
    if len(words) > 1 and f"{words[0]} {words[1]}" in FEMALE_PREFIXES:
        return 'Female'
        
    # Check tokens in name
    for w in words:
        w_clean = re.sub(r'\.', '', w)
        if w_clean in FEMALE_NAME_TOKENS:
            return 'Female'
        if w_clean == "devi":
            return 'Female'
        if w_clean.endswith("ben") and len(w_clean) > 4: # Gujarati female naming (e.g. Anandiben, Bhanuben)
            return 'Female'
        if w_clean.endswith("bai") and len(w_clean) > 4: # Marathi/Rajasthani female naming
            return 'Female'
        if w_clean.endswith("vati") and len(w_clean) > 5:
            return 'Female'
        if w_clean.endswith("wati") and len(w_clean) > 5:
            return 'Female'
        if w_clean.endswith("amman") or w_clean.endswith("ammal"): # Tamil female naming
            return 'Female'

    return 'Male'

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found!")
        return

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        rows = list(reader)

    if "gender" not in fieldnames:
        # Place gender right after role or elected_person
        idx = fieldnames.index("elected_person") + 1 if "elected_person" in fieldnames else 5
        fieldnames.insert(idx, "gender")

    female_count = 0
    male_count = 0
    female_leaders = []

    for r in rows:
        name = r.get("elected_person", "")
        calculated = determine_gender(name)
        r["gender"] = calculated
        if calculated == "Female":
            female_count += 1
            female_leaders.append((r.get("state", ""), r.get("constituency_name", ""), name))
        else:
            male_count += 1

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Successfully processed {len(rows)} candidates:")
    print(f"  Female representatives identified: {female_count} ({round(female_count/len(rows)*100, 2)}%)")
    print(f"  Male representatives identified: {male_count} ({round(male_count/len(rows)*100, 2)}%)")
    print("\nSample Female Leaders Identified:")
    for st, const, nm in female_leaders[:25]:
        print(f"  - [{st}] {const}: {nm}")

if __name__ == "__main__":
    main()
