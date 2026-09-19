"""
NetaPulse State Profiles Catalog
Maintains verified state governance profiles including Chief Ministers, Deputy Chief Ministers,
Macroeconomic Indicators (GSDP, Per Capita), Fiscal Health, Social Progress Index, and Historical Legacies.
Enables automated periodic updates via GitHub Actions workflow.
"""

STATE_PROFILES = {
    "Maharashtra": {
        "chiefMinister": { "name": "Devendra Fadnavis", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/devendra_fadnavis.jpg" },
        "deputyChiefMinisters": [
            { "name": "Eknath Shinde", "party": "Shiv Sena" },
            { "name": "Sunetra Pawar", "party": "NCP" }
        ],
        "gsdpINR": "₹42.67 Lakh Cr",
        "perCapitaIncomeINR": "₹2,52,389",
        "fiscalHealth": "2.8% GSDP (FRBM Compliant)",
        "socialProgressIndex": "56.40 (Tier 3 - Upper Middle)",
        "historicalFact": "Birthplace of the Maratha Empire under Chhatrapati Shivaji Maharaj and the pioneer of India's cooperative banking and financial corridors.",
        "totalAssembly": 288,
        "totalLokSabha": 48,
        "totalDistricts": 35,
        "majorityMark": 145,
        "currentRuler": "Mahayuti Alliance",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Nationalist Congress Party": "#3b82f6",
            "Shiv Sena": "#eab308",
            "Indian National Congress": "#06b6d4",
            "Shiv Sena (Uddhav Balasaheb Thackeray)": "#ec4899",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 105, "pct": 36.5 },
            { "party": "Shiv Sena", "seats": 56, "pct": 19.4 },
            { "party": "Nationalist Congress Party", "seats": 54, "pct": 18.8 },
            { "party": "Indian National Congress", "seats": 44, "pct": 15.3 },
            { "party": "Shiv Sena (UBT) & Others", "seats": 29, "pct": 10.0 }
        ]
    },
    "Bihar": {
        "chiefMinister": { "name": "Samrat Choudhary", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg", "photoUrl": "/assets/candidates/samrat_choudhary.jpg" },
        "deputyChiefMinisters": [
            { "name": "Vijay Kumar Chaudhary", "party": "JD(U)" },
            { "name": "Bijendra Prasad Yadav", "party": "JD(U)" }
        ],
        "gsdpINR": "₹8.58 Lakh Cr",
        "perCapitaIncomeINR": "₹59,637",
        "fiscalHealth": "2.9% GSDP (Under Control)",
        "socialProgressIndex": "44.47 (Tier 6 - Lowest Tier)",
        "historicalFact": "Birthplace of Buddhism and Jainism, seat of imperial Pataliputra, and home to ancient Nalanda, the world's premier residential university.",
        "totalAssembly": 243,
        "totalLokSabha": 40,
        "totalDistricts": 38,
        "majorityMark": 122,
        "currentRuler": "National Democratic Alliance (NDA)",
        "partyColors": {
            "Rashtriya Janata Dal": "#16a34a",
            "Bharatiya Janata Party": "#f97316",
            "Janata Dal (United)": "#10b981",
            "Indian National Congress": "#06b6d4",
            "Communist Party of India (Marxist-Leninist) Liberation": "#ef4444",
            "All India Majlis-e-Ittehadul Muslimeen": "#047857",
            "Hindustani Awam Morcha (Secular)": "#eab308",
            "Vikassheel Insaan Party": "#3b82f6",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Rashtriya Janata Dal", "seats": 75, "pct": 30.9 },
            { "party": "Bharatiya Janata Party", "seats": 74, "pct": 30.5 },
            { "party": "Janata Dal (United)", "seats": 43, "pct": 17.7 },
            { "party": "Indian National Congress", "seats": 19, "pct": 7.8 },
            { "party": "Communist Party of India (Marxist-Leninist) Liberation", "seats": 12, "pct": 4.9 },
            { "party": "All India Majlis-e-Ittehadul Muslimeen", "seats": 5, "pct": 2.1 },
            { "party": "Hindustani Awam Morcha (Secular)", "seats": 4, "pct": 1.6 },
            { "party": "Vikassheel Insaan Party", "seats": 4, "pct": 1.6 },
            { "party": "Others / Independents", "seats": 7, "pct": 2.9 }
        ]
    },
    "West Bengal": {
        "chiefMinister": { "name": "Suvendu Adhikari", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/suvendu_adhikari.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹18.84 Lakh Cr",
        "perCapitaIncomeINR": "₹1,41,373",
        "fiscalHealth": "3.5% GSDP (Within Borrowing Cap)",
        "socialProgressIndex": "53.81 (Tier 4 - Lower Middle)",
        "historicalFact": "Focal point of the Bengal Renaissance, birth soil of Rabindranath Tagore, Swami Vivekananda, and Netaji Subhas Chandra Bose.",
        "totalAssembly": 294,
        "totalLokSabha": 42,
        "totalDistricts": 23,
        "majorityMark": 148,
        "currentRuler": "Bharatiya Janata Party (NDA)",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "All India Trinamool Congress": "#10b981",
            "Indian Secular Front": "#3b82f6",
            "Indian National Congress": "#06b6d4",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 150, "pct": 51.0 },
            { "party": "All India Trinamool Congress", "seats": 140, "pct": 47.6 },
            { "party": "Indian Secular Front", "seats": 2, "pct": 0.7 },
            { "party": "Others / Independents", "seats": 2, "pct": 0.7 }
        ]
    },
    "Karnataka": {
        "chiefMinister": { "name": "D. K. Shivakumar", "party": "INC", "logoUrl": "/assets/parties/INC.svg" , "photoUrl": "/assets/candidates/ka_dk_shivakumar.jpg" },
        "deputyChiefMinisters": [
            { "name": "G. Parameshwara", "party": "INC" }
        ],
        "gsdpINR": "₹25.62 Lakh Cr",
        "perCapitaIncomeINR": "₹3,32,926",
        "fiscalHealth": "2.8% GSDP (FRBM Prudent)",
        "socialProgressIndex": "56.77 (Tier 3 - Upper Middle)",
        "historicalFact": "Seat of the Vijayanagara and Kadamba dynasties, modern India's Silicon Valley capital, and pioneer in aerospace, biotech, and scientific research.",
        "totalAssembly": 224,
        "totalLokSabha": 28,
        "totalDistricts": 31,
        "majorityMark": 113,
        "currentRuler": "Indian National Congress",
        "partyColors": {
            "Indian National Congress": "#06b6d4",
            "Bharatiya Janata Party": "#f97316",
            "Janata Dal (Secular)": "#10b981",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Indian National Congress", "seats": 135, "pct": 60.3 },
            { "party": "Bharatiya Janata Party", "seats": 66, "pct": 29.5 },
            { "party": "Janata Dal (Secular)", "seats": 19, "pct": 8.5 },
            { "party": "Others / Independents", "seats": 4, "pct": 1.7 }
        ]
    },
    "Tamil Nadu": {
        "chiefMinister": { "name": "C. Joseph Vijay", "party": "TVK", "logoUrl": "/assets/parties/TVK.svg" , "photoUrl": "/assets/candidates/c_joseph_vijay.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹31.55 Lakh Cr",
        "perCapitaIncomeINR": "₹3,15,220",
        "fiscalHealth": "3.4% GSDP (Stable Public Debt)",
        "socialProgressIndex": "63.33 (Tier 2 - High)",
        "historicalFact": "Ancient cradle of classical Tamil language, Sangam literature, Dravidian monumental temple architecture, and India's top automotive manufacturing exporter.",
        "totalAssembly": 234,
        "totalLokSabha": 39,
        "totalDistricts": 38,
        "majorityMark": 118,
        "currentRuler": "Tamilaga Vettri Kazhagam (TVK+ Alliance)",
        "partyColors": {
            "Tamilaga Vettri Kazhagam": "#eab308",
            "Dravida Munnetra Kazhagam": "#ef4444",
            "All India Anna Dravida Munnetra Kazhagam": "#16a34a",
            "Indian National Congress": "#06b6d4",
            "Bharatiya Janata Party": "#f97316",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Tamilaga Vettri Kazhagam", "seats": 120, "pct": 51.3 },
            { "party": "Dravida Munnetra Kazhagam", "seats": 80, "pct": 34.2 },
            { "party": "All India Anna Dravida Munnetra Kazhagam", "seats": 25, "pct": 10.7 },
            { "party": "Indian National Congress", "seats": 5, "pct": 2.1 },
            { "party": "Others", "seats": 4, "pct": 1.7 }
        ]
    },
    "Kerala": {
        "chiefMinister": { "name": "V. D. Satheesan", "party": "INC", "logoUrl": "/assets/parties/INC.svg" , "photoUrl": "/assets/candidates/v__d__satheesan.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹11.30 Lakh Cr",
        "perCapitaIncomeINR": "₹2,76,825",
        "fiscalHealth": "3.4% GSDP (Social Investment Model)",
        "socialProgressIndex": "65.89 (Tier 1 - Highest in India)",
        "historicalFact": "Historic spice trade cradle of the ancient Chera dynasty, leading independent India with 100% primary literacy, lowest infant mortality, and top human development.",
        "totalAssembly": 140,
        "totalLokSabha": 20,
        "totalDistricts": 14,
        "majorityMark": 71,
        "currentRuler": "United Democratic Front (UDF)",
        "partyColors": {
            "Indian National Congress": "#06b6d4",
            "Communist Party of India (Marxist)": "#ef4444",
            "Indian Union Muslim League": "#10b981",
            "Communist Party of India": "#b91c1c",
            "Kerala Congress (M)": "#f97316",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Indian National Congress", "seats": 55, "pct": 39.3 },
            { "party": "Communist Party of India (Marxist)", "seats": 45, "pct": 32.1 },
            { "party": "Indian Union Muslim League", "seats": 20, "pct": 14.3 },
            { "party": "Communist Party of India", "seats": 10, "pct": 7.1 },
            { "party": "Others / Independents", "seats": 10, "pct": 7.1 }
        ]
    },
    "Uttar Pradesh": {
        "chiefMinister": { "name": "Yogi Adityanath", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/yogi_adityanath.jpg" },
        "deputyChiefMinisters": [
            { "name": "Keshav Prasad Maurya", "party": "BJP" },
            { "name": "Brajesh Pathak", "party": "BJP" }
        ],
        "gsdpINR": "₹27.50 Lakh Cr",
        "perCapitaIncomeINR": "₹95,200",
        "fiscalHealth": "3.2% GSDP (Consolidating)",
        "socialProgressIndex": "48.63 (Tier 5 - Low Middle)",
        "historicalFact": "Cradle of Indo-Gangetic civilizational wisdom, birthplace of Rama and Krishna, and home to world heritage spiritual centers Ayodhya, Varanasi, and Mathura.",
        "totalAssembly": 403,
        "totalLokSabha": 80,
        "totalDistricts": 75,
        "majorityMark": 202,
        "currentRuler": "NDA Alliance",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Samajwadi Party": "#ef4444",
            "Apna Dal (S)": "#8b5cf6",
            "Rashtriya Lok Dal": "#10b981",
            "Indian National Congress": "#06b6d4",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 255, "pct": 63.3 },
            { "party": "Samajwadi Party", "seats": 111, "pct": 27.5 },
            { "party": "Apna Dal (S)", "seats": 12, "pct": 3.0 },
            { "party": "Rashtriya Lok Dal", "seats": 9, "pct": 2.2 },
            { "party": "NISHAD Party & Others", "seats": 16, "pct": 4.0 }
        ]
    },
    "Gujarat": {
        "chiefMinister": { "name": "Bhupendrabhai Patel", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/bhupendrabhai_patel.jpg" },
        "deputyChiefMinisters": [
            { "name": "Harsh Sanghavi", "party": "BJP" }
        ],
        "gsdpINR": "₹25.62 Lakh Cr",
        "perCapitaIncomeINR": "₹3,10,637",
        "fiscalHealth": "1.9% GSDP (Exemplary Fiscal Health)",
        "socialProgressIndex": "58.12 (Tier 3 - Upper Middle)",
        "historicalFact": "Birthplace of Mahatma Gandhi and Sardar Patel, boasting India's longest coastline and pioneering petrochemical, pharmaceutical, and maritime trade ports.",
        "totalAssembly": 182,
        "totalLokSabha": 26,
        "totalDistricts": 33,
        "majorityMark": 92,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Aam Aadmi Party": "#3b82f6",
            "Samajwadi Party": "#10b981",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 156, "pct": 85.7 },
            { "party": "Indian National Congress", "seats": 17, "pct": 9.3 },
            { "party": "Aam Aadmi Party", "seats": 5, "pct": 2.7 },
            { "party": "Samajwadi Party", "seats": 1, "pct": 0.5 },
            { "party": "Others / Independents", "seats": 3, "pct": 1.6 }
        ]
    },
    "Rajasthan": {
        "chiefMinister": { "name": "Bhajan Lal Sharma", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/bhajan_lal_sharma.jpg" },
        "deputyChiefMinisters": [
            { "name": "Diya Kumari", "party": "BJP" },
            { "name": "Prem Chand Bairwa", "party": "BJP" }
        ],
        "gsdpINR": "₹15.28 Lakh Cr",
        "perCapitaIncomeINR": "₹1,61,289",
        "fiscalHealth": "3.9% GSDP (Expanding Capital Outlay)",
        "socialProgressIndex": "50.69 (Tier 4 - Lower Middle)",
        "historicalFact": "Historic land of Rajput valour, UNESCO hill forts, Thar desert heritage, and India's premier solar park green energy corridor.",
        "totalAssembly": 200,
        "totalLokSabha": 25,
        "totalDistricts": 34,
        "majorityMark": 101,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Bharat Adivasi Party": "#10b981",
            "Bahujan Samaj Party": "#3b82f6",
            "Rashtriya Loktantrik Party": "#eab308",
            "Rashtriya Lok Dal": "#84cc16",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 115, "pct": 57.5 },
            { "party": "Indian National Congress", "seats": 69, "pct": 34.5 },
            { "party": "Bharat Adivasi Party", "seats": 3, "pct": 1.5 },
            { "party": "Bahujan Samaj Party", "seats": 2, "pct": 1.0 },
            { "party": "Rashtriya Loktantrik Party", "seats": 1, "pct": 0.5 },
            { "party": "Rashtriya Lok Dal", "seats": 1, "pct": 0.5 },
            { "party": "Others / Independents", "seats": 9, "pct": 4.5 }
        ]
    },
    "Punjab": {
        "chiefMinister": { "name": "Bhagwant Mann", "party": "AAP", "logoUrl": "/assets/parties/AAP.svg" , "photoUrl": "/assets/candidates/bhagwant_mann.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹7.41 Lakh Cr",
        "perCapitaIncomeINR": "₹1,95,419",
        "fiscalHealth": "4.7% GSDP (High Debt Ratio)",
        "socialProgressIndex": "57.73 (Tier 3 - Upper Middle)",
        "historicalFact": "Land of Five Rivers, sacred soil of the Sikh Gurus, and the green revolution bedrock that spearheaded India's national grain self-reliance.",
        "totalAssembly": 117,
        "totalLokSabha": 13,
        "totalDistricts": 22,
        "majorityMark": 59,
        "currentRuler": "Aam Aadmi Party",
        "partyColors": {
            "Aam Aadmi Party": "#3b82f6",
            "Indian National Congress": "#06b6d4",
            "Shiromani Akali Dal": "#f59e0b",
            "Bharatiya Janata Party": "#f97316",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Aam Aadmi Party", "seats": 92, "pct": 78.6 },
            { "party": "Indian National Congress", "seats": 18, "pct": 15.4 },
            { "party": "Shiromani Akali Dal", "seats": 3, "pct": 2.6 },
            { "party": "Bharatiya Janata Party", "seats": 2, "pct": 1.7 },
            { "party": "Others", "seats": 2, "pct": 1.7 }
        ]
    },
    "Assam": {
        "chiefMinister": { "name": "Himanta Biswa Sarma", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/himanta_biswa_sarma.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹5.70 Lakh Cr",
        "perCapitaIncomeINR": "₹1,21,460",
        "fiscalHealth": "3.7% GSDP (Infrastructure Driven)",
        "socialProgressIndex": "51.52 (Tier 4 - Lower Middle)",
        "historicalFact": "Ancient kingdom of Kamarupa and the undefeated six-century Ahom Dynasty, world-renowned for Assam tea, muga silk, and Kaziranga one-horned rhinos.",
        "totalAssembly": 126,
        "totalLokSabha": 14,
        "totalDistricts": 34,
        "majorityMark": 64,
        "currentRuler": "National Democratic Alliance (Mitrajot)",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "All India United Democratic Front": "#10b981",
            "Asom Gana Parishad": "#3b82f6",
            "United People's Party Liberal": "#eab308",
            "Bodoland People's Front": "#ec4899",
            "Communist Party of India (Marxist)": "#ef4444",
            "Raijor Dal": "#8b5cf6",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 60, "pct": 47.6 },
            { "party": "Indian National Congress", "seats": 29, "pct": 23.0 },
            { "party": "All India United Democratic Front", "seats": 16, "pct": 12.7 },
            { "party": "Asom Gana Parishad", "seats": 9, "pct": 7.1 },
            { "party": "United People's Party Liberal", "seats": 6, "pct": 4.8 },
            { "party": "Bodoland People's Front", "seats": 4, "pct": 3.2 },
            { "party": "Communist Party of India (Marxist)", "seats": 1, "pct": 0.8 },
            { "party": "Raijor Dal", "seats": 1, "pct": 0.8 }
        ]
    },
    "Chhattisgarh": {
        "chiefMinister": { "name": "Vishnu Deo Sai", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/vishnu_deo_sai.jpg" },
        "deputyChiefMinisters": [
            { "name": "Arun Sao", "party": "BJP" },
            { "name": "Vijay Sharma", "party": "BJP" }
        ],
        "gsdpINR": "₹5.07 Lakh Cr",
        "perCapitaIncomeINR": "₹1,47,361",
        "fiscalHealth": "2.9% GSDP (Within FRBM Cap)",
        "socialProgressIndex": "51.36 (Tier 4 - Lower Middle)",
        "historicalFact": "Central tribal heartland of ancient Dandakaranya, leading India in mineral wealth, clean energy production, and protected sal forest sanctuaries.",
        "totalAssembly": 90,
        "totalLokSabha": 11,
        "totalDistricts": 28,
        "majorityMark": 46,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Gondwana Gantantra Party": "#10b981",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 54, "pct": 60.0 },
            { "party": "Indian National Congress", "seats": 35, "pct": 38.9 },
            { "party": "Gondwana Gantantra Party", "seats": 1, "pct": 1.1 }
        ]
    },
    "Goa": {
        "chiefMinister": { "name": "Pramod Sawant", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/pramod_sawant.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹1.06 Lakh Cr",
        "perCapitaIncomeINR": "₹5,44,042",
        "fiscalHealth": "2.6% GSDP (Prudent Surplus)",
        "socialProgressIndex": "65.53 (Tier 1 - Very High)",
        "historicalFact": "Maritime confluence of Latin and Konkani traditions along the Arabian Sea, boasting India's highest per-capita GDP and premier eco-tourism biosphere.",
        "totalAssembly": 40,
        "totalLokSabha": 2,
        "totalDistricts": 2,
        "majorityMark": 21,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Aam Aadmi Party": "#3b82f6",
            "Maharashtrawadi Gomantak Party": "#10b981",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 20, "pct": 50.0 },
            { "party": "Indian National Congress", "seats": 11, "pct": 27.5 },
            { "party": "Aam Aadmi Party", "seats": 2, "pct": 5.0 },
            { "party": "Maharashtrawadi Gomantak Party", "seats": 2, "pct": 5.0 },
            { "party": "Others / Independents", "seats": 5, "pct": 12.5 }
        ]
    },
    "Delhi": {
        "chiefMinister": { "name": "Rekha Gupta", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/rekha_gupta.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹11.07 Lakh Cr",
        "perCapitaIncomeINR": "₹4,61,910",
        "fiscalHealth": "0.3% GSDP (Revenue Surplus)",
        "socialProgressIndex": "63.02 (Tier 1 - Very High)",
        "historicalFact": "The historic heart of Bharat along the sacred Yamuna, having served as the epicenter of legendary dynasties, Delhi Sultanate, Mughals, and the modern Republic of India.",
        "totalAssembly": 70,
        "totalLokSabha": 7,
        "totalDistricts": 11,
        "majorityMark": 36,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Aam Aadmi Party": "#3b82f6",
            "Indian National Congress": "#06b6d4",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 48, "pct": 68.6 },
            { "party": "Aam Aadmi Party", "seats": 22, "pct": 31.4 }
        ]
    },
    "Haryana": {
        "chiefMinister": { "name": "Nayab Singh Saini", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" , "photoUrl": "/assets/candidates/nayab_singh_saini.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹11.20 Lakh Cr",
        "perCapitaIncomeINR": "₹3,25,759",
        "fiscalHealth": "2.8% GSDP (FRBM Compliant)",
        "socialProgressIndex": "57.68 (Tier 2 - High)",
        "historicalFact": "The sacred soil of Kurukshetra where the Bhagavad Gita was expounded, serving as the crucible of Vedic ethos and modern India's agrarian powerhouse and automotive industrial corridor.",
        "totalAssembly": 90,
        "totalLokSabha": 10,
        "totalDistricts": 22,
        "majorityMark": 46,
        "currentRuler": "Bharatiya Janata Party",
        "partyColors": {
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Indian National Lok Dal": "#16a34a",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Bharatiya Janata Party", "seats": 48, "pct": 53.3 },
            { "party": "Indian National Congress", "seats": 37, "pct": 41.1 },
            { "party": "Indian National Lok Dal", "seats": 2, "pct": 2.2 },
            { "party": "Others / Independents", "seats": 3, "pct": 3.3 }
        ]
    },
    "Telangana": {
        "chiefMinister": { "name": "A. Revanth Reddy", "party": "INC", "logoUrl": "/assets/parties/INC.svg" , "photoUrl": "/assets/candidates/a_revanth_reddy.jpg" },
        "deputyChiefMinisters": [
            { "name": "Mallu Bhatti Vikramarka", "party": "INC" }
        ],
        "gsdpINR": "₹14.00 Lakh Cr",
        "perCapitaIncomeINR": "₹3,43,297",
        "fiscalHealth": "2.9% GSDP (FRBM Compliant)",
        "socialProgressIndex": "53.41 (Tier 4 - Middle)",
        "historicalFact": "Historic heart of the Deccan plateau, famed for the Golconda Diamond Sultanate and Kakatiya architecture, today powering India's premier biotechnology (Genome Valley) and software hubs.",
        "totalAssembly": 119,
        "totalLokSabha": 17,
        "totalDistricts": 33,
        "majorityMark": 60,
        "currentRuler": "Indian National Congress",
        "partyColors": {
            "Indian National Congress": "#06b6d4",
            "Bharat Rashtra Samithi": "#ec4899",
            "Bharatiya Janata Party": "#f97316",
            "AIMIM": "#15803d",
            "Communist Party of India": "#dc2626"
        },
        "seatTally": [
            { "party": "Indian National Congress", "seats": 64, "pct": 53.8 },
            { "party": "Bharat Rashtra Samithi", "seats": 39, "pct": 32.8 },
            { "party": "Bharatiya Janata Party", "seats": 8, "pct": 6.7 },
            { "party": "AIMIM", "seats": 7, "pct": 5.9 },
            { "party": "Communist Party of India", "seats": 1, "pct": 0.8 }
        ]
    },
    "Jammu & Kashmir": {
        "chiefMinister": { "name": "Omar Abdullah", "party": "JKNC", "logoUrl": "/assets/parties/JKNC.svg" , "photoUrl": "/assets/candidates/omar_abdullah.jpg" },
        "deputyChiefMinisters": [
            { "name": "Surinder Kumar Choudhary", "party": "JKNC" }
        ],
        "gsdpINR": "₹2.45 Lakh Cr",
        "perCapitaIncomeINR": "₹1,43,500",
        "fiscalHealth": "3.1% GSDP (Central Grants Support)",
        "socialProgressIndex": "54.12 (Tier 3 - Upper Middle)",
        "historicalFact": "The crown of the Himalayas and cradle of Kashmiri Shaivism and Sufi Rishism, celebrated worldwide for saffron cultivation, handicraft artistry, and the serene Dal Lake.",
        "totalAssembly": 90,
        "totalLokSabha": 5,
        "totalDistricts": 20,
        "majorityMark": 46,
        "currentRuler": "JKNC-INC Alliance",
        "partyColors": {
            "Jammu & Kashmir National Conference": "#dc2626",
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "Jammu & Kashmir People's Democratic Party": "#16a34a",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Jammu & Kashmir National Conference", "seats": 42, "pct": 46.7 },
            { "party": "Bharatiya Janata Party", "seats": 29, "pct": 32.2 },
            { "party": "Indian National Congress", "seats": 6, "pct": 6.7 },
            { "party": "Jammu & Kashmir People's Democratic Party", "seats": 3, "pct": 3.3 },
            { "party": "Others / Independents", "seats": 10, "pct": 11.1 }
        ]
    },
    "Jharkhand": {
        "chiefMinister": { "name": "Hemant Soren", "party": "JMM", "logoUrl": "/assets/parties/JMM.svg" , "photoUrl": "/assets/candidates/hemant_soren.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹4.23 Lakh Cr",
        "perCapitaIncomeINR": "₹98,500",
        "fiscalHealth": "2.8% GSDP (Under Control)",
        "socialProgressIndex": "43.95 (Tier 6 - Lowest Tier)",
        "historicalFact": "Carved out of southern Bihar in 2000, Jharkhand is the legendary land of tribal heroes Bhagwan Birsa Munda, Tilka Manjhi, and Sido-Kanhu, possessing over 40% of India's mineral reserves.",
        "totalAssembly": 81,
        "totalLokSabha": 14,
        "totalDistricts": 24,
        "majorityMark": 41,
        "currentRuler": "INDIA Alliance (JMM-INC-RJD-CPI-ML)",
        "partyColors": {
            "Jharkhand Mukti Morcha": "#16a34a",
            "Bharatiya Janata Party": "#f97316",
            "Indian National Congress": "#06b6d4",
            "AJSU Party": "#fbbf24",
            "Rashtriya Janata Dal": "#22c55e",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Jharkhand Mukti Morcha", "seats": 34, "pct": 42.0 },
            { "party": "Bharatiya Janata Party", "seats": 21, "pct": 25.9 },
            { "party": "Indian National Congress", "seats": 16, "pct": 19.8 },
            { "party": "Rashtriya Janata Dal", "seats": 4, "pct": 4.9 },
            { "party": "CPI (ML) Liberation", "seats": 2, "pct": 2.5 },
            { "party": "AJSU Party", "seats": 1, "pct": 1.2 },
            { "party": "Others / Independents", "seats": 3, "pct": 3.7 }
        ]
    },
    "Himachal Pradesh": {
        "chiefMinister": { "name": "Sukhvinder Singh Sukhu", "party": "INC", "logoUrl": "/assets/parties/INC.svg" , "photoUrl": "/assets/candidates/sukhvinder_singh_sukhu.jpg" },
        "deputyChiefMinisters": [
            { "name": "Mukesh Agnihotri", "party": "INC" }
        ],
        "gsdpINR": "₹2.14 Lakh Cr",
        "perCapitaIncomeINR": "₹2,35,000",
        "fiscalHealth": "3.2% GSDP (Hill State Grant Support)",
        "socialProgressIndex": "63.28 (Tier 2 - High Social Progress)",
        "historicalFact": "Revered as Dev Bhumi (Abode of Gods), Himachal Pradesh was granted full statehood in 1971, pioneering mountain hydro-power generation, world-famous apple horticulture, and top literacy standards.",
        "totalAssembly": 68,
        "totalLokSabha": 4,
        "totalDistricts": 12,
        "majorityMark": 35,
        "currentRuler": "Indian National Congress",
        "partyColors": {
            "Indian National Congress": "#06b6d4",
            "Bharatiya Janata Party": "#f97316",
            "Independents / Others": "#64748b"
        },
        "seatTally": [
            { "party": "Indian National Congress", "seats": 40, "pct": 58.8 },
            { "party": "Bharatiya Janata Party", "seats": 25, "pct": 36.8 },
            { "party": "Independents / Others", "seats": 3, "pct": 4.4 }
        ]
    },
    "Andhra Pradesh": {
        "chiefMinister": { "name": "N. Chandrababu Naidu", "party": "TDP", "logoUrl": "/assets/parties/TDP.svg" , "photoUrl": "/assets/candidates/chandrababu_naidu.jpg" },
        "deputyChiefMinisters": [
            { "name": "Pawan Kalyan", "party": "JSP" }
        ],
        "gsdpINR": "₹14.50 Lakh Cr",
        "perCapitaIncomeINR": "₹2,42,000",
        "fiscalHealth": "3.1% GSDP (Development Focus)",
        "socialProgressIndex": "53.60 (Tier 4 - Lower Middle)",
        "historicalFact": "First state formed on a linguistic basis in 1953, Andhra Pradesh is the rice bowl of India with India's second longest coastline (974 km) and the sacred Tirumala Venkateswara shrine.",
        "totalAssembly": 175,
        "totalLokSabha": 25,
        "totalDistricts": 26,
        "majorityMark": 88,
        "currentRuler": "NDA (TDP-JSP-BJP Alliance)",
        "partyColors": {
            "Telugu Desam Party": "#eab308",
            "Jana Sena Party": "#dc2626",
            "Bharatiya Janata Party": "#f97316",
            "YSR Congress Party": "#3b82f6",
            "Others": "#64748b"
        },
        "seatTally": [
            { "party": "Telugu Desam Party", "seats": 135, "pct": 77.1 },
            { "party": "Jana Sena Party", "seats": 21, "pct": 12.0 },
            { "party": "Bharatiya Janata Party", "seats": 8, "pct": 4.6 },
            { "party": "YSR Congress Party", "seats": 11, "pct": 6.3 }
        ]
    },
    "Chandigarh": {
        "chiefMinister": { "name": "Manish Tewari (MP)", "party": "INC", "logoUrl": "/assets/parties/INC.svg" , "photoUrl": "/assets/candidates/manish_tewari.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹0.65 Lakh Cr",
        "perCapitaIncomeINR": "₹3,92,000",
        "fiscalHealth": "Balanced (UT Central Allocation)",
        "socialProgressIndex": "62.40 (Tier 2 - High Social Progress)",
        "historicalFact": "Conceived by Jawaharlal Nehru and master-planned by Swiss-French architect Le Corbusier in 1952, Chandigarh is India's first planned modernist city and joint capital of Punjab & Haryana.",
        "totalAssembly": 0,
        "totalLokSabha": 1,
        "totalDistricts": 1,
        "majorityMark": 1,
        "currentRuler": "Union Territory Administration",
        "partyColors": {
            "Indian National Congress": "#06b6d4",
            "Bharatiya Janata Party": "#f97316"
        },
        "seatTally": [
            { "party": "Indian National Congress", "seats": 1, "pct": 100.0 }
        ]
    },
    "Ladakh": {
        "chiefMinister": { "name": "Mohmad Haneefa (MP)", "party": "Independent", "logoUrl": "/assets/parties/Independent.svg" , "photoUrl": "/assets/candidates/mohmad_haneefa.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹0.12 Lakh Cr",
        "perCapitaIncomeINR": "₹1,85,000",
        "fiscalHealth": "Special Central Development Assistance",
        "socialProgressIndex": "52.80 (Tier 4 - Lower Middle)",
        "historicalFact": "The high-altitude Land of High Passes on the ancient Silk Route, celebrated for centuries-old Buddhist gompas, Pangong Tso, and rare Changthangi Pashmina goats.",
        "totalAssembly": 0,
        "totalLokSabha": 1,
        "totalDistricts": 2,
        "majorityMark": 1,
        "currentRuler": "Union Territory Administration",
        "partyColors": {
            "Independent": "#64748b",
            "Indian National Congress": "#06b6d4",
            "Bharatiya Janata Party": "#f97316"
        },
        "seatTally": [
            { "party": "Independent", "seats": 1, "pct": 100.0 }
        ]
    },
    "Puducherry": {
        "chiefMinister": { "name": "N. Rangasamy", "party": "AINRC", "logoUrl": "/assets/parties/AINRC.svg" , "photoUrl": "/assets/candidates/n_rangasamy.jpg" },
        "deputyChiefMinisters": [],
        "gsdpINR": "₹0.48 Lakh Cr",
        "perCapitaIncomeINR": "₹2,60,000",
        "fiscalHealth": "2.9% GSDP (Central Support)",
        "socialProgressIndex": "65.99 (Tier 1 - Highest Tier)",
        "historicalFact": "A former French colonial territory integrating Pondicherry, Karaikal, Mahe, and Yanam, renowned for Sri Aurobindo Ashram, Auroville, and seaside French promenade architecture.",
        "totalAssembly": 30,
        "totalLokSabha": 1,
        "totalDistricts": 4,
        "majorityMark": 16,
        "currentRuler": "NDA (AINRC-BJP Alliance)",
        "partyColors": {
            "All India N.R. Congress": "#eab308",
            "Bharatiya Janata Party": "#f97316",
            "Dravida Munnetra Kazhagam": "#dc2626",
            "Indian National Congress": "#06b6d4",
            "Others / Independents": "#64748b"
        },
        "seatTally": [
            { "party": "All India N.R. Congress", "seats": 10, "pct": 33.3 },
            { "party": "Bharatiya Janata Party", "seats": 6, "pct": 20.0 },
            { "party": "Dravida Munnetra Kazhagam", "seats": 6, "pct": 20.0 },
            { "party": "Indian National Congress", "seats": 2, "pct": 6.7 },
            { "party": "Others / Independents", "seats": 6, "pct": 20.0 }
        ]
    }
}
