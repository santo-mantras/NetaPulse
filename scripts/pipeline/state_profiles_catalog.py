"""
NetaPulse State Profiles Catalog
Maintains verified state governance profiles including Chief Ministers, Deputy Chief Ministers,
Macroeconomic Indicators (GSDP, Per Capita), Fiscal Health, Social Progress Index, and Historical Legacies.
Enables automated periodic updates via GitHub Actions workflow.
"""

STATE_PROFILES = {
    "Maharashtra": {
        "chiefMinister": { "name": "Devendra Fadnavis", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Samrat Choudhary", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
        "deputyChiefMinisters": [
            { "name": "Bijendra Prasad Yadav", "party": "JD(U)" },
            { "name": "Vijay Kumar Chaudhary", "party": "JD(U)" }
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
        "chiefMinister": { "name": "Suvendu Adhikari", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "D. K. Shivakumar", "party": "INC", "logoUrl": "/assets/parties/INC.svg" },
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
        "chiefMinister": { "name": "C. Joseph Vijay", "party": "TVK", "logoUrl": "/assets/parties/TVK.svg" },
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
        "chiefMinister": { "name": "V. D. Satheesan", "party": "INC", "logoUrl": "/assets/parties/INC.svg" },
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
        "chiefMinister": { "name": "Yogi Adityanath", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Bhupendrabhai Patel", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Bhajan Lal Sharma", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Bhagwant Mann", "party": "AAP", "logoUrl": "/assets/parties/AAP.svg" },
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
        "chiefMinister": { "name": "Himanta Biswa Sarma", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Vishnu Deo Sai", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Pramod Sawant", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
        "chiefMinister": { "name": "Rekha Gupta", "party": "BJP", "logoUrl": "/assets/parties/BJP.svg" },
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
    }
}
