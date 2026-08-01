import realData from './realGovernanceData.json';
import type { LocationHierarchy, CandidateProfile, CampaignPromise, NewsReport } from '../types/governance';

export const mockLocations: LocationHierarchy[] = realData.locations as LocationHierarchy[];

export const mockCandidates: Record<string, CandidateProfile> = {};
(realData.candidates as CandidateProfile[]).forEach(c => {
    mockCandidates[c.id] = c;
});

export const mockPromises: Record<string, CampaignPromise[]> = {};
const allPromises = realData.promises as CampaignPromise[];
allPromises.forEach(p => {
    // extract candidate_id from p.id which is p_{state}_{i}_{idx} or similar.
    // wait, in compile.py: p_{candidate_id}_{i} -> p_c_{state}_{i}_{idx}
    const parts = p.id.split('_');
    const cid = `c_${parts[2]}_${parts[3]}`; 
    if (!mockPromises[cid]) mockPromises[cid] = [];
    mockPromises[cid].push(p);
});

export const mockNews: Record<string, NewsReport[]> = {};
const allNews = realData.news as NewsReport[];
allNews.forEach(n => {
    const parts = n.id.split('_');
    const cid = `c_${parts[2]}_${parts[3]}`; 
    if (!mockNews[cid]) mockNews[cid] = [];
    mockNews[cid].push(n);
});
