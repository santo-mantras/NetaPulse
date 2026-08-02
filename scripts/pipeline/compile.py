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

def get_party_logo(party_name):
    # Map common variations
    mapping = {
        "Bharatiya Janata Party": "BJP",
        "BJP": "BJP",
        "Indian National Congress": "INC",
        "INC": "INC",
        "Nationalist Congress Party": "NCP",
        "NCP": "NCP",
        "Shiv Sena": "Shiv Sena",
        "SHS": "Shiv Sena",
        "Aam Aadmi Party": "AAP",
        "AAP": "AAP",
        "Maharashtra Navnirman Sena": "MNS",
        "MNS": "MNS",
        "Shiromani Akali Dal": "SAD",
        "SAD": "SAD"
    }
    key = mapping.get(party_name, "Independent")
    return f"/jumlabaaz/assets/parties/{key}.svg"

def compile_data():
    locations_map = {}
    candidates = []
    all_news = []
    all_promises = []

    # 1. Load Real Maharashtra Data
    mh_real_path = "scripts/pipeline/raw_maharashtra_real.json"
    if os.path.exists(mh_real_path):
        with open(mh_real_path, "r", encoding="utf-8") as f:
            mh_data = json.load(f)
            
        district_counts = {}
        for raw_c in mh_data:
            dist = raw_c.get("district", "Unknown")
            const = raw_c.get("constituency", "Unknown")
            if dist not in district_counts: district_counts[dist] = 0
            district_counts[dist] += 1
            
            loc_key = f"Maharashtra_{dist}_{const}"
            if loc_key not in locations_map:
                locations_map[loc_key] = LocationHierarchy(
                    stateLgdCode=27,
                    stateName="Maharashtra",
                    districtLgdCode=2700 + len(district_counts),
                    districtName=dist,
                    assemblyConstituencyCode=f"AC-{len(locations_map)+1}",
                    assemblyConstituencyName=const,
                    parliamentaryConstituencyCode=f"PC-MH",
                    parliamentaryConstituencyName=f"{dist} PC",
                    crimeRate=f"{random.randint(10, 50)} per 100k",
                    literacyRate=random.randint(60, 95),
                    hospitalsCount=random.randint(2, 20),
                    govtSchoolsCount=random.randint(10, 50),
                    regionalInsight={
                        "title": f"Insight into {const}",
                        "historicalFact": "Historical trade hub and cultural center.",
                        "currentChallenge": "Rapid urbanization and local infrastructure."
                    }
                )
            
            c_id = f"mh_{raw_c['id']}"
            name = raw_c['name']
            party = raw_c['party']
            
            # 30% chance of having switched parties (mocked for now, just to show UI)
            party_history = [{"party": party, "yearJoined": 2019}]
            if random.random() < 0.3:
                previous_party = random.choice(["BJP", "INC", "NCP", "Shiv Sena"])
                if previous_party != party:
                    party_history = [
                        {"party": previous_party, "yearJoined": 2014, "yearLeft": 2019},
                        {"party": party, "yearJoined": 2019}
                    ]

            photo_url = raw_c.get("photoLocalPath")
            if photo_url and photo_url.startswith("/assets"):
                photo_url = "/jumlabaaz" + photo_url
            
            role = "MLA"
            name_lower = name.lower()
            if "fadnavis" in name_lower:
                role = "Chief Minister"
            elif "eknath shinde" in name_lower or "ajit pawar" in name_lower:
                role = "Deputy Chief Minister"

            candidates.append(CandidateProfile(
                id=c_id,
                name=name,
                role=role,
                party=party,
                photoUrl=photo_url or "",
                constituencyName=const,
                state="Maharashtra",
                attendancePercentage=random.randint(40, 98),
                attendanceBody="State Assembly",
                averages={"attendance": 75, "questions": 30, "bills": 1},
                termsServed=random.randint(1, 4),
                questionsAsked=random.randint(0, 100),
                privateMemberBills=random.randint(0, 5),
                declaredAssetsINR=random.randint(1000000, 500000000),
                declaredLiabilitiesINR=random.randint(0, 10000000),
                criminalCasesCount=raw_c.get("criminalCasesCount", 0),
                criminalCasesDetails=[],
                education=raw_c.get("education", "Graduate"),
                affidavitPdfUrl=raw_c.get("affidavitUrl", ""),
                funFact=f"Has been active in {const} politics.",
                politicalFact=f"Represents {party} and serves on key committees.",
                bio=f"{name} is an Indian politician representing {const}. Elected in 2019.",
                partyLogoUrl=get_party_logo(party),
                partyHistory=party_history
            ))
            
            # Use real promises and media if available
            c_promises = raw_c.get("promisesTracked", [])
            c_media = raw_c.get("mediaSpotlight", [])
            
            for p in c_promises:
                all_promises.append(CampaignPromise(
                    id=f"{c_id}_{p['id']}",
                    title=p['title'],
                    category="Manifesto",
                    status=p['status'],
                    declaredInManifesto=p['description'],
                    verifiedOutcome="Party level tracking",
                    sourceCitation="Party Manifesto"
                ))
            
            for m in c_media:
                all_news.append(NewsReport(
                    id=f"{c_id}_{m['id']}",
                    publisher=m['source'],
                    title=m['title'],
                    summary="",
                    url=m['url'],
                    publishedDate=m['date'],
                    category="News",
                    verificationStatus="Media Report"
                ))

    # 2. Mock Punjab Data (to keep the app functioning for other states)
    pb_districts = ["Amritsar", "Ludhiana", "Jalandhar", "Patiala", "Bathinda"]
    pb_acs = ["Amritsar Central", "Amritsar North", "Ludhiana East", "Ludhiana West", "Jalandhar Central"]
    
    for i, ac in enumerate(pb_acs):
        dist = pb_districts[i % len(pb_districts)]
        loc_key = f"Punjab_{dist}_{ac}"
        locations_map[loc_key] = LocationHierarchy(
            stateLgdCode=3,
            stateName="Punjab",
            districtLgdCode=300 + i,
            districtName=dist,
            assemblyConstituencyCode=f"AC-PB-{i}",
            assemblyConstituencyName=ac,
            parliamentaryConstituencyCode=f"PC-PB",
            parliamentaryConstituencyName=f"{dist} PC",
            crimeRate="20 per 100k",
            literacyRate=75,
            hospitalsCount=5,
            govtSchoolsCount=15,
            regionalInsight={"title": "Punjab", "historicalFact": "None", "currentChallenge": "None"}
        )
        
        c_id = f"pb_{i}"
        name = f"Mock Punjab MLA {i}"
        party = random.choice(["AAP", "INC", "SAD"])
        candidates.append(CandidateProfile(
            id=c_id,
            name=name,
            role="MLA",
            party=party,
            photoUrl="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png",
            constituencyName=ac,
            state="Punjab",
            attendancePercentage=80,
            attendanceBody="State Assembly",
            averages={"attendance": 75, "questions": 30, "bills": 1},
            termsServed=1,
            questionsAsked=10,
            privateMemberBills=1,
            declaredAssetsINR=10000000,
            declaredLiabilitiesINR=0,
            criminalCasesCount=0,
            criminalCasesDetails=[],
            education="Graduate",
            affidavitPdfUrl="",
            funFact="Mock",
            politicalFact="Mock",
            bio="Mock data for Punjab.",
            partyLogoUrl=get_party_logo(party),
            partyHistory=[{"party": party, "yearJoined": 2022}]
        ))
        all_promises.extend(generate_mock_promises(c_id))
        all_news.extend(generate_mock_news(name, c_id))

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
        
    print(f"Successfully compiled {len(candidates)} candidates into {out_path}")

if __name__ == "__main__":
    compile_data()
