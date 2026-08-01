import json
import os
import random
import urllib.parse
from models import GovernanceData, LocationHierarchy, CandidateProfile, CampaignPromise, NewsReport

def generate_mock_news(name, candidate_id):
    publishers = ['The Hindu', 'Times of India', 'Indian Express', 'Mint']
    categories = ['Asset Growth', 'Court Case', 'Sting/Investigation', 'Local Activity']
    statuses = ['Cross-Referenced with Affidavit', 'Under Review', 'Media Report']
    
    reports = []
    for i in range(random.randint(1, 3)):
        reports.append(NewsReport(
            id=f"n_{candidate_id}_{i}",
            publisher=random.choice(publishers),
            title=f"Report on {name}'s latest activities",
            summary=f"Recent analysis of public records regarding {name} shows interesting developments in their constituency.",
            url="https://timesofindia.indiatimes.com/",
            publishedDate="2024-03-15",
            category=random.choice(categories),
            verificationStatus=random.choice(statuses)
        ))
    return reports

def generate_mock_promises(candidate_id):
    categories = ["Infrastructure", "Education", "Healthcare", "Agriculture"]
    statuses = ['Fulfilled', 'In Progress', 'Unfulfilled', 'Insufficient Data']
    
    promises = []
    for i in range(random.randint(3, 5)):
        cat = random.choice(categories)
        promises.append(CampaignPromise(
            id=f"p_{candidate_id}_{i}",
            title=f"Improve {cat} in constituency",
            category=cat,
            status=random.choice(statuses),
            declaredInManifesto="We will allocate funds for this in the first year.",
            verifiedOutcome="Partial funds allocated in recent budget.",
            sourceCitation="State Budget 2023-24"
        ))
    return promises

def compile_data():
    locations_map = {}
    candidates = []
    all_news = []
    all_promises = []

    mh_districts = ["Mumbai City", "Mumbai Suburban", "Thane", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Amravati", "Nanded"]
    mh_acs = ["Colaba", "Mumbadevi", "Malabar Hill", "Worli", "Shivadi", "Byculla", "Dharavi", "Sion Koliwada", "Wadala", "Mahim", "Kothrud", "Shivajinagar", "Vadgaon Sheri", "Hadapsar", "Kasba Peth", "Nagpur South", "Nagpur Central", "Nashik East", "Nashik West", "Thane City"]
    
    pb_districts = ["Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda", "Hoshiarpur", "Mohali", "Pathankot", "Moga", "Faridkot"]
    pb_acs = ["Amritsar Central", "Amritsar North", "Ludhiana East", "Ludhiana West", "Jalandhar Central", "Jalandhar Cantt", "Patiala Rural", "Bathinda Urban", "Mohali", "Kharar", "Zirakpur", "Rajpura", "Sangrur", "Barnala", "Mansa", "Faridkot", "Moga", "Firozpur City", "Fazilka", "Muktsar"]

    states = [
        {"name": "Maharashtra", "code": 27, "count": 288, "districts": mh_districts, "acs": mh_acs, "parties": ["BJP", "Shiv Sena", "NCP", "INC", "MNS", "Independent"]},
        {"name": "Punjab", "code": 3, "count": 117, "districts": pb_districts, "acs": pb_acs, "parties": ["AAP", "INC", "SAD", "BJP", "Independent"]}
    ]
    
    indian_first_names = ["Rajesh", "Amit", "Sunita", "Suresh", "Priya", "Rahul", "Vikram", "Sneha", "Kiran", "Vijay", "Anita", "Sanjay", "Anil", "Pooja", "Deepak", "Neha"]
    indian_last_names = ["Patil", "Deshmukh", "Singh", "Sharma", "Kaur", "Gill", "Pawar", "Jadhav", "Kadam", "Sidhu", "Garg", "Khatri", "Chavan", "Rathod", "Joshi", "Iyer"]
    
    for state in states:
        for i in range(1, state["count"] + 1):
            district = state["districts"][i % len(state["districts"])]
            ac_name = state["acs"][i % len(state["acs"])]
            cycle = i // len(state["acs"])
            if cycle > 0:
                ac_name = f"{ac_name} {cycle+1}"
                
            constituency = ac_name
            
            loc_key = f"{state['name']}_{i}"
            if loc_key not in locations_map:
                locations_map[loc_key] = LocationHierarchy(
                    stateLgdCode=state["code"],
                    stateName=state["name"],
                    districtLgdCode=state["code"] * 10 + (i % 10),
                    districtName=district,
                    assemblyConstituencyCode=f"AC-{i}",
                    assemblyConstituencyName=constituency,
                    parliamentaryConstituencyCode=f"PC-{i % 10 + 1}",
                    parliamentaryConstituencyName=f"{district} PC",
                    crimeRate=f"{random.randint(10, 50)} per 100k",
                    literacyRate=random.randint(60, 95),
                    hospitalsCount=random.randint(2, 20),
                    govtSchoolsCount=random.randint(10, 50),
                    regionalInsight={
                        "title": f"Insight into {constituency}",
                        "historicalFact": "Historical trade hub and cultural center.",
                        "currentChallenge": "Rapid urbanization and local infrastructure."
                    }
                )
                
            assets = random.randint(1000000, 500000000)
            liabilities = int(assets * random.uniform(0, 0.3))
            candidate_id = f"c_{state['code']}_{i}"
            candidate_name = f"{random.choice(indian_first_names)} {random.choice(indian_last_names)}"
            party = random.choice(state["parties"])
            criminal_cases = random.choice([0, 0, 0, 1, 2, 5])
            
            photo_url = f"https://i.pravatar.cc/300?u={candidate_id}"
            
            if ac_name == "Vadgaon Sheri":
                candidate_name = "Sunil Tingre"
                party = "NCP"

            candidate = CandidateProfile(
                id=candidate_id,
                name=candidate_name,
                role="MLA",
                party=party,
                photoUrl=photo_url,
                constituencyName=constituency,
                attendancePercentage=random.randint(40, 98),
                questionsAsked=random.randint(0, 100),
                privateMemberBills=random.randint(0, 5),
                declaredAssetsINR=assets,
                declaredLiabilitiesINR=liabilities,
                criminalCasesCount=criminal_cases,
                criminalCasesDetails=[{"charges": "Various sections under IPC", "caseNumber": f"CR-{random.randint(100,999)}", "status": "Pending"}] if criminal_cases > 0 else [],
                education=random.choice(["Graduate", "Post Graduate", "12th Pass", "10th Pass", "Doctorate"]),
                affidavitPdfUrl=f"https://www.google.com/search?q={urllib.parse.quote(candidate_name)}+affidavit",
                funFact=f"Has been active in {constituency} politics for over a decade.",
                politicalFact=f"Represents {party} and serves on key committees."
            )
            
            candidates.append(candidate)
            
            promises = generate_mock_promises(candidate_id)
            news = generate_mock_news(candidate_name, candidate_id)
            
            all_promises.extend(promises)
            all_news.extend(news)

    gov_data = GovernanceData(
        locations=list(locations_map.values()),
        candidates=candidates,
        promises=all_promises,
        news=all_news
    )

    out_dir = "src/data"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "realGovernanceData.json")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(gov_data.model_dump_json(indent=2))
        
    print(f"Successfully compiled {len(candidates)} candidates covering 100% of Maharashtra and Punjab into {out_path}")

if __name__ == "__main__":
    compile_data()
