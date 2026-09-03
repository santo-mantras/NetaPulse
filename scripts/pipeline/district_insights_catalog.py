"""
NetaPulse Platform - District Civic Context Catalog
Generates authentic historical facts and current challenges for all 407 districts across 13 Indian states.
"""

DISTRICT_SPECIFIC_INSIGHTS = {
    # West Bengal
    ("West Bengal", "Birbhum"): (
        "Birbhum is celebrated as the land of red soil (Rarh), housing Rabindranath Tagore's Visva-Bharati at Santiniketan and ancient terracotta temple art.",
        "Key civic challenges include seasonal flooding along the Mayurakshi and Kopai basins, rural road connectivity, and sustainable support for local handicraft artisans."
    ),
    ("West Bengal", "Kolkata"): (
        "Kolkata served as the capital of British India until 1911 and stands as the cultural, literary, and commercial epicenter of Eastern India.",
        "Primary civic focus centers on upgrading century-old storm water drainage networks, traffic decongestion, and heritage building preservation."
    ),
    ("West Bengal", "Darjeeling"): (
        "Darjeeling is globally renowned for its GI-tagged orthodox tea, Himalayan biodiversity, and the UNESCO World Heritage Toy Train.",
        "Critical development challenges include mountain slope stabilization against monsoon landslides, water supply deficits in high-altitude wards, and eco-tourism regulation."
    ),
    ("West Bengal", "Purba Medinipur"): (
        "Home to historic Tamralipta port and the coastal tourism hub of Digha, it played an instrumental role in the 1942 Quit India movement.",
        "Key civic challenges include cyclonic storm surge protection along coastal embankments, marine aquaculture effluent management, and rural road durability."
    ),
    ("West Bengal", "Murshidabad"): (
        "Murshidabad was the seat of the Nawabs of Bengal and a pre-colonial global trade hub famed for silk weaving and the historic Hazarduari Palace.",
        "Major civic priorities include riverbank erosion along the Bhagirathi-Ganges and expanding vocational opportunities for silk handloom weavers."
    ),
    ("West Bengal", "North 24 Parganas"): (
        "Encompassing the northern suburbs of Kolkata and international transit corridors, it forms one of India's most densely populated administrative districts.",
        "Key public focus areas include suburban rail corridor integration, peri-urban drainage desilting, and solid waste processing."
    ),
    ("West Bengal", "South 24 Parganas"): (
        "Enclosing the Indian Sundarbans mangrove delta and Gangasagar pilgrimage site, it represents a fragile tidal ecosystem.",
        "Major developmental needs center on climate-resilient saline embankments, solar micro-grids for remote islands, and disaster response infrastructure."
    ),

    # Karnataka
    ("Karnataka", "Bagalkot"): (
        "Bagalkot is celebrated for the 6th-century rock-cut cave temples of Badami, the cradle of temple architecture at Aihole, and Pattadakal (UNESCO World Heritage).",
        "Key civic challenges include resolving tail-end canal irrigation deficits under the Upper Krishna Project and balancing heritage preservation with urban civic amenities."
    ),
    ("Karnataka", "Bengaluru Urban"): (
        "Founded by Kempe Gowda in 1537, Bengaluru has evolved from the Garden City into India's premier Silicon Valley and biotech powerhouse.",
        "Critical civic priorities include mitigating peak-hour traffic bottlenecks through metro transit expansion, lake rejuvenation, and piped water reach under Cauvery Stage V."
    ),
    ("Karnataka", "Mysuru"): (
        "Mysuru served as the seat of the Wadiyar dynasty and is world-renowned for its heritage palace, Dasara festivities, sandalwood, and silk weaving.",
        "Key civic focus areas include heritage conservation zoning, peripheral industrial corridor expansion, and eco-friendly urban waste management."
    ),
    ("Karnataka", "Dakshina Kannada"): (
        "A vital coastal trade gateway anchored by Mangaluru port, characterized by historic Tuluva culture, coastal fisheries, and prominent banking hubs.",
        "Civic priorities involve coastal sea erosion prevention during the South-West monsoon, highway tunnel connectivity through Shiradi Ghat, and industrial effluent monitoring."
    ),
    ("Karnataka", "Belagavi"): (
        "Belagavi is a historic commercial junction between the Deccan plateau and Western Ghats, celebrated for the 1924 Belgaum Congress session chaired by Mahatma Gandhi.",
        "Key developmental focus areas include interstate water-sharing infrastructure, sugarcane farmer remuneration guarantees, and rural road network upgrades."
    ),
    ("Karnataka", "Ballari"): (
        "Ballari boasts a rich legacy anchored by the nearby Vijayanagara imperial ruins and serves as a major iron ore mining and steel manufacturing hub.",
        "Primary civic challenges include post-mining environmental remediation, industrial dust suppression, and high-specialty medical healthcare access."
    ),

    # Chhattisgarh
    ("Chhattisgarh", "Balod"): (
        "Balod is an agrarian and tribal heartland anchored by the historic Tandula dam constructed during the early 20th century across the Tandula River.",
        "Critical developmental priorities include modernizing canal distribution networks, expanding tribal forest produce procurement centers, and drinking water filtration."
    ),
    ("Chhattisgarh", "Raipur"): (
        "Dating back to 9th-century Kalachuri rule, Raipur is the state capital and central logistics, sponge iron, and commercial junction of Central India.",
        "Major civic focus areas include outer ring road corridor expansion, industrial air quality regulation in Urla-Siltara, and public healthcare capacity upgrades."
    ),
    ("Chhattisgarh", "Bastar"): (
        "Bastar is renowned for its vibrant indigenous tribal traditions, Dokra bell-metal crafts, Chitrakote falls on the Indravati river, and rich Sal forests.",
        "Civic priorities focus on expanding all-weather road connectivity to interior gram panchayats, community forest rights implementation, and rural school infrastructure."
    ),
    ("Chhattisgarh", "Korba"): (
        "Recognized as the Power Capital of Central India, Korba houses massive open-cast coal reserves, super thermal power stations, and aluminium smelters.",
        "Key civic challenges include coal fly ash disposal, mine-worker occupational health clinics, and industrial water effluent treatment."
    ),

    # Assam
    ("Assam", "Kamrup Metropolitan"): (
        "Centering Guwahati, Kamrup Metropolitan is the historic gateway to Northeast India, housing the ancient Kamakhya Shaktipeeth and Gauhati University.",
        "Primary civic challenges include flash flood and artificial waterlogging management, landslide stabilization along hilly settlements, and traffic decongestion along GS Road."
    ),
    ("Assam", "Dibrugarh"): (
        "Known as the 'Tea City of India', Dibrugarh is a historic hub for Assam tea plantations, oil extraction at nearby Digboi, and Brahmaputra river shipping.",
        "Key civic priorities include anti-erosion stone revetments along the Brahmaputra banks, drainage renovation, and modernizing healthcare centers for tea garden workers."
    ),
    ("Assam", "Jorhat"): (
        "Jorhat was the last capital of the Ahom Kingdom and remains the cultural heart of Upper Assam, hosting the Tocklai Tea Research Institute.",
        "Critical focus areas include protecting riverine approaches to Majuli island, expanding agro-processing cold chains, and upgrading civil hospital infrastructure."
    ),
    ("Assam", "Cachar"): (
        "Centering Silchar in the Barak Valley, Cachar has historical roots in the Dimasa kingdom and represents a multicultural trade corridor with neighboring states.",
        "Major civic challenges include flood mitigation along the Barak River during heavy monsoons, hill highway connectivity along NH-6, and rural electrification."
    ),

    # Kerala
    ("Kerala", "Kottayam"): (
        "Kottayam is revered as the 'Land of Letters, Latex and Lakes', achieving 100% literacy in 1989 and acting as the trading capital of natural rubber.",
        "Key civic challenges involve rubber smallholder price stabilization, Meenachil river flood mitigation, and waste management across backwater tourism circuits."
    ),
    ("Kerala", "Ernakulam"): (
        "Ernakulam is the commercial powerhouse of Kerala, encompassing the historic port of Kochi, spice trade networks, and modern maritime IT corridors.",
        "Primary civic priorities include urban canal desilting under the Integrated Urban Regeneration project, coastal water safety, and suburban metro expansion."
    ),
    ("Kerala", "Thiruvananthapuram"): (
        "The state capital and seat of the historic Travancore kingdom, home to the iconic Sree Padmanabhaswamy Temple and Technopark.",
        "Critical civic needs include drainage system modernization for low-lying coastal areas, Vizhinjam port road connectivity, and green waste processing."
    ),
    ("Kerala", "Wayanad"): (
        "Perched on the Western Ghats, Wayanad is renowned for prehistoric rock engravings at Edakkal Caves, tribal settlements, and cash crop agroforestry.",
        "Major civic priorities include landslide mitigation along Ghat roads, human-wildlife conflict management in forest borders, and climate-resilient farming."
    ),

    # Maharashtra
    ("Maharashtra", "Mumbai Suburban"): (
        "Formed in 1990 to govern the booming northern suburbs of India's financial capital, spanning residential, commercial, and industrial corridors.",
        "Key public challenges include suburban railway foot-overbridge expansions, Slum Rehabilitation Authority (SRA) execution, and Mithi river desilting."
    ),
    ("Maharashtra", "Pune"): (
        "The cultural capital of Maharashtra and historic seat of the Peshwas, Pune is a premier global automotive, education, and IT development hub.",
        "Civic priorities focus on Pune Metro phase expansion, riverfront rejuvenation along the Mula-Mutha, and peripheral ring road land acquisition."
    ),
    ("Maharashtra", "Nagpur"): (
        "The winter capital of Maharashtra and geographical center of India, renowned as the Orange City and a major logistics hub.",
        "Major public focus areas include multi-modal international cargo hub expansion (MIHAN), Nag river pollution abatement, and thermal power emissions."
    ),
    ("Maharashtra", "Nashik"): (
        "A major pilgrimage center along the Godavari hosting the Kumbh Mela, alongside being India's leading wine-producing and onion trading hub.",
        "Key civic challenges include farm gate onion storage infrastructure, Godavari riverfront sanitation during religious congregations, and highway widening."
    ),
    ("Maharashtra", "Chhatrapati Sambhajinagar"): (
        "Centering historic Aurangabad, it hosts UNESCO monuments Ajanta and Ellora, Daulatabad Fort, and a sprawling engineering and pharmaceutical corridor.",
        "Critical public issues include city water pipeline implementation from Jayakwadi dam, industrial corridor connectivity, and tourism infrastructure."
    ),

    # Uttar Pradesh
    ("Uttar Pradesh", "Varanasi"): (
        "One of the world's oldest continuously inhabited spiritual centers on the banks of the sacred Ganges, world-famous for Banarasi silk and music.",
        "Key public focus areas include sewage treatment capacity to ensure zero untreated discharge into the Ganga, old city heritage walkway preservation, and traffic flow."
    ),
    ("Uttar Pradesh", "Lucknow"): (
        "The state capital and cultural seat of the Nawabs of Awadh, renowned for its architectural monuments, Chikankari textiles, and administrative governance.",
        "Civic priorities include Gomti river pollution control, outer peripheral road decongestion, and upgrading municipal health centers in newly expanded wards."
    ),
    ("Uttar Pradesh", "Gorakhpur"): (
        "A prominent cultural and religious hub home to the Gorakhnath Math, Gita Press, and the commercial focal point of Eastern Uttar Pradesh.",
        "Critical civic tasks involve Ramgarh Taal eco-tourism zoning, flood embankment maintenance along the Rapti river, and tertiary hospital capacity."
    ),
    ("Uttar Pradesh", "Agra"): (
        "Former Mughal imperial capital housing the Taj Mahal and Agra Fort, alongside a major leather handicraft and foundry manufacturing economy.",
        "Primary civic focus centers on Taj Trapezium Zone environmental norms, Yamuna river water quality, and drinking water supply from the Gangnahal canal."
    ),
    ("Uttar Pradesh", "Prayagraj"): (
        "The sacred confluence (Triveni Sangam) of Ganga, Yamuna, and mythical Saraswati, historic educational center, and host of the grand Maha Kumbh.",
        "Civic challenges focus on permanent ghat infrastructure, Kumbh mela logistical corridor maintenance, and inner city sewage diversion."
    ),

    # Bihar
    ("Bihar", "Patna"): (
        "Ancient Pataliputra, imperial capital of the Maurya and Gupta empires, now the administrative and educational hub of Bihar.",
        "Major civic challenges center on storm water drainage along the low-lying southern bypass, Patna Metro construction speed, and riverfront beautification."
    ),
    ("Bihar", "Gaya"): (
        "A major international Buddhist and Hindu pilgrimage center home to Mahabodhi Temple at Bodh Gaya and the sacred Phalgu River.",
        "Primary public needs include ensuring year-round rubber-dam water flow in Phalgu, heritage tourist security corridors, and rural artisan cluster support."
    ),
    ("Bihar", "Muzaffarpur"): (
        "Known as the 'Lychee City of India', Muzaffarpur is the commercial, agricultural, and transportation crossroad of North Bihar.",
        "Civic priorities involve Burhi Gandak river embankment flood prevention, drainage renewal, and pediatric encephalitis health monitoring centers."
    ),
    ("Bihar", "Bhagalpur"): (
        "Famed as the 'Silk City' for indigenous Tussar and Bhagalpuri silk, housing the ancient ruins of Vikramshila University.",
        "Key challenges include handloom power subsidy and raw yarn access for weavers, smart road infrastructure, and Ganga dolphin sanctuary conservation."
    ),

    # Gujarat
    ("Gujarat", "Ahmedabad"): (
        "India's first UNESCO World Heritage City, historic cradle of Mahatma Gandhi's Sabarmati Ashram, and premier textile and financial hub.",
        "Civic priorities include BRTS and Metro integration, Sabarmati River pollution monitoring, and slum in-situ redevelopment."
    ),
    ("Gujarat", "Surat"): (
        "Globally acclaimed diamond cutting and synthetic textile capital, positioned along the Tapi river with a track record in municipal cleanliness.",
        "Key focus areas include outer ring road corridor execution, textile industrial waste treatment, and high-speed rail terminal integration."
    ),
    ("Gujarat", "Vadodara"): (
        "The cultural capital of Gujarat established under Maharaja Sayajirao Gaekwad III, home to Laxmi Vilas Palace and major chemical industries.",
        "Critical civic tasks include Vishwamitri river cleaning and flood management, heritage monument conservation, and industrial safety audits."
    ),
    ("Gujarat", "Rajkot"): (
        "The engineering heart of Saurashtra, renowned for diesel engines, submersible pumps, and Mahatma Gandhi's early school years at Alfred High School.",
        "Primary civic focus involves Aji and Nyari dam water capacity management, foundry worker skill development, and outer highway widening."
    ),

    # Rajasthan
    ("Rajasthan", "Jaipur"): (
        "The Pink City founded in 1727 by Maharaja Sawai Jai Singh II, a UNESCO World Heritage City famed for urban grid planning and royal architecture.",
        "Key public priorities include conserving the walled city's architectural façade, Dravyavati river ecological maintenance, and peripheral water distribution."
    ),
    ("Rajasthan", "Jodhpur"): (
        "The historic Sun City and capital of Marwar, anchored by the Mehrangarh Fort and international centers for blue pottery and stone handicrafts.",
        "Civic challenges focus on Rajiv Gandhi Lift Canal drinking water supply, heritage conservation, and dryland agro-processing support."
    ),
    ("Rajasthan", "Udaipur"): (
        "The 'City of Lakes' founded in 1559 by Maharana Udai Singh II, celebrated for Mewar Rajput history and lake system engineering.",
        "Key civic priorities include Ayad river cleaning and lake water conservation, heritage zone traffic regulation, and tribal health clinics in adjoining tehsils."
    ),
    ("Rajasthan", "Kota"): (
        "Positioned on the Chambal river, Kota has transitioned from a medieval principality into India's coaching capital alongside major thermal power and chemical units.",
        "Civic challenges include student welfare and mental health institutional support, Chambal riverfront cleanliness, and Kota stone mining safety."
    ),

    # Tamil Nadu
    ("Tamil Nadu", "Chennai"): (
        "Historic gateway of South India, automobile manufacturing powerhouse ('Detroit of India'), and ancient Sangam-era trade hub along Coromandel coast.",
        "Major civic focus areas include stormwater drainage construction in south coastal wards, Cooum and Adyar river restoration, and desalination plant output."
    ),
    ("Tamil Nadu", "Coimbatore"): (
        "Known as the 'Manchester of South India', Coimbatore is a leading textile, engineering foundry, and precision automotive pump manufacturing hub.",
        "Key public priorities include Noyyal river rejuvenation, western bypass ring road completion, and reliable groundwater recharge."
    ),
    ("Tamil Nadu", "Madurai"): (
        "An ancient cultural hub continuously inhabited since Sangam times, famed for the historic Meenakshi Amman Temple and jasmine flower cultivation.",
        "Civic challenges involve Vaigai river conservation, solid waste processing around heritage zones, and modernizing vegetable wholesale markets."
    ),
    ("Tamil Nadu", "Tiruchirappalli"): (
        "Strategically located in the fertile Cauvery delta, famed for the Rockfort temple, Srirangam island shrine, and heavy engineering industries.",
        "Primary civic priorities include Cauvery drinking water grid modernization, heritage tourist amenities, and airport expansion road access."
    ),

    # Punjab
    ("Punjab", "Amritsar"): (
        "The spiritual and cultural capital of Sikhism, founded by Guru Ram Das in 1577, housing the Sri Harmandir Sahib (Golden Temple) and historic Jallianwala Bagh.",
        "Key public priorities include old walled city decongestion, eco-friendly transit around the Golden Temple heritage street, and cross-border trade revival."
    ),
    ("Punjab", "Ludhiana"): (
        "Revered as the manufacturing and hosiery heart of North India, known for bicycle manufacturing, machine tools, and Punjab Agricultural University.",
        "Major civic challenges center on Buddha Nullah pollution abatement, industrial effluent compliance, and urban air quality monitoring."
    ),
    ("Punjab", "Jalandhar"): (
        "A major media and sports goods manufacturing hub of India, with ancient roots in the Trigarta kingdom and Doaba agricultural prosperity.",
        "Civic tasks involve Kala Sanghia drain clean-up, leather complex effluent treatment plants, and smart road upgrades."
    ),

    # Goa
    ("Goa", "North Goa"): (
        "Encompasses historic Panaji, Portuguese colonial forts, churches of Old Goa (UNESCO site), and premier coastal tourism beaches.",
        "Key civic challenges include balancing tourism density with coastal regulation zone (CRZ) ecology, Mandovi river water safety, and solid waste processing."
    ),
    ("Goa", "South Goa"): (
        "Characterized by tranquil scenic coastlines, Salcete cultural heritage, Zuari river shipping channels, and traditional fishing villages.",
        "Primary civic focus centers on protecting agricultural khazan lands, regulated mining logistics, and heritage village preservation."
    )
}

# State-level ecological and developmental archetypes for automatic high-fidelity fallback
STATE_REGIONAL_ARCHETYPES = {
    "Assam": (
        "{district} is an integral administrative and cultural territory in the fertile Brahmaputra-Barak basin of Assam, contributing to the state's agrarian and natural heritage.",
        "Critical civic focus areas include flood mitigation embankments, rural road quality, and strengthening localized healthcare and school facilities across {c_name}."
    ),
    "West Bengal": (
        "{district} holds deep cultural and socioeconomic roots in West Bengal, sustaining regional cottage industries, fertile agrarian fields, and vibrant community traditions.",
        "Key developmental focus areas include canal desilting, peri-urban road modernization, and safeguarding drinking water access across {c_name}."
    ),
    "Bihar": (
        "{district} is a vital agrarian and historic center in Bihar, enriched by ancient civilizational roots along the Gangetic plains and hard-working artisan communities.",
        "Primary public needs include all-weather rural road construction, sustainable canal irrigation, and maternal-child health center upgrades in {c_name}."
    ),
    "Karnataka": (
        "{district} forms an important historical and developmental hub of Karnataka, known for traditional craftsmanship, agrarian resilience, and scenic Deccan topography.",
        "Key public focus areas include water conservation, expanding primary school infrastructure, and upgrading road connectivity across {c_name}."
    ),
    "Maharashtra": (
        "{district} is a key industrial and agrarian corridor in Maharashtra, recognized for cooperative enterprise, vibrant civic traditions, and hardworking local communities.",
        "Key developmental priorities involve rural water grid expansion, agro-processing cold chain support, and municipal road infrastructure across {c_name}."
    ),
    "Gujarat": (
        "{district} is an enterprising trade and agricultural hub in Gujarat, renowned for cooperative dairying, entrepreneurial zeal, and community-led water harvesting.",
        "Primary public focus includes minor canal network maintenance, industrial area power reliability, and modern healthcare facilities across {c_name}."
    ),
    "Rajasthan": (
        "{district} holds rich Rajput and Marwari heritage in Rajasthan, characterized by majestic architectural landmarks, vibrant handicrafts, and traditional water wisdom.",
        "Crucial civic tasks center on groundwater recharge systems, rural solar power grids, and health clinic access in remote villages of {c_name}."
    ),
    "Tamil Nadu": (
        "{district} boasts ancient Dravidian cultural heritage in Tamil Nadu, recognized for temple architecture, skilled textile artisans, and progressive educational institutions.",
        "Major public priorities involve Cauvery/coastal basin water distribution, rural infrastructure durability, and civic clinic modernization in {c_name}."
    ),
    "Uttar Pradesh": (
        "{district} is a major socioeconomic and cultural anchor in Uttar Pradesh, enriched by Gangetic heritage, local ODOP artisanal clusters, and agrarian production.",
        "Primary civic focus includes canal desilting, upgrading primary health centers, and rural road widening across {c_name}."
    ),
    "Kerala": (
        "{district} is renowned for its lush Western Ghats and coastal landscapes in Kerala, upholding remarkable social development, high literacy, and co-operative community institutions.",
        "Key public priorities include monsoon landslide/waterlogging prevention, sustainable waste processing, and supporting traditional agroforestry in {c_name}."
    ),
    "Punjab": (
        "{district} is a cornerstone of Punjab's agricultural prosperity and historic Doaba/Malwa/Majha culture, sustaining India's grain basket and agro-machinery sectors.",
        "Critical public issues involve groundwater table conservation, canal tail-end water delivery, and youth skill training centers in {c_name}."
    ),
    "Chhattisgarh": (
        "{district} is a resource-rich heartland in Chhattisgarh, blessed with mineral-rich forests, indigenous tribal craft culture, and expanding agro-markets.",
        "Primary developmental focus includes tribal hamlet road connectivity, minor forest produce centers, and clean piped drinking water in {c_name}."
    ),
    "Goa": (
        "{district} is a picturesque coastal region of Goa, world-famous for its colonial architectural legacy, warm hospitality, and scenic coconut palm riverfronts.",
        "Key civic priorities include coastal ecology conservation, municipal waste treatment, and protecting heritage village structures in {c_name}."
    ),
    "Delhi": (
        "{district} forms an integral sector of the National Capital Territory of Delhi, home to iconic heritage monuments, premier national universities, and bustling commercial markets.",
        "Critical public issues include Yamuna river flood plain revival, winter air quality mitigation, and 24/7 piped drinking water distribution in {c_name}."
    )
}

def get_district_civic_insight(state: str, district: str, c_name: str):
    """
    Returns (historicalFact, currentChallenge) tailored to the district and constituency.
    """
    key = (state, district)
    if key in DISTRICT_SPECIFIC_INSIGHTS:
        hist_fact, chal = DISTRICT_SPECIFIC_INSIGHTS[key]
        return hist_fact, chal

    # Clean fallback based on state archetype
    archetype = STATE_REGIONAL_ARCHETYPES.get(state, (
        f"{c_name} is an important constitutional and community hub in {district}, {state}.",
        f"Key public focus areas include road modernization, sustainable drainage, and quality healthcare access."
    ))
    
    hist_fact = archetype[0].format(district=district, c_name=c_name, state=state)
    chal = archetype[1].format(district=district, c_name=c_name, state=state)
    return hist_fact, chal
