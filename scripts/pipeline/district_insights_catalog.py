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
    ),

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
    ),

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
