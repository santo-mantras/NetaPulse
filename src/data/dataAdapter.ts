import realData from './realGovernanceData.json';
import type { LocationHierarchy, CandidateProfile, CampaignPromise, NewsReport } from '../types/governance';

export const mockLocations: LocationHierarchy[] = realData.locations as unknown as LocationHierarchy[];

export const mockCandidates: Record<string, CandidateProfile> = {};
(realData.candidates as unknown as CandidateProfile[]).forEach(c => {
    mockCandidates[c.id] = c;
});

export const mockPromises: Record<string, CampaignPromise[]> = {};
const allPromises = realData.promises as CampaignPromise[];
allPromises.forEach(p => {
    // Robust extraction: e.g. "mh_1_prom_1" -> "mh_1", "up_25_prom_3" -> "up_25"
    const match = p.id.match(/^([a-z]+_\d+)_prom_/i);
    const cid = match ? match[1] : p.id.substring(0, p.id.lastIndexOf('_prom_'));
    if (cid) {
        if (!mockPromises[cid]) mockPromises[cid] = [];
        mockPromises[cid].push(p);
    }
});

export const mockNews: Record<string, NewsReport[]> = {};
const allNews = realData.news as NewsReport[];
allNews.forEach(n => {
    // Robust extraction: e.g. "mh_1_news_1" -> "mh_1", "ka_12_news_2" -> "ka_12"
    const match = n.id.match(/^([a-z]+_\d+)_news_/i);
    const cid = match ? match[1] : n.id.substring(0, n.id.lastIndexOf('_news_'));
    if (cid) {
        if (!mockNews[cid]) mockNews[cid] = [];
        mockNews[cid].push(n);
    }
});

export const mockStateProfiles: Record<string, any> = (realData as any).stateProfiles || {};
