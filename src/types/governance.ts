export interface LocationHierarchy {
    stateLgdCode: number;
    stateName: string;
    districtLgdCode: number;
    districtName: string;
    assemblyConstituencyCode: string;
    assemblyConstituencyName: string;
    parliamentaryConstituencyCode: string;
    parliamentaryConstituencyName: string;
    crimeRate: string;
    literacyRate: number;
    hospitalsCount: number;
    govtSchoolsCount: number;
    regionalInsight: {
        title: string;
        historicalFact: string;
        currentChallenge: string;
    };
}

export interface CandidateProfile {
    id: string;
    name: string;
    role: 'MLA' | 'MP' | 'Corporator';
    party: string;
    photoUrl: string;
    constituencyName: string;
    attendancePercentage: number;
    attendanceBody: string;
    averages: {
        attendance: number;
        questions: number;
        bills: number;
    };
    questionsAsked: number;
    privateMemberBills: number;
    declaredAssetsINR: number;
    declaredLiabilitiesINR: number;
    criminalCasesCount: number;
    criminalCasesDetails: {
        charges: string;
        caseNumber: string;
        status: string;
    }[];
    education: string;
    affidavitPdfUrl: string;
    funFact: string;
    politicalFact: string;
    termsServed: number;
}

export interface CampaignPromise {
    id: string;
    title: string;
    category: string;
    status: 'Fulfilled' | 'In Progress' | 'Unfulfilled' | 'Insufficient Data';
    declaredInManifesto: string;
    verifiedOutcome: string;
    sourceCitation: string;
}

export interface NewsReport {
    id: string;
    publisher: 'The Hindu' | 'Times of India' | 'Indian Express' | 'Mint' | 'Other';
    title: string;
    summary: string;
    url: string;
    publishedDate: string;
    category: 'Asset Growth' | 'Court Case' | 'Sting/Investigation' | 'Local Activity';
    verificationStatus: 'Cross-Referenced with Affidavit' | 'Under Review' | 'Media Report';
}
