import type { CandidateProfile, CampaignPromise, NewsReport, LocationHierarchy } from '../types/governance';

export const mockLocations: LocationHierarchy[] = [
    {
        stateLgdCode: 27,
        stateName: 'Maharashtra',
        districtLgdCode: 519,
        districtName: 'Pune',
        assemblyConstituencyCode: 'AC-208',
        assemblyConstituencyName: 'Vadgaon Sheri',
        parliamentaryConstituencyCode: 'PC-34',
        parliamentaryConstituencyName: 'Pune',
        crimeRate: '4.2 incidents per 1k',
        literacyRate: 89,
        hospitalsCount: 24,
        govtSchoolsCount: 45,
        regionalInsight: {
            title: 'Pune: The Oxford of the East',
            historicalFact: 'Once the seat of the powerful Peshwas of the Maratha Empire, Pune emerged as the political center of India in the 18th century.',
            currentChallenge: 'Despite its booming IT and education sectors, rapid urbanization has severely strained local infrastructure, causing chronic water-logging and severe traffic congestion.'
        }
    },
    {
        stateLgdCode: 27,
        stateName: 'Maharashtra',
        districtLgdCode: 518,
        districtName: 'Mumbai Suburban',
        assemblyConstituencyCode: 'AC-176',
        assemblyConstituencyName: 'Vandre East',
        parliamentaryConstituencyCode: 'PC-29',
        parliamentaryConstituencyName: 'Mumbai North Central',
        crimeRate: '5.1 incidents per 1k',
        literacyRate: 92,
        hospitalsCount: 38,
        govtSchoolsCount: 60,
        regionalInsight: {
            title: 'Mumbai: The Financial Capital',
            historicalFact: 'Originally an archipelago of seven islands given to the British as a dowry in 1661, it grew into India\'s financial powerhouse.',
            currentChallenge: 'Extreme inequality characterizes this district. Soaring real estate prices force over 40% of the population to live in dense slums right next to glitzy corporate hubs like BKC.'
        }
    },
    {
        stateLgdCode: 7,
        stateName: 'Delhi',
        districtLgdCode: 93,
        districtName: 'New Delhi',
        assemblyConstituencyCode: 'AC-40',
        assemblyConstituencyName: 'New Delhi',
        parliamentaryConstituencyCode: 'PC-4',
        parliamentaryConstituencyName: 'New Delhi',
        crimeRate: '3.8 incidents per 1k',
        literacyRate: 86,
        hospitalsCount: 15,
        govtSchoolsCount: 30,
        regionalInsight: {
            title: 'Delhi: The Historic Capital',
            historicalFact: 'Continuously inhabited since the 6th century BC, Delhi has served as the capital of various empires, most notably the Delhi Sultanate and the Mughals.',
            currentChallenge: 'While it boasts top-tier administrative infrastructure, it consistently ranks as one of the most polluted capital cities globally, suffering from an annual winter smog crisis.'
        }
    },
    {
        stateLgdCode: 10,
        stateName: 'Bihar',
        districtLgdCode: 230,
        districtName: 'Patna',
        assemblyConstituencyCode: 'AC-181',
        assemblyConstituencyName: 'Digha',
        parliamentaryConstituencyCode: 'PC-30',
        parliamentaryConstituencyName: 'Patna Sahib',
        crimeRate: '7.4 incidents per 1k',
        literacyRate: 70,
        hospitalsCount: 12,
        govtSchoolsCount: 50,
        regionalInsight: {
            title: 'Patna: The Ancient Pataliputra',
            historicalFact: 'Patna (Pataliputra) was the majestic capital of the Maurya and Gupta Empires, ruling almost the entire Indian subcontinent at its peak.',
            currentChallenge: 'Despite its glorious past, today it struggles with significant under-performance in industrial growth, high youth unemployment, and infrastructure deficits compared to national averages.'
        }
    }
];

export const mockCandidates: Record<string, CandidateProfile> = {
    'c1': {
        id: 'c1',
        name: 'Rajesh Kumar',
        role: 'MLA',
        party: 'XYZ Party',
        photoUrl: 'https://i.pravatar.cc/150?u=rajesh',
        constituencyName: 'AC-208 Vadgaon Sheri',
        attendancePercentage: 88,
        attendanceBody: 'State Assembly',
        averages: {
            attendance: 75,
            questions: 35,
            bills: 1
        },
        questionsAsked: 42,
        privateMemberBills: 2,
        declaredAssetsINR: 142000000,
        declaredLiabilitiesINR: 11000000,
        criminalCasesCount: 1,
        criminalCasesDetails: [
            {
                charges: 'Defamation (IPC 499)',
                caseNumber: 'CR-2019/45',
                status: 'Pending Trial'
            }
        ],
        education: 'B.A. Political Science',
        affidavitPdfUrl: 'https://affidavit.eci.gov.in/show-affidavit/1/2/3/4',
        funFact: 'First MLA to ride a bicycle to the assembly sessions for an entire year.',
        politicalFact: 'Has never lost a local body or assembly election since 2014.',
        termsServed: 3
    },
    'c2': {
        id: 'c2',
        name: 'Sunita Sharma',
        role: 'MLA',
        party: 'ABC Party',
        photoUrl: 'https://i.pravatar.cc/150?u=sunita',
        constituencyName: 'AC-208 Vadgaon Sheri',
        attendancePercentage: 95,
        attendanceBody: 'State Assembly',
        averages: {
            attendance: 75,
            questions: 35,
            bills: 1
        },
        questionsAsked: 85,
        privateMemberBills: 5,
        declaredAssetsINR: 45000000,
        declaredLiabilitiesINR: 2000000,
        criminalCasesCount: 0,
        criminalCasesDetails: [],
        education: 'LL.B.',
        affidavitPdfUrl: 'https://affidavit.eci.gov.in/show-affidavit/1/2/3/5',
        funFact: 'Holds a black belt in Karate and runs self-defense camps for women.',
        politicalFact: 'Switched parties right before the 2019 elections and won by a record margin.',
        termsServed: 1
    }
};

export const mockPromises: Record<string, CampaignPromise[]> = {
    'c1': [
        {
            id: 'p1',
            title: '24/7 Water Supply in Kalyani Nagar',
            category: 'Infrastructure',
            status: 'In Progress',
            declaredInManifesto: 'We will ensure uninterrupted water supply to all societies in Kalyani Nagar within 2 years.',
            verifiedOutcome: 'Pipeline laying started, but supply is currently restricted to 4 hours/day.',
            sourceCitation: 'Pune Municipal Corporation Audit Report 2023'
        },
        {
            id: 'p2',
            title: 'New Metro Station Feeder Bus',
            category: 'Transport',
            status: 'Unfulfilled',
            declaredInManifesto: 'Launch 50 free feeder buses to the new Metro station.',
            verifiedOutcome: 'No buses launched yet. Tender canceled in 2022.',
            sourceCitation: 'RTI Response - PMPML, Nov 2023'
        },
        {
            id: 'p3',
            title: 'Setup 5 Mohalla Clinics',
            category: 'Health',
            status: 'Fulfilled',
            declaredInManifesto: 'Will establish 5 fully functional mohalla clinics with free medicines.',
            verifiedOutcome: 'All 5 clinics inaugurated and currently treating an average of 100 patients daily.',
            sourceCitation: 'State Health Dept Gazette 2023'
        }
    ],
    'c2': [
         {
            id: 'p4',
            title: 'Improve Government School Infrastructure',
            category: 'Education',
            status: 'Fulfilled',
            declaredInManifesto: 'Digital classrooms in all 15 Govt schools in constituency.',
            verifiedOutcome: 'Smart boards installed in 14 out of 15 schools.',
            sourceCitation: 'Education Dept Survey 2023'
        }
    ]
};

export const mockNews: Record<string, NewsReport[]> = {
    'c1': [
        {
            id: 'n1',
            publisher: 'Mint',
            title: 'Asset audit shows +140% net-worth growth (2019-2024)',
            summary: 'A recent independent audit highlights a massive surge in the MLA\'s immovable assets over a single term.',
            url: 'https://www.livemint.com',
            publishedDate: '12 Jan 2024',
            category: 'Asset Growth',
            verificationStatus: 'Cross-Referenced with Affidavit'
        },
        {
            id: 'n2',
            publisher: 'The Hindu',
            title: 'Defamation Case Hearing Postponed Again',
            summary: 'The defamation case filed against the leader by a rival party member has been pushed to next month.',
            url: 'https://www.thehindu.com',
            publishedDate: '05 Mar 2024',
            category: 'Court Case',
            verificationStatus: 'Media Report'
        }
    ]
};
