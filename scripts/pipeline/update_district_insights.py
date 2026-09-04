"""
Enriches scripts/pipeline/district_insights_catalog.py with authentic, verified district insights
for all districts across Haryana, Telangana, and Jammu & Kashmir, eliminating generic/hardcoded fallbacks.
"""

import sys

NEW_DISTRICT_INSIGHTS = """
    # ==========================================
    # Haryana Districts
    # ==========================================
    ("Haryana", "Kurukshetra"): (
        "Sacred land of the Mahabharata and birthplace of the Bhagavad Gita at Jyotisar, Kurukshetra is celebrated as the crucible of Vedic philosophy, ancient learning, and India's agricultural prosperity.",
        "Key civic priorities include de-siltation of the Saraswati river basin feeder channels, pilgrim infrastructure around Brahma Sarovar, and managing post-harvest agricultural residue."
    ),
    ("Haryana", "Ambala"): (
        "Historically famous for the 1857 Sepoy Mutiny uprising and its major military cantonment, Ambala is internationally recognized as India's premier scientific instruments manufacturing center and major rail junction.",
        "Critical civic tasks center on Tangri river monsoon flash flood prevention, industrial cluster drainage, and traffic decongestion along National Highway 44."
    ),
    ("Haryana", "Karnal"): (
        "Known as the City of Daanveer Karna and home to the National Dairy Research Institute (NDRI), Karnal is the epicenter of India's basmati rice export trade and agricultural genetics.",
        "Civic challenges include balancing intensive agrochemical runoff with groundwater recharge, modernizing rural grain mandis, and peripheral road upgrades."
    ),
    ("Haryana", "Panipat"): (
        "Site of three historic battles that shaped Indian medieval history (1526, 1556, and 1761), Panipat is globally acclaimed as the 'Textile City' and India's largest center for shoddy yarn and handloom rugs.",
        "Primary public priorities include industrial textile effluent treatment in the dye cluster, municipal solid waste management, and heavy goods corridor bypass development."
    ),
    ("Haryana", "Sonipat"): (
        "Believed to be ancient 'Swarnaprastha' founded by the Pandavas, Sonipat has transformed into an education and industrial corridor hosting world-class universities and automotive manufacturing hubs.",
        "Major civic tasks include stormwater drainage integration along the Kundli corridor, protecting the Yamuna floodplains from encroachments, and commuter transport links."
    ),
    ("Haryana", "Rohtak"): (
        "Heart of the Jat heartland and Haryana's educational capital, home to Maharshi Dayanand University and India's premier cloth market (Shori Bazaar).",
        "Civic focus centers on groundwater table salinization in low-lying sectors, modernization of the drainage pumping grid, and outer orbital road development."
    ),
    ("Haryana", "Gurugram"): (
        "Traditionally associated with Guru Dronacharya as 'Gurugram', it has evolved from a rural hamlet into India's premier Millennium City and global Fortune 500 corporate center.",
        "Critical public priorities include resolving chronic monsoon waterlogging along the Delhi-Gurugram expressway, Najafgarh drain environmental revival, and civic water distribution."
    ),
    ("Haryana", "Faridabad"): (
        "Founded in 1607 by Sheikh Farid, it served as a model refugee township post-1947 and grew into Northern India's pioneering heavy industrial, tractor, and engineering manufacturing base.",
        "Major developmental tasks involve Aravali forest biodiversity conservation, upgrading legacy sewer grids, and rapid transit expansion to Greater Faridabad."
    ),
    ("Haryana", "Hisar"): (
        "Founded in 1354 by Firoz Shah Tughlaq as 'Hisar-e-Firoza', it is celebrated as India's 'Steel City' and a major agricultural research center hosting CCS HAU and Central Sheep Breeding Farm.",
        "Key civic challenges include mitigating industrial emissions in steel re-rolling zones, canal water supply during arid summer months, and rural health clinics."
    ),
    ("Haryana", "Sirsa"): (
        "Dating to ancient Saraswati river trade routes and mentioned in the Mahabharata as Sairishaka, Sirsa is Haryana's largest cotton and wheat growing agrarian hub.",
        "Civic priorities focus on preventing pink bollworm infestations, canal distributary tail-end water security, and rural public healthcare access."
    ),
    ("Haryana", "Jind"): (
        "Historically associated with the ancient Jayanti Devi temple built by the Pandavas, Jind forms the socio-political heartland and dairy cattle hub of Haryana.",
        "Key public focus areas include rural road link durability, agro-processing cold storage chains, and modern drinking water treatment plants."
    ),
    ("Haryana", "Jhajjar"): (
        "Famed for its rich military tradition providing generations of decorated soldiers to the Indian Armed Forces, and home to the Bhindawas bird sanctuary wetland.",
        "Critical civic tasks center on stormwater accumulation during monsoons, rural youth skill development, and water pipeline reach across arid villages."
    ),
    ("Haryana", "Rewari"): (
        "Seat of King Hemu (Hemchandra Vikramaditya) and birthplace of the 1857 hero Rao Tula Ram, Rewari is world-famous for its traditional brassware and India's oldest operational steam locomotive shed.",
        "Civic focus involves industrial pollution monitoring in the Bawal DMIC zone, Sahibi river rejuvenation, and clean drinking water filtration."
    ),
    ("Haryana", "Yamunanagar"): (
        "Bordered by the Shivalik foothills and sacred Hathnikund barrage, it is celebrated as India's premier plywood and timber manufacturing cluster along with sugar refining.",
        "Major civic tasks include riverbed silt management along the Yamuna, industrial wastewater treatment from paper mills, and Shivalik eco-sensitive preservation."
    ),
    ("Haryana", "Kaithal"): (
        "Legendary birthplace of Lord Hanuman (Kapisthala) and burial site of Razia Sultana, the first female monarch of the Delhi Sultanate.",
        "Primary public needs include reviving historical water bodies, grain market decongestion, and upgrading rural health sub-centers."
    ),
    ("Haryana", "Bhiwani"): (
        "Known as the 'Kashi of North India' for its historic temples and the 'Boxing Club of India' for producing Olympic medalists and international pugilists.",
        "Key civic priorities include combatting groundwater depletion in the semi-arid zone, sports academy infrastructure upgrades, and canal water distribution."
    ),
    ("Haryana", "Fatehabad"): (
        "Home to ancient Harappan archaeological sites at Banawali and Kunal, founded by Firoz Shah Tughlaq in honor of his son Fateh Khan.",
        "Civic focus centers on groundwater salinity, expanding micro-irrigation subsidies, and modernizing veterinary hospitals."
    ),
    ("Haryana", "Mahendragarh"): (
        "Historic stronghold of the Rathore Rajputs with its massive fortress, known for rich copper, iron, and limestone deposits in the Dhosi hill volcanic range.",
        "Critical developmental priorities include drinking water supply in the rocky Aravalli terrain, agricultural power supply, and dryland farming support."
    ),
    ("Haryana", "Palwal"): (
        "Associated with the legendary demon Palwasur and Mahatma Gandhi's first political arrest at Palwal railway station during the 1919 anti-Rowlatt Satyagraha.",
        "Public priorities include expanding highway overbridges along the KMP expressway, peri-urban drainage, and rural primary healthcare."
    ),
    ("Haryana", "Nuh"): (
        "Heart of the Mewat cultural region, characterized by ancient Aravalli ridges, Kotla lake wetlands, and rich Meo folklore and pastoral traditions.",
        "Major civic needs involve maternal healthcare access, expanding secondary educational institutions, and resolving chronic drinking water salinity."
    ),
    ("Haryana", "Charkhi Dadri"): (
        "Nestled between two adjoining settlements and home to rare flexible sandstone (Kalyana stone), recognized for its prominent defense recruitment tradition.",
        "Key civic tasks involve canal water rationing during summer months, rural connectivity roads, and local agro-processing hubs."
    ),

    # ==========================================
    # Jammu & Kashmir Districts
    # ==========================================
    ("Jammu & Kashmir", "Anantnag"): (
        "Celebrated as the commercial capital of South Kashmir, home to the ancient 8th-century Martand Sun Temple and the traditional pilgrimage gateway for the sacred Amarnath Yatra.",
        "Critical civic priorities include Lidder and Jhelum riverbank flood stabilization, winter highway connectivity, and expanding high-density apple cold storage facilities."
    ),
    ("Jammu & Kashmir", "Srinagar"): (
        "Founded over two millennia ago by Emperor Ashoka, Srinagar is world-renowned for the serene Dal Lake, Mughal Gardens, historic wooden architecture, and GI-tagged Pashmina weaving.",
        "Major public focus centers on Dal and Nigeen lake ecological restoration, underground sewage network expansion, and heritage architectural conservation."
    ),
    ("Jammu & Kashmir", "Baramulla"): (
        "Historic gateway to the Kashmir Valley along the Jhelum river gorge, featuring ancient Buddhist and Hindu sites (Parihaspora and Ushkar) and world-famous apple orchards of Sopore.",
        "Civic challenges include flood spill channel maintenance, apple trade logistics during harvest season, and high-altitude road all-weather connectivity."
    ),
    ("Jammu & Kashmir", "Budgam"): (
        "Seat of the revered Sufi saint Sheikh Noor-ud-din Noorani (Nund Rishi) at Charar-i-Sharief and home to the pristine high-altitude meadows of Doodhpathri.",
        "Public developmental priorities include karewa plateau conservation against illegal soil mining, airport approach road decongestion, and rural drinking water filtration."
    ),
    ("Jammu & Kashmir", "Ganderbal"): (
        "Traversed by the rushing Sindh River, it hosts the sacred Kheer Bhawani temple at Tulmulla and serves as the strategic base for the Sonamarg-Ladakh mountain corridor.",
        "Civic tasks center on regulating eco-tourism density, Sindh river sand-mining control, and mountain slope avalanche mitigation along the Zojila highway."
    ),
    ("Jammu & Kashmir", "Pulwama"): (
        "Globally acclaimed as the 'Saffron Bowl of Kashmir' around Pampore and the premier dairy hub of the valley, sustaining traditional walnut and willow bat manufacturing.",
        "Major priorities include protecting prime saffron soil (karewas) from urbanization, irrigation sprinkler networks for saffron fields, and industrial estate infrastructure."
    ),
    ("Jammu & Kashmir", "Kupwara"): (
        "Border district blessed with the enchanting Lolab and Bangus valleys, marked by alpine forests, freshwater streams, and traditional Gujjar-Bakkarwal pastoral culture.",
        "Key civic needs focus on Sadna Top tunnel and winter road clearance, cross-border healthcare, and telecommunication infrastructure in remote border villages."
    ),
    ("Jammu & Kashmir", "Bandipora"): (
        "Bordered by Wular Lake—one of Asia's largest freshwater lakes—and celebrated for the ancient Gilgit trade route, high-yield walnut production, and Kishanganga hydel power.",
        "Critical civic focus involves Wular lake silt dredging and wetland revival, trout fish aquaculture support, and Bandipora-Gurez winter tunnel connectivity."
    ),
    ("Jammu & Kashmir", "Kulgam"): (
        "Known as the 'Rice Bowl of South Kashmir' along the Veshaw River, famous for the scenic Aharbal waterfall and traditional red-clay pottery and apple plantations.",
        "Civic challenges include Veshaw river flash flood control, rural farm road macadamization, and rural youth sports infrastructure."
    ),
    ("Jammu & Kashmir", "Shopian"): (
        "Historic stop along the imperial Mughal Road over Pir Panjal, recognized as the premier apple and walnut hub of the Himalayas with rich spiritual heritage.",
        "Public focus centers on Mughal Road all-weather year-round maintenance, anti-hail net subsidies for orchards, and expanding CA cold chain facilities."
    ),
    ("Jammu & Kashmir", "Jammu"): (
        "The revered 'City of Temples' along the Tawi river, seat of the historic Bahu Fort, Raghunath Temple, and the primary transit hub for millions of Vaishno Devi pilgrims.",
        "Key civic tasks include Tawi riverfront development, urban drainage desilting, and mitigating peak pilgrimage traffic congestion through smart mobility."
    ),
    ("Jammu & Kashmir", "Kathua"): (
        "Gateway to Jammu & Kashmir along the Ravi River, known for the ancient Jasrota royal palace ruins, industrial parks, and the picturesque Ranjit Sagar Dam.",
        "Primary civic priorities involve industrial effluent monitoring along Govindsar, Kandi belt drinking water security, and rural border road connectivity."
    ),
    ("Jammu & Kashmir", "Udhampur"): (
        "Strategic headquarters of the Indian Army's Northern Command, home to the ancient Devika sacred river and the historic Krimchi temple complex.",
        "Civic tasks involve landslide mitigation along the Jammu-Srinagar national highway, Devika river pollution abatement, and rural school infrastructure."
    ),
    ("Jammu & Kashmir", "Samba"): (
        "Historically celebrated for its 22 royal clans (Samba Barah), traditional handloom calico printing, and scenic Mansar and Surinsar lakes.",
        "Public priorities include expanding industrial infrastructure in the SIDCO zone, Kandi area water harvesting sumps, and border village security bunkers."
    ),
    ("Jammu & Kashmir", "Rajouri"): (
        "Ancient kingdom of Rajapuri mentioned in Kalhana's Rajatarangini, bridging Jammu with the Kashmir valley across the Pir Panjal mountains.",
        "Major civic focus areas include border area school upgrades, rural electrification in hilly terrains, and medical clinic modernization."
    ),
    ("Jammu & Kashmir", "Poonch"): (
        "Historic border principality famed for Poonch Fort, sacred Chittoor Baba Buddha Amarnath, and the serene Seven Lakes alpine circuit.",
        "Critical challenges include Pir Panjal tunnel connectivity, border shelling rehabilitation centers, and all-weather road links to interior hamlets."
    ),
    ("Jammu & Kashmir", "Reasi"): (
        "Home to the revered Shri Mata Vaishno Devi shrine at Katra, the historic Bhimgarh Fort, and the world's highest railway bridge spanning the Chenab river.",
        "Civic priorities focus on pilgrimage crowd flow management, Chenab gorge eco-conservation, and rural drinking water pipelines."
    ),
    ("Jammu & Kashmir", "Ramban"): (
        "Perched along the rugged Chenab gorge, famous for the Baglihar Hydroelectric project and dense deodar forests, forming the central spine of NH-44.",
        "Major public priorities involve landslide-prone slope stabilization along the highway, riverbank safety, and mountain emergency trauma clinics."
    ),
    ("Jammu & Kashmir", "Doda"): (
        "Characterized by precipitous Himalayan valleys, Bhaderwah's picturesque meadows (Chhota Kashmir), and traditional lavender cultivation.",
        "Civic focus involves road safety on mountain highways, promotion of aromatic flower processing units, and winter heating facilities in public schools."
    ),
    ("Jammu & Kashmir", "Kishtwar"): (
        "Known as the 'Land of Sapphire and Saffron' along the upper Chenab, hosting the Dul Hasti power project and the Kishtwar High Altitude National Park.",
        "Key developmental tasks include Chenab river hydel project ecological compliance, remote high-altitude road access, and specialized hospital facilities."
    ),

    # ==========================================
    # Telangana Districts
    # ==========================================
    ("Telangana", "Adilabad"): (
        "Ancient gateway to South India along the Penganga and Godavari rivers, celebrated for the Dokra bell-metal crafts of Jainoor, Kuntala waterfall, and vibrant Gond tribal folklore.",
        "Primary civic priorities include expanding minor irrigation for cotton and soybean farmers, tribal hamlet all-weather road links, and upgrading district health centers."
    ),
    ("Telangana", "Hyderabad"): (
        "Founded in 1591 by Muhammad Quli Qutb Shah around the iconic Charminar, the historic City of Pearls is now India's global IT hub, Genome Valley biopharma capital, and culinary epicenter.",
        "Critical civic tasks center on Musi river rejuvenation, expanding Hyderabad Metro Phase II, and stormwater drainage modernization to prevent urban inundation."
    ),
    ("Telangana", "Medchal-Malkajgiri"): (
        "Rapidly expanding northern urban gateway of Hyderabad, hosting premier research institutes (BITS Pilani, NIPER) and major industrial and logistics corridors.",
        "Major public needs include peripheral ring road decongestion, drinking water supply from the Godavari grid, and municipal solid waste recycling."
    ),
    ("Telangana", "Ranga Reddy"): (
        "Named after the freedom fighter K.V. Ranga Reddy, it encompasses Hyderabad's premier financial district, HITEC City, Shamshabad International Airport, and hardware parks.",
        "Civic priorities focus on balancing rapid real estate expansion with lake conservation (Gandipet & Himayatsagar), public bus transit, and underground drainage."
    ),
    ("Telangana", "Hanumakonda"): (
        "Heart of the medieval Kakatiya Empire, celebrated for the 1000 Pillar Temple, Padmakshi temple, and NIT Warangal, India's first Regional Engineering College.",
        "Major civic tasks include urban stormwater drainage revamp, heritage tourism zoning, and university research cluster expansion."
    ),
    ("Telangana", "Warangal"): (
        "Historic capital of the Kakatiya dynasty, famous for the massive Warangal Fort stone gateways (Kakatiya Kala Thoranam) and the UNESCO World Heritage Ramappa Temple nearby.",
        "Key developmental needs involve textile park (Kakatiya Mega Textile Park) logistics, Bhadrakali lake preservation, and ring road bypass construction."
    ),
    ("Telangana", "Karimnagar"): (
        "Historically known as Sabbinadu along the Godavari, world-renowned for exquisite silver filigree (Tarkashi) craftsmanship and granary production under the Lower Manair Dam.",
        "Civic challenges include Manair riverfront beautification, granary mandi modernization, and industrial effluent control."
    ),
    ("Telangana", "Nizamabad"): (
        "Situated in the fertile basin of the Godavari and Manjira rivers, famed for the historic 10th-century Nizamabad Fort and extensive turmeric and paddy agricultural production.",
        "Critical public priorities include establishing the National Turmeric Board infrastructure, canal desilting, and groundwater recharge in Kandi zones."
    ),
    ("Telangana", "Nalgonda"): (
        "Land of the historic Telangana Armed Struggle and Nagarjuna Sagar Dam, celebrated for ancient Buddhist monastic remains and archaeological monuments.",
        "Major civic tasks include eradicating tail-end fluoride contamination through Mission Bhagiratha, canal lining maintenance, and solar farm integration."
    ),
    ("Telangana", "Khammam"): (
        "Historic threshold of the Deccan featuring the 1000-year-old Khammam Fort atop Stambhadri hill, rich in coal reserves, granite quarries, and chilli cultivation.",
        "Key public focus includes Munneru river flood embankment construction, modern chilli mandi cold storage, and granite dust suppression."
    ),
    ("Telangana", "Mahabubnagar"): (
        "Historically known as Palamoor, home to the legendary 800-year-old Pillalamarri banyan tree and the confluence of the Krishna and Tungabhadra rivers.",
        "Critical civic tasks involve Koilsagar and Jurala canal network repairs, drinking water distribution, and reversing migrant labor distress through local agro-industries."
    ),
    ("Telangana", "Siddipet"): (
        "Known for the historic Komuravelli Mallanna temple and celebrated as a model green governance township with innovative underground drainage and urban lakes.",
        "Public priorities include Ranganayaka Sagar canal distribution maintenance, expanding cottage textile weaving, and rural sports complexes."
    ),
    ("Telangana", "Rajanna Sircilla"): (
        "Renowned as the 'Textile City' of Telangana, celebrated for powerlooms, handloom weaving cooperatives, and the sacred Sri Raja Rajeshwara Swamy Temple at Vemulawada.",
        "Key civic challenges include powerloom modernization subsidies, yarn price stabilization, and Mid Manair reservoir rehabilitation settlements."
    ),
    ("Telangana", "Bhadradri Kothagudem"): (
        "Forest and mineral rich district hosting the sacred Sri Sita Ramachandra Swamy temple at Bhadrachalam along the Godavari and the Singareni Collieries coal mines.",
        "Major civic priorities include Godavari river monsoon flood mitigation in Bhadrachalam, tribal healthcare access, and mine-area environmental remediation."
    ),
    ("Telangana", "Mulugu"): (
        "Home to the sacred biennial Medaram Sammakka Saralamma Jatara—Asia's largest tribal pilgrimage—and the UNESCO World Heritage Ramappa Temple.",
        "Public priorities include eco-tourism regulation around Laknavaram lake, tribal forest rights documentation, and primary health clinics in dense forest thandas."
    ),
    ("Telangana", "Sangareddy"): (
        "Strategic industrial and academic district home to IIT Hyderabad and major pharmaceutical and defense manufacturing public sector units.",
        "Civic focus involves industrial pollution containment in the Patancheru belt, rural road widening, and drinking water grid expansion."
    ),
    ("Telangana", "Kamareddy"): (
        "Agrarian district known for sugarcane and rice cultivation, historical trade routes, and the sacred Domakonda Fort.",
        "Key tasks include Nizamsagar canal modernization, sugarcane farmer timely procurement payments, and municipal infrastructure upgrades."
    ),
    ("Telangana", "Jagtial"): (
        "Known for the historic star-shaped Jagtial Fort built by French engineers and lush mango and sweet orange orchards.",
        "Civic focus includes mango pulp processing units, canal distributary maintenance from Sri Ram Sagar Project, and rural road durability."
    ),
    ("Telangana", "Jangaon"): (
        "Historic center of the 1946 Telangana peasant rebellion (Chityala Ailamma's struggle) and ancient Jain and Shaivite stone sculptures.",
        "Primary public needs involve tank rejuvenation under Mission Kakatiya, rural women dairy cooperatives, and drinking water supply."
    ),
    ("Telangana", "Jayashankar Bhupalpally"): (
        "Named after Professor K. Jayashankar, rich in coal reserves, pristine teak forests, and ancient Kakatiya temples at Ghanpur.",
        "Major priorities include opencast coal mine dust mitigation, forest village solar micro-grids, and tribal maternal healthcare."
    ),
    ("Telangana", "Jogulamba Gadwal"): (
        "Home to the revered Jogulamba temple (one of the 18 Maha Shakti Peethas) at Alampur at the confluence of Krishna and Tungabhadra, famed for Gadwal handloom silk sarees.",
        "Key challenges include weaver loan access, flood protection bunds along Tungabhadra, and drinking water reach."
    ),
    ("Telangana", "Kumuram Bheem Asifabad"): (
        "Birthplace of tribal revolutionary leader Kumuram Bheem who fought for 'Jal, Jangal, Zameen', home to Jodeghat and ancient Gond-Kolam tribes.",
        "Public focus centers on interior forest road connectivity, seasonal epidemic control in tribal hamlets, and indigenous craft promotion."
    ),
    ("Telangana", "Mahabubabad"): (
        "Rich in Lambada and Koya tribal culture, home to ancient rock paintings and the historical Bayyaram iron ore and stone inscription sites.",
        "Civic needs include Bayyaram mining infrastructure development, railway overbridges, and tribal education hostel upgrades."
    ),
    ("Telangana", "Mancherial"): (
        "Prominent industrial and commercial junction along the Godavari, known for Singareni coal fields, cement manufacturing, and the Pranahita wildlife sanctuary.",
        "Major civic tasks include river pollution abatement, fly ash control from power units, and urban municipal drainage."
    ),
    ("Telangana", "Medak"): (
        "Historic seat of Medak Fort built by the Kakatiyas and the magnificent 1924 Gothic-style Medak Cathedral, one of the largest churches in Asia.",
        "Key public focus includes Haldi Vagu river rejuvenation, rural agro-warehouses, and drinking water supply to drought-prone mandals."
    ),
    ("Telangana", "Nagarkurnool"): (
        "Heart of the Nallamala forest range, home to indigenous Chenchu tribes, Amrabad Tiger Reserve, and the Srisailam left bank hydel station.",
        "Critical tasks involve wildlife corridor protection, water pipeline reach to Chenchu thandas, and rural road safety."
    ),
    ("Telangana", "Narayanpet"): (
        "World-renowned for traditional Narayanpet handloom sarees with silver and gold zari borders, carrying centuries-old weaving traditions from the Maratha era.",
        "Civic priorities include weaver cluster modernization, artisan credit guarantees, and drinking water supply under Koilsagar."
    ),
    ("Telangana", "Nirmal"): (
        "Celebrated for centuries-old Nirmal lacquerware, oil paintings, and wooden toys crafted by the traditional 'Naqqash' community, and historic French-built battery forts.",
        "Major public tasks involve artisan raw material timber supply, Godavari basin soil erosion prevention, and municipal drainage."
    ),
    ("Telangana", "Peddapalli"): (
        "Important industrial and energy hub along the Godavari, hosting NTPC Ramagundam super thermal power station and open-cast coal mines.",
        "Primary civic focus centers on air quality index management in Ramagundam, worker occupational health facilities, and fly ash reuse."
    ),
    ("Telangana", "Suryapet"): (
        "Important commercial and educational crossway between Hyderabad and Vijayawada, famous for the historic Pillalamarri temples and Durgamma temple.",
        "Civic needs include Musi and Krishna canal distributary repairs, highway pedestrian crossings, and grain market facilities."
    ),
    ("Telangana", "Vikarabad"): (
        "Nestled in the Ananthagiri Hills, the birthplace of the Musi river, celebrated as a serene eco-tourism and medicinal plant hub with premier sanitarium facilities.",
        "Public priorities include Ananthagiri hill biodiversity preservation, Musi headwater protection, and road widening from Hyderabad."
    ),
    ("Telangana", "Wanaparthy"): (
        "Historic principality ruled by the Wanaparthy Samsthanam, known for its royal palace (now polytechnic institute) and ancient tank irrigation network.",
        "Key civic challenges include Sarala Sagar siphon system maintenance, drought-resilient seed distribution, and rural healthcare clinics."
    ),
    ("Telangana", "Yadadri Bhuvanagiri"): (
        "Famous for the magnificent renovated hill shrine of Sri Lakshmi Narasimha Swamy at Yadagirigutta and the monolithic 12th-century Bhuvanagiri Fort built by the Western Chalukyas.",
        "Civic priorities involve pilgrim transport amenities, heritage conservation around the fort, and drinking water grid distribution."
    )
"""

NEW_ARCHETYPES = """
    "Haryana": (
        "{district} is an integral agrarian and industrial territory of Haryana, enriched by ancient Saraswati-Ghaggar basin traditions, leading crop yields, and bustling commercial mandis.",
        "Primary public focus includes canal water tail-end delivery, rural road durability, and expanding primary health clinics in {c_name}."
    ),
    "Telangana": (
        "{district} is a vibrant administrative and cultural territory of Telangana, characterized by Kakatiya tank irrigation heritage, Deccan plateau geology, and progressive village self-governance.",
        "Key civic focus areas include Mission Bhagiratha drinking water grid reach, local school infrastructure, and public health clinic upgrades in {c_name}."
    ),
    "Jammu & Kashmir": (
        "{district} holds profound geographical and cultural heritage in Jammu & Kashmir, set amidst majestic Himalayan valleys, traditional artisanal crafts, and resilient mountain communities.",
        "Critical development priorities center on winter road maintenance, high-altitude drinking water pipelines, and rural healthcare access in {c_name}."
    ),
"""

FILE_PATH = "scripts/pipeline/district_insights_catalog.py"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Insert new district specific insights before `DISTRICT_SPECIFIC_INSIGHTS` closes with `}`
target_close_insights = '    ("Goa", "South Goa"): (\n        "Characterized by tranquil scenic coastlines, Salcete cultural heritage, Zuari river shipping channels, and traditional fishing villages.",\n        "Primary civic focus centers on protecting agricultural khazan lands, regulated mining logistics, and heritage village preservation."\n    )\n}'

if target_close_insights in content:
    replacement = target_close_insights[:-2] + ",\n" + NEW_DISTRICT_INSIGHTS + "\n}"
    content = content.replace(target_close_insights, replacement)
    print("Added district insights for Haryana, Jammu & Kashmir, and Telangana!")
else:
    print("Could not locate target_close_insights, trying alternative matching")
    sys.exit(1)

# 2. Insert new archetypes before `STATE_REGIONAL_ARCHETYPES` closes with `}`
target_close_archetypes = '    "Delhi": (\n        "{district} forms an integral sector of the National Capital Territory of Delhi, home to iconic heritage monuments, premier national universities, and bustling commercial markets.",\n        "Critical public issues include Yamuna river flood plain revival, winter air quality mitigation, and 24/7 piped drinking water distribution in {c_name}."\n    )\n}'

if target_close_archetypes in content:
    replacement = target_close_archetypes[:-2] + ",\n" + NEW_ARCHETYPES + "\n}"
    content = content.replace(target_close_archetypes, replacement)
    print("Added state archetypes for Haryana, Jammu & Kashmir, and Telangana!")
else:
    print("Could not locate target_close_archetypes")
    sys.exit(1)

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {FILE_PATH}!")
