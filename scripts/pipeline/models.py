from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict, Any

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
    role: str
    party: str
    photoUrl: str
    constituencyName: str
    state: str
    attendancePercentage: int
    attendanceBody: Optional[str] = "State Assembly"
    questionsAsked: int
    privateMemberBills: int
    declaredAssetsINR: int
    declaredLiabilitiesINR: int
    criminalCasesCount: int
    criminalCasesDetails: List[dict]
    education: str
    affidavitPdfUrl: str
    termsServed: Optional[int] = 1
    funFact: Optional[str] = None
    politicalFact: Optional[str] = None
    bio: Optional[str] = None
    partyHistory: Optional[List[Dict[str, Any]]] = None
    partyLogoUrl: Optional[str] = None
    averages: Optional[dict] = {"attendance": 75, "questions": 30, "bills": 1}

class CampaignPromise(BaseModel):
    id: str
    title: str
    category: str
    status: str
    declaredInManifesto: str
    verifiedOutcome: str
    sourceCitation: str

class NewsReport(BaseModel):
    id: str
    publisher: str
    title: str
    summary: str
    url: str
    publishedDate: str
    category: str
    verificationStatus: str

class GovernanceData(BaseModel):
    locations: List[LocationHierarchy]
    candidates: List[CandidateProfile]
    promises: List[CampaignPromise]
    news: List[NewsReport]
