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
    districtStatsSources?: {
        crimeRateSource?: string;
        literacySource?: string;
        hospitalsSource?: string;
        schoolsSource?: string;
    };
}

export interface CandidateProfile {
    id: string;
    name: string;
    role: 'MLA' | 'MP' | 'Corporator';
    party: string;
    photoUrl: string;
    constituencyName: string;
    state: string;
    attendancePercentage: number;
    attendanceBody: string;
    averages: {
        attendance: number;
        questions: number;
        bills?: number;
        fundUtilization?: number;
        debates?: number;
    };
    questionsAsked: number;
    privateMemberBills?: number;
    fundSchemeName?: string;
    fundUtilizationPercentage?: number;
    ladFundAllocatedINR?: number;
    ladFundUtilizedINR?: number;
    ladFundUnspentINR?: number;
    worksRecommendedCount?: number;
    worksCompletedCount?: number;
    worksPendingCount?: number;
    fundSourceCitation?: string;
    ladFundCategoryBreakdown?: {
        category: string;
        percentage: number;
        allocatedINR: number;
        status?: 'Completed' | 'Under Implementation' | 'Pending Sanction';
    }[];
    debatesParticipated?: number;
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
    funFact?: string;
    politicalFact?: string;
    bio?: string;
    dataSources?: {
        affidavitSource?: string;
        attendanceSource?: string;
        questionsSource?: string;
        fundSource?: string;
    };
    partyLogoUrl?: string;
    partyHistory?: {
        party: string;
        yearJoined: number;
        yearLeft?: number;
    }[];
    termsServed: number;
}

export interface CampaignPromise {
    id: string;
    title: string;
    category: string;
    tier?: 'state_manifesto' | 'national_manifesto' | 'constituency_promise';
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
