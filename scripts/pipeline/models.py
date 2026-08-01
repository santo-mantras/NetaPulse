from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class LocationHierarchy(BaseModel):
    stateLgdCode: int
    stateName: str
    districtLgdCode: int
    districtName: str
    assemblyConstituencyCode: str
    assemblyConstituencyName: str
    parliamentaryConstituencyCode: str
    parliamentaryConstituencyName: str
    crimeRate: Optional[str] = "N/A"
    literacyRate: Optional[int] = 0
    hospitalsCount: Optional[int] = 0
    govtSchoolsCount: Optional[int] = 0
    regionalInsight: Optional[dict] = None

class CandidateProfile(BaseModel):
    id: str
    name: str
    role: Literal['MLA', 'MP', 'Corporator']
    party: str
    photoUrl: str
    constituencyName: str
    attendancePercentage: int
    questionsAsked: int
    privateMemberBills: int
    declaredAssetsINR: int
    declaredLiabilitiesINR: int
    criminalCasesCount: int
    criminalCasesDetails: List[dict]
    education: str
    affidavitPdfUrl: str
    termsServed: Optional[int] = 1
    funFact: Optional[str] = "Information pending."
    politicalFact: Optional[str] = "Information pending."
    averages: Optional[dict] = {"attendance": 75, "questions": 30, "bills": 1}

class CampaignPromise(BaseModel):
    id: str
    title: str
    category: str
    status: Literal['Fulfilled', 'In Progress', 'Unfulfilled', 'Insufficient Data']
    declaredInManifesto: str
    verifiedOutcome: str
    sourceCitation: str

class NewsReport(BaseModel):
    id: str
    publisher: Literal['The Hindu', 'Times of India', 'Indian Express', 'Mint', 'Other']
    title: str
    summary: str
    url: str
    publishedDate: str
    category: Literal['Asset Growth', 'Court Case', 'Sting/Investigation', 'Local Activity']
    verificationStatus: Literal['Cross-Referenced with Affidavit', 'Under Review', 'Media Report']

class GovernanceData(BaseModel):
    locations: List[LocationHierarchy]
    candidates: List[CandidateProfile]
    promises: List[CampaignPromise]
    news: List[NewsReport]
