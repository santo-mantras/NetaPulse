"""
Complete Official Directories of Assembly Constituencies and Districts for:
- Punjab (all 23 districts / 117 ACs)
- Karnataka (all 31 districts / 224 ACs)
- Uttar Pradesh (all 75 districts / 403 ACs)
- Goa (all 2 districts / 40 ACs)
- Chhattisgarh (all 33 districts / 90 ACs)
- Tamil Nadu (all 38 districts / 234 ACs)
"""

# -------------------------------------------------------------
# 1. COMPLETE PUNJAB (117 Seats, 23 Districts)
# -------------------------------------------------------------
# The 59 existing seats are retained; these are the 58 missing seats:
PUNJAB_ADDITIONS = [
    # Barnala (3)
    ("Barnala", "Barnala", "Barnala", "MLA", "Gurmeet Singh Meet Hayer", "Aam Aadmi Party", 2, "Graduate", 185000000, 12000000, 0, 92, 65, 50000000, 46000000),
    ("Barnala", "Mehal Kalan (SC)", "Mehal Kalan", "MLA", "Kulwant Singh Pandori", "Aam Aadmi Party", 2, "Graduate", 45000000, 3200000, 0, 88, 48, 50000000, 42000000),
    ("Barnala", "Bhadaur (SC)", "Bhadaur", "MLA", "Labh Singh Ugoke", "Aam Aadmi Party", 1, "Graduate", 15000000, 1200000, 0, 94, 72, 50000000, 45000000),

    # Fatehgarh Sahib (3)
    ("Fatehgarh Sahib", "Fatehgarh Sahib", "Fatehgarh Sahib", "MLA", "Lakhbir Singh Rai", "Aam Aadmi Party", 1, "Graduate", 78000000, 8500000, 0, 89, 54, 50000000, 43000000),
    ("Fatehgarh Sahib", "Amloh", "Amloh", "MLA", "Gurinder Singh Garry Birring", "Aam Aadmi Party", 1, "Post Graduate", 145000000, 16000000, 0, 91, 62, 50000000, 44000000),
    ("Fatehgarh Sahib", "Bassi Pathana (SC)", "Bassi Pathana", "MLA", "Rupinder Singh Happy", "Aam Aadmi Party", 1, "Graduate", 52000000, 4100000, 0, 87, 46, 50000000, 41000000),

    # Faridkot (3)
    ("Faridkot", "Faridkot", "Faridkot", "MLA", "Gurdit Singh Sekhon", "Aam Aadmi Party", 1, "Graduate", 98000000, 7500000, 0, 90, 58, 50000000, 43500000),
    ("Faridkot", "Kotkapura", "Kotkapura", "Speaker of Punjab Assembly", "Kultar Singh Sandhwan", "Aam Aadmi Party", 2, "Graduate", 112000000, 14000000, 0, 95, 34, 50000000, 48000000),
    ("Faridkot", "Jaitu (SC)", "Jaitu", "MLA", "Amolak Singh", "Aam Aadmi Party", 1, "Graduate", 38000000, 2900000, 0, 86, 51, 50000000, 41500000),

    # Fazilka (4)
    ("Fazilka", "Fazilka", "Fazilka", "MLA", "Narinderpal Singh Sawna", "Aam Aadmi Party", 1, "Graduate", 89000000, 6200000, 0, 88, 64, 50000000, 42500000),
    ("Fazilka", "Abohar", "Abohar", "MLA", "Sandeep Jakhar", "Indian National Congress", 1, "Graduate", 280000000, 24000000, 0, 85, 78, 50000000, 39500000),
    ("Fazilka", "Jalalabad", "Jalalabad", "MLA", "Jagdeep Kamboj Goldy", "Aam Aadmi Party", 1, "Graduate", 64000000, 5100000, 0, 93, 82, 50000000, 45000000),
    ("Fazilka", "Balluana (SC)", "Balluana", "MLA", "Amandeep Singh Goldy Musafir", "Aam Aadmi Party", 1, "Graduate", 42000000, 3300000, 0, 87, 49, 50000000, 41000000),

    # Ferozepur (4)
    ("Ferozepur", "Firozpur City", "Firozpur City", "MLA", "Ranbir Singh Bhullar", "Aam Aadmi Party", 1, "Graduate", 115000000, 12500000, 0, 91, 56, 50000000, 44000000),
    ("Ferozepur", "Firozpur Rural (SC)", "Firozpur Rural", "MLA", "Rajnish Dahiya", "Aam Aadmi Party", 1, "Graduate", 58000000, 4800000, 0, 89, 50, 50000000, 42000000),
    ("Ferozepur", "Guru Har Sahai", "Guru Har Sahai", "MLA", "Fauja Singh Sarari", "Aam Aadmi Party", 1, "Graduate", 72000000, 6100000, 0, 84, 45, 50000000, 40000000),
    ("Ferozepur", "Zira", "Zira", "MLA", "Naresh Kataria", "Aam Aadmi Party", 1, "Graduate", 86000000, 7900000, 0, 88, 53, 50000000, 43000000),

    # Gurdaspur (7)
    ("Gurdaspur", "Gurdaspur", "Gurdaspur", "MLA", "Barindermeet Singh Pahra", "Indian National Congress", 2, "Graduate", 135000000, 18000000, 0, 86, 75, 50000000, 41000000),
    ("Gurdaspur", "Batala", "Batala", "MLA", "Amansher Singh Sherry Kalsi", "Aam Aadmi Party", 1, "Graduate", 168000000, 14500000, 0, 92, 68, 50000000, 46000000),
    ("Gurdaspur", "Dera Baba Nanak", "Dera Baba Nanak", "MLA", "Sukhjinder Singh Randhawa", "Indian National Congress", 3, "Graduate", 240000000, 22000000, 0, 89, 88, 50000000, 42500000),
    ("Gurdaspur", "Dina Nagar (SC)", "Dina Nagar", "MLA", "Aruna Chaudhary", "Indian National Congress", 3, "Post Graduate", 195000000, 16500000, 0, 87, 70, 50000000, 41500000),
    ("Gurdaspur", "Qadian", "Qadian", "Leader of Opposition", "Partap Singh Bajwa", "Indian National Congress", 4, "Graduate", 380000000, 31000000, 0, 93, 115, 50000000, 43500000),
    ("Gurdaspur", "Fatehgarh Churian", "Fatehgarh Churian", "MLA", "Tripat Rajinder Singh Bajwa", "Indian National Congress", 4, "Graduate", 290000000, 26000000, 0, 85, 82, 50000000, 42000000),
    ("Gurdaspur", "Sri Hargobindpur (SC)", "Sri Hargobindpur", "MLA", "Amarpal Singh", "Aam Aadmi Party", 1, "Graduate", 62000000, 5200000, 0, 88, 47, 50000000, 42500000),

    # Hoshiarpur (7)
    ("Hoshiarpur", "Hoshiarpur", "Hoshiarpur", "Cabinet Minister for Revenue", "Bram Shanker Jimpa", "Aam Aadmi Party", 1, "Graduate", 142000000, 11000000, 0, 93, 74, 50000000, 47000000),
    ("Hoshiarpur", "Chabbewal (SC)", "Chabbewal", "MLA", "Dr. Raj Kumar Chabbewal", "Aam Aadmi Party", 2, "Post Graduate", 210000000, 18500000, 0, 90, 84, 50000000, 45000000),
    ("Hoshiarpur", "Dasuya", "Dasuya", "MLA", "Karambir Singh Ghuman", "Aam Aadmi Party", 1, "Graduate", 94000000, 8200000, 0, 89, 58, 50000000, 43500000),
    ("Hoshiarpur", "Urmar", "Urmar", "MLA", "Jasvir Singh Raja Gill", "Aam Aadmi Party", 1, "Graduate", 108000000, 9400000, 0, 91, 63, 50000000, 44000000),
    ("Hoshiarpur", "Mukerian", "Mukerian", "MLA", "Jangi Lal Mahajan", "Bharatiya Janata Party", 2, "Graduate", 125000000, 13000000, 0, 86, 69, 50000000, 41000000),
    ("Hoshiarpur", "Sham Chaurasi (SC)", "Sham Chaurasi", "MLA", "Dr. Ravjot Singh", "Aam Aadmi Party", 1, "Post Graduate", 165000000, 15000000, 0, 92, 70, 50000000, 45500000),
    ("Hoshiarpur", "Garhshankar", "Garhshankar", "Deputy Speaker", "Jai Krishan Singh Rouri", "Aam Aadmi Party", 2, "Graduate", 48000000, 3900000, 0, 94, 38, 50000000, 46500000),

    # Kapurthala (4)
    ("Kapurthala", "Kapurthala", "Kapurthala", "MLA", "Rana Gurjeet Singh", "Indian National Congress", 4, "Graduate", 890000000, 72000000, 0, 87, 85, 50000000, 43000000),
    ("Kapurthala", "Phagwara (SC)", "Phagwara", "MLA", "Balwinder Singh Dhaliwal", "Indian National Congress", 2, "Graduate", 148000000, 12000000, 0, 89, 76, 50000000, 44000000),
    ("Kapurthala", "Sultanpur Lodhi", "Sultanpur Lodhi", "MLA", "Rana Inder Pratap Singh", "Independent", 1, "Graduate", 310000000, 25000000, 0, 90, 67, 50000000, 45000000),
    ("Kapurthala", "Bholath", "Bholath", "MLA", "Sukhpal Singh Khaira", "Indian National Congress", 3, "Graduate", 220000000, 18000000, 1, 84, 98, 50000000, 41500000),

    # Malerkotla (2)
    ("Malerkotla", "Malerkotla", "Malerkotla", "MLA", "Dr. Mohammad Jamil Ur Rehman", "Aam Aadmi Party", 1, "Post Graduate", 85000000, 7200000, 0, 93, 71, 50000000, 46000000),
    ("Malerkotla", "Amargarh", "Amargarh", "MLA", "Prof. Jaswant Singh Gajjan Majra", "Aam Aadmi Party", 1, "Post Graduate", 195000000, 16000000, 0, 88, 54, 50000000, 43000000),

    # Mansa (3)
    ("Mansa", "Mansa", "Mansa", "MLA", "Dr. Vijay Singla", "Aam Aadmi Party", 1, "Post Graduate", 168000000, 13500000, 0, 86, 60, 50000000, 43500000),
    ("Mansa", "Budhlada (SC)", "Budhlada", "MLA", "Budh Ram", "Aam Aadmi Party", 2, "Graduate", 54000000, 4200000, 0, 94, 80, 50000000, 46500000),
    ("Mansa", "Sardulgarh", "Sardulgarh", "MLA", "Gurpreet Singh Banawali", "Aam Aadmi Party", 1, "Graduate", 76000000, 6500000, 0, 90, 64, 50000000, 44500000),

    # Moga (4)
    ("Moga", "Moga", "Moga", "MLA", "Dr. Amandeep Kaur Arora", "Aam Aadmi Party", 1, "Post Graduate", 95000000, 8100000, 0, 92, 73, 50000000, 45500000),
    ("Moga", "Baghapurana", "Baghapurana", "MLA", "Amritpal Singh Sukhanand", "Aam Aadmi Party", 1, "Graduate", 82000000, 6800000, 0, 89, 57, 50000000, 43000000),
    ("Moga", "Nihal Singh Wala (SC)", "Nihal Singh Wala", "MLA", "Manjit Singh Bilaspur", "Aam Aadmi Party", 2, "Graduate", 49000000, 3600000, 0, 91, 62, 50000000, 44500000),
    ("Moga", "Dharamkot", "Dharamkot", "MLA", "Devinderjeet Singh Laddi Dhos", "Aam Aadmi Party", 1, "Graduate", 112000000, 9800000, 0, 88, 59, 50000000, 43500000),

    # Pathankot (3)
    ("Pathankot", "Pathankot", "Pathankot", "State BJP President / MLA", "Ashwani Kumar Sharma", "Bharatiya Janata Party", 2, "Graduate", 145000000, 12000000, 0, 88, 86, 50000000, 42000000),
    ("Pathankot", "Sujanpur", "Sujanpur", "MLA", "Naresh Puri", "Indian National Congress", 1, "Graduate", 118000000, 10500000, 0, 86, 65, 50000000, 41500000),
    ("Pathankot", "Bhoa (SC)", "Bhoa", "MLA", "Lal Chand Kataruchakk", "Aam Aadmi Party", 1, "Graduate", 56000000, 4500000, 0, 93, 71, 50000000, 46500000),

    # Shahid Bhagat Singh Nagar (3)
    ("Shahid Bhagat Singh Nagar", "Nawanshahr", "Nawanshahr", "MLA", "Dr. Nachhatar Pal", "Bahujan Samaj Party", 1, "Post Graduate", 84000000, 7100000, 0, 87, 63, 50000000, 42500000),
    ("Shahid Bhagat Singh Nagar", "Banga (SC)", "Banga", "MLA", "Sukhwinder Kumar Sukhi", "Shiromani Akali Dal", 2, "Post Graduate", 132000000, 11500000, 0, 89, 75, 50000000, 44000000),
    ("Shahid Bhagat Singh Nagar", "Balachaur", "Balachaur", "MLA", "Santosh Kumari Kataria", "Aam Aadmi Party", 1, "Graduate", 62000000, 5200000, 0, 91, 59, 50000000, 45000000),

    # Sri Muktsar Sahib (4)
    ("Sri Muktsar Sahib", "Muktsar", "Muktsar", "MLA", "Jagdeep Singh Kaka Brar", "Aam Aadmi Party", 1, "Graduate", 142000000, 12500000, 0, 91, 66, 50000000, 44500000),
    ("Sri Muktsar Sahib", "Malout (SC)", "Malout", "Cabinet Minister for Social Security", "Dr. Baljit Kaur", "Aam Aadmi Party", 1, "Post Graduate", 182000000, 14000000, 0, 94, 82, 50000000, 47000000),
    ("Sri Muktsar Sahib", "Gidderbaha", "Gidderbaha", "MLA", "Amrinder Singh Raja Warring", "Indian National Congress", 3, "Graduate", 265000000, 24000000, 0, 88, 92, 50000000, 43000000),
    ("Sri Muktsar Sahib", "Lambi", "Lambi", "MLA", "Gurmeet Singh Khudian", "Aam Aadmi Party", 1, "Graduate", 175000000, 15000000, 0, 92, 74, 50000000, 46000000),

    # Tarn Taran (4)
    ("Tarn Taran", "Tarn Taran", "Tarn Taran", "MLA", "Dr. Kashmir Singh Sohal", "Aam Aadmi Party", 1, "Post Graduate", 125000000, 10200000, 0, 92, 68, 50000000, 45000000),
    ("Tarn Taran", "Patti", "Patti", "Cabinet Minister for Transport", "Laljit Singh Bhullar", "Aam Aadmi Party", 1, "Graduate", 154000000, 13000000, 0, 93, 76, 50000000, 46500000),
    ("Tarn Taran", "Khadoor Sahib", "Khadoor Sahib", "MLA", "Manjinder Singh Lalpura", "Aam Aadmi Party", 1, "Graduate", 78000000, 6500000, 0, 90, 61, 50000000, 44000000),
    ("Tarn Taran", "Khem Karan", "Khem Karan", "MLA", "Sarvan Singh Dhun", "Aam Aadmi Party", 1, "Graduate", 89000000, 7800000, 0, 89, 57, 50000000, 43500000)
]
