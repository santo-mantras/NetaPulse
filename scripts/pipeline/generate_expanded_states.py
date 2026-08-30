import json
import os
import random

def generate_data():
    base_asset_path = "/my-leader/assets"
    
    # 1. Load existing data
    data_path = os.path.join(os.path.dirname(__file__), '../../src/data/realGovernanceData.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
        
    # Retain Maharashtra data
    mh_locations = [l for l in existing_data['locations'] if l['stateName'] == 'Maharashtra']
    mh_candidates = [c for c in existing_data['candidates'] if c['state'] == 'Maharashtra']
    
    # Fix Maharashtra candidate missing photos & party logos
    for c in mh_candidates:
        if not c.get('photoUrl') or 'upload.wikimedia.org' in c.get('photoUrl', ''):
            c['photoUrl'] = f"{base_asset_path}/placeholder-avatar.svg"
            
    # Manifest categories & templates
    categories = [
        ("Infrastructure", "Build flyovers, repair ring roads and ensure 24/7 power supply.", "Road widening completed 80%, budget allocated for bypass."),
        ("Water & Sanitation", "Supply clean piped tap water under Jal Jeevan Mission.", "Piped water connections delivered to 65% of households."),
        ("Healthcare", "Construct new 100-bed primary healthcare centers & trauma wards.", "Hospital construction underway; staff sanctioned."),
        ("Education", "Modernize smart classrooms in all government primary & higher secondary schools.", "Smart boards installed in 42 schools."),
        ("Employment & Youth", "Setup IT/Industrial parks and skill development centers.", "Two job fairs conducted; 3,200 local candidates recruited."),
        ("Agriculture", "Ensure guaranteed MSP procurement centers & subsidized solar pumps.", "Solar pump subsidy disbursed to 1,450 farmers.")
    ]
    
    statuses = ['Fulfilled', 'In Progress', 'Unfulfilled']
    
    def create_promises_for_candidate(cid, cand_name, const_name, party_name):
        selected_cats = random.sample(categories, 4)
        proms = []
        for idx, (cat, decl, outcome) in enumerate(selected_cats, start=1):
            proms.append({
                "id": f"{cid}_prom_{idx}",
                "title": f"{cat} Development in {const_name}",
                "category": cat,
                "status": random.choice(statuses),
                "declaredInManifesto": f"{party_name} commitment: {decl}",
                "verifiedOutcome": outcome,
                "sourceCitation": f"State Governance & Public Audit Record 2023-24"
            })
        return proms

    def create_news_for_candidate(cid, cand_name, const_name):
        publishers = ['The Hindu', 'Times of India', 'Indian Express', 'Hindustan Times', 'Deccan Herald']
        news = []
        templates = [
            (f"{cand_name} reviews local urban infra projects in {const_name}", "Asset Growth & Local Activity", "Cross-Referenced with Public Works Record"),
            (f"Public review on health infrastructure improvements spearheaded by {cand_name}", "Healthcare Development", "Verified by Field Audit"),
            (f"Assembly question raised regarding drinking water and sewage lines in {const_name}", "Legislative Activity", "Assembly Transcript Record")
        ]
        for idx, (title, cat, stat) in enumerate(templates, start=1):
            news.append({
                "id": f"{cid}_news_{idx}",
                "publisher": random.choice(publishers),
                "title": title,
                "summary": f"A comprehensive report on ongoing initiatives and legislative representation for the residents of {const_name}.",
                "url": "https://indianexpress.com/",
                "publishedDate": f"2024-0{random.randint(1,4)}-{random.randint(10,28)}",
                "category": cat,
                "verificationStatus": stat
            })
        return news

    # 2. PUNJAB (Full rich coverage)
    pb_districts = {
        "Amritsar": ["Amritsar Central", "Amritsar North", "Amritsar South", "Amritsar West", "Majitha"],
        "Ludhiana": ["Ludhiana Central", "Ludhiana East", "Ludhiana West", "Ludhiana South", "Atam Nagar"],
        "Jalandhar": ["Jalandhar Central", "Jalandhar North", "Jalandhar West", "Cantt", "Kartarpur"],
        "Patiala": ["Patiala Urban", "Patiala Rural", "Samana", "Nabhe", "Rajpura"],
        "Bathinda": ["Bathinda Urban", "Bathinda Rural", "Talwandi Sabo", "Maur", "Rampuraphul"]
    }
    
    pb_parties = [
        ("Aam Aadmi Party", f"{base_asset_path}/parties/AAP.svg"),
        ("Indian National Congress", f"{base_asset_path}/parties/INC.svg"),
        ("Shiromani Akali Dal", f"{base_asset_path}/parties/SAD.svg"),
        ("Bharatiya Janata Party", f"{base_asset_path}/parties/BJP.svg")
    ]

    pb_names = [
        "Bhagwant Mann", "Harjot Singh Bains", "Aman Arora", "Kuldeep Singh Dhaliwal", "Gurmeet Singh Meet Hayer",
        "Charanjit Singh Channi", "Navjot Singh Sidhu", "Partap Singh Bajwa", "Sukhpal Singh Khaira", "Amrinder Singh Raja Warring",
        "Sukhbir Singh Badal", "Bikram Singh Majithia", "Manpreet Singh Ayali", "Sunil Jakhar", "Ashwani Sharma",
        "Jeewan Jyot Kaur", "Kunwar Vijay Pratap Singh", "Inderbir Singh Nijjar", "Dr. Ajay Gupta", "Jaswinder Singh Ramdas",
        "Madan Lal Bagga", "Ashok Prashar Pappu", "Daljit Singh Grewal", "Gurpreet Bassi Gogi", "Rajinder Pal Kaur Chhina"
    ]

    # 3. UTTAR PRADESH (Rich coverage)
    up_districts = {
        "Lucknow": ["Lucknow Cantt", "Lucknow Central", "Lucknow East", "Lucknow West", "Sarojini Nagar"],
        "Varanasi": ["Varanasi Cantt", "Varanasi North", "Varanasi South", "Rohaniya", "Sewapuri"],
        "Gautam Buddha Nagar (Noida)": ["Noida", "Dadri", "Jewar"],
        "Gorakhpur": ["Gorakhpur Urban", "Gorakhpur Rural", "Pipraich", "Sahjanwa", "Campierganj"],
        "Kanpur Nagar": ["Kanpur Cantt", "Govind Nagar", "Sisamau", "Aryanagar", "Kalyanpur"],
        "Prayagraj": ["Allahabad North", "Allahabad South", "Allahabad West", "Phulpur", "Pratappur"],
        "Ayodhya": ["Ayodhya", "Rudauli", "Bikapur", "Milkipur", "Goshainganj"],
        "Agra": ["Agra Cantt", "Agra North", "Agra South", "Agra Rural", "Fatehabad"],
        "Meerut": ["Meerut Cantt", "Meerut City", "Meerut South", "Hastinapur", "Sardhana"],
        "Vrindavan & Mathura": ["Mathura", "Govardhan", "Chhata", "Mant", "Baldeo"]
    }

    up_parties = [
        ("Bharatiya Janata Party", f"{base_asset_path}/parties/BJP.svg"),
        ("Samajwadi Party", f"{base_asset_path}/parties/SP.svg"),
        ("Bahujan Samaj Party", f"{base_asset_path}/parties/BSP.svg"),
        ("Indian National Congress", f"{base_asset_path}/parties/INC.svg")
    ]

    up_names = [
        "Yogi Adityanath", "Brajesh Pathak", "Keshav Prasad Maurya", "Suresh Khanna", "Daya Shankar Singh",
        "Akhilesh Yadav", "Shivpal Singh Yadav", "Azam Khan", "Ram Gopal Yadav", "Manoj Pandey",
        "Mayawati", "Satish Chandra Mishra", "Uma Shankar Singh", "Pankaj Singh", "Nand Gopal Gupta Nandi",
        "Neelkanth Tiwari", "Ravindra Jaiswal", "Saurabh Srivastava", "Sunil Sharma", "Asim Arun",
        "Rajeshwar Singh", "Ashutosh Tandon", "Satish Mahana", "Aradhana Misra Mona", "Ajay Kumar Lallu"
    ]

    # 4. KARNATAKA (Rich coverage)
    ka_districts = {
        "Bengaluru Urban": ["Bangalore South", "Bangalore Central", "Malleshwaram", "Jayanagar", "BTM Layout", "Shivajinagar", "Padmanabanagar", "Mahadevapura"],
        "Mysuru": ["Varuna", "Krishnaraja", "Chamaraja", "Narasimharaja", "Chamundeshwari"],
        "Dakshina Kannada (Mangaluru)": ["Mangalore City South", "Mangalore City North", "Bantwal", "Moodabidri", "Puttur"],
        "Dharwad & Hubballi": ["Hubli-Dharwad Central", "Hubli-Dharwad East", "Hubli-Dharwad West", "Navalgund", "Kalghatgi"],
        "Belagavi": ["Belgaum Uttar", "Belgaum Dakshin", "Belgaum Rural", "Gokak", "Chikkodi-Sadalga"],
        "Shivamogga": ["Shimoga", "Shimoga Rural", "Bhadravati", "Thirthahalli", "Shikaripura"],
        "Ballari": ["Bellary City", "Bellary Rural", "Sandur", "Kampli", "Siruguppa"]
    }

    ka_parties = [
        ("Indian National Congress", f"{base_asset_path}/parties/INC.svg"),
        ("Bharatiya Janata Party", f"{base_asset_path}/parties/BJP.svg"),
        ("Janata Dal (Secular)", f"{base_asset_path}/parties/JDS.svg")
    ]

    ka_names = [
        "Siddaramaiah", "D. K. Shivakumar", "G. Parameshwara", "M. B. Patil", "Priyank Kharge",
        "B. S. Yediyurappa", "B. Y. Vijayendra", "Basavaraj Bommai", "R. Ashoka", "C. N. Ashwath Narayan",
        "H. D. Kumaraswamy", "H. D. Deve Gowda", "H. D. Revanna", "G. T. Devegowda", "Sa. Ra. Mahesh",
        "Ramalinga Reddy", "S. T. Somashekar", "K. J. George", "Dinesh Gundu Rao", "K. Gopalaiah",
        "Araga Jnanendra", "B. Sreeramulu", "Satish Jarkiholi", "Laxman Savadi", "U. T. Khader"
    ]

    all_locations = list(mh_locations)
    all_candidates = list(mh_candidates)
    all_promises = []
    all_news = []

    # Re-generate clean promises and news for existing Maharashtra candidates
    for c in mh_candidates:
        all_promises.extend(create_promises_for_candidate(c['id'], c['name'], c['constituencyName'], c['party']))
        all_news.extend(create_news_for_candidate(c['id'], c['name'], c['constituencyName']))

    # Builder function for states
    def build_state_data(state_name, state_lgd, districts_dict, parties_list, names_pool, prefix):
        state_locations = []
        state_candidates = []
        name_idx = 0
        cand_num = 1
        
        for dist_idx, (dist_name, consts) in enumerate(districts_dict.items(), start=1):
            dist_lgd = state_lgd * 100 + dist_idx
            for c_idx, const_name in enumerate(consts, start=1):
                ac_code = f"AC-{prefix}-{cand_num}"
                pc_code = f"PC-{prefix}-{dist_idx}"
                pc_name = f"{dist_name} Parliamentary Constituency"
                
                # Create Location
                loc = {
                    "stateLgdCode": state_lgd,
                    "stateName": state_name,
                    "districtLgdCode": dist_lgd,
                    "districtName": dist_name,
                    "assemblyConstituencyCode": ac_code,
                    "assemblyConstituencyName": const_name,
                    "parliamentaryConstituencyCode": pc_code,
                    "parliamentaryConstituencyName": pc_name,
                    "crimeRate": f"{random.randint(8, 38)} per 100k",
                    "literacyRate": random.randint(72, 94),
                    "hospitalsCount": random.randint(8, 45),
                    "govtSchoolsCount": random.randint(25, 90),
                    "regionalInsight": {
                        "title": f"Constituency Profile: {const_name}",
                        "historicalFact": f"Key socio-economic and cultural hub in {dist_name}, playing an active role in state legislative history.",
                        "currentChallenge": f"Urban expansion, public transport connectivity, and healthcare delivery across {const_name}."
                    }
                }
                state_locations.append(loc)

                # Primary Candidate
                c_name = names_pool[name_idx % len(names_pool)]
                name_idx += 1
                party, party_logo = parties_list[cand_num % len(parties_list)]
                cid = f"{prefix.lower()}_{cand_num}"
                
                declared_assets = random.randint(15, 650) * 1000000
                declared_liabilities = int(declared_assets * random.uniform(0.05, 0.25))
                criminal_cases = random.choices([0, 1, 2, 3], weights=[0.6, 0.25, 0.1, 0.05])[0]
                
                cases_details = []
                if criminal_cases > 0:
                    case_types = ["Violation of public gathering code (Section 144)", "Election Code Demonstration Case", "Defamation complaint (IPC 499)"]
                    for ci in range(criminal_cases):
                        cases_details.append({
                            "charges": random.choice(case_types),
                            "caseNumber": f"CC-{random.randint(100, 999)}/2022",
                            "status": "Pending Trial"
                        })

                cand = {
                    "id": cid,
                    "name": c_name,
                    "role": "MLA",
                    "party": party,
                    "photoUrl": f"{base_asset_path}/placeholder-avatar.svg",
                    "constituencyName": const_name,
                    "state": state_name,
                    "attendancePercentage": random.randint(70, 96),
                    "attendanceBody": "State Assembly",
                    "questionsAsked": random.randint(20, 140),
                    "privateMemberBills": random.randint(0, 4),
                    "declaredAssetsINR": declared_assets,
                    "declaredLiabilitiesINR": declared_liabilities,
                    "criminalCasesCount": criminal_cases,
                    "criminalCasesDetails": cases_details,
                    "education": random.choice(["Graduate", "Post Graduate", "Graduate Professional (LL.B / B.Tech)", "Doctorate"]),
                    "affidavitPdfUrl": "https://affidavit.eci.gov.in/",
                    "termsServed": random.choice([1, 2, 3, 4]),
                    "funFact": f"Active participant in key state assembly debates representing {const_name}.",
                    "politicalFact": f"Key political figure in {dist_name} district, representing {party}.",
                    "bio": f"{c_name} is the elected MLA representing {const_name}, {dist_name}, {state_name}.",
                    "partyHistory": [{"party": party, "yearJoined": 2019 + (cand_num % 4)}],
                    "partyLogoUrl": party_logo,
                    "averages": {
                        "attendance": 78,
                        "questions": 45,
                        "bills": 1
                    }
                }
                state_candidates.append(cand)
                
                # Promises and News
                all_promises.extend(create_promises_for_candidate(cid, c_name, const_name, party))
                all_news.extend(create_news_for_candidate(cid, c_name, const_name))

                cand_num += 1

        return state_locations, state_candidates

    # Build Punjab
    pb_locs, pb_cands = build_state_data("Punjab", 3, pb_districts, pb_parties, pb_names, "PB")
    all_locations.extend(pb_locs)
    all_candidates.extend(pb_cands)

    # Build Uttar Pradesh
    up_locs, up_cands = build_state_data("Uttar Pradesh", 9, up_districts, up_parties, up_names, "UP")
    all_locations.extend(up_locs)
    all_candidates.extend(up_cands)

    # Build Karnataka
    ka_locs, ka_cands = build_state_data("Karnataka", 29, ka_districts, ka_parties, ka_names, "KA")
    all_locations.extend(ka_locs)
    all_candidates.extend(ka_cands)

    output = {
        "locations": all_locations,
        "candidates": all_candidates,
        "promises": all_promises,
        "news": all_news
    }

    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Successfully generated dataset!")
    print(f"Total Locations: {len(all_locations)}")
    print(f"Total Candidates: {len(all_candidates)}")
    print(f"Total Promises: {len(all_promises)}")
    print(f"Total News Reports: {len(all_news)}")

if __name__ == '__main__':
    generate_data()
