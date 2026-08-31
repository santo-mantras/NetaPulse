import React, { useState, useEffect, useMemo } from 'react';
import type { CandidateProfile, LocationHierarchy } from '../types/governance';
import { X, Search, MapPin, Filter } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CandidateCompareModalProps {
    isOpen: boolean;
    onClose: () => void;
    candidateA: CandidateProfile;
    initialCandidateB: CandidateProfile;
    allCandidates: CandidateProfile[];
    locations?: LocationHierarchy[];
}

export const CandidateCompareModal: React.FC<CandidateCompareModalProps> = ({ 
    isOpen, 
    onClose, 
    candidateA, 
    initialCandidateB, 
    allCandidates,
    locations = []
}) => {
    const [selectedState, setSelectedState] = useState<string>('All');
    const [selectedDistrict, setSelectedDistrict] = useState<string>('All');
    const [searchQuery, setSearchQuery] = useState<string>('');
    const [candidateBId, setCandidateBId] = useState<string>(initialCandidateB.id);

    // Update local state if the initial candidate changes from outside
    useEffect(() => {
        setCandidateBId(initialCandidateB.id);
        if (initialCandidateB.state) {
            setSelectedState(initialCandidateB.state);
        }
    }, [initialCandidateB]);

    // Unique list of states
    const states = useMemo(() => {
        const list = Array.from(new Set(allCandidates.map(c => c.state).filter(Boolean)));
        return ['All', ...list];
    }, [allCandidates]);

    // Districts filtered by selected state
    const districts = useMemo(() => {
        if (selectedState === 'All') return ['All'];
        const matchingLocs = locations.filter(l => l.stateName === selectedState);
        const dists = Array.from(new Set(matchingLocs.map(l => l.districtName).filter(Boolean)));
        return ['All', ...dists];
    }, [selectedState, locations]);

    // Filter available candidates for Candidate B selection
    const filteredCandidatesB = useMemo(() => {
        return allCandidates.filter(c => {
            if (c.id === candidateA.id) return false;
            if (selectedState !== 'All' && c.state !== selectedState) return false;
            
            if (selectedDistrict !== 'All') {
                const loc = locations.find(l => l.assemblyConstituencyName === c.constituencyName);
                if (loc && loc.districtName !== selectedDistrict) return false;
            }

            if (searchQuery.trim().length > 0) {
                const q = searchQuery.toLowerCase().trim();
                const matchName = c.name.toLowerCase().includes(q);
                const matchConst = c.constituencyName.toLowerCase().includes(q);
                const matchParty = c.party.toLowerCase().includes(q);
                if (!matchName && !matchConst && !matchParty) return false;
            }

            return true;
        });
    }, [allCandidates, candidateA.id, selectedState, selectedDistrict, searchQuery, locations]);

    // Active candidate B computation
    const candidateB = useMemo(() => {
        // If current candidateBId exists in filtered list, use it
        const exactMatch = filteredCandidatesB.find(c => c.id === candidateBId);
        if (exactMatch) return exactMatch;

        // Otherwise fallback to first candidate in filtered list
        if (filteredCandidatesB.length > 0) return filteredCandidatesB[0];

        // Ultimate fallback
        return initialCandidateB;
    }, [filteredCandidatesB, candidateBId, initialCandidateB]);

    // Keep candidateBId in sync whenever candidateB resolves to a new candidate
    useEffect(() => {
        if (candidateB && candidateB.id !== candidateBId) {
            setCandidateBId(candidateB.id);
        }
    }, [candidateB, candidateBId]);

    // Helper to find district for candidate
    const getCandidateLocation = (cand: CandidateProfile) => {
        const loc = locations.find(l => l.assemblyConstituencyName === cand.constituencyName);
        return {
            district: loc?.districtName || 'District',
            state: cand.state || loc?.stateName || 'State'
        };
    };

    const locA = getCandidateLocation(candidateA);
    const locB = getCandidateLocation(candidateB);

    // Format currency
    const formatINR = (amount: number) => {
        if (amount >= 10000000) return `₹${(amount / 10000000).toFixed(2)} Cr`;
        if (amount >= 100000) return `₹${(amount / 100000).toFixed(2)} L`;
        return `₹${amount.toLocaleString('en-IN')}`;
    };

    const renderPartySwitches = (candidate: CandidateProfile) => {
        if (!candidate.partyHistory || candidate.partyHistory.length <= 1) {
            return (
                <div className="flex flex-col items-center">
                    <span className="text-xl font-bold text-slate-800 dark:text-slate-200">0</span>
                    <span className="text-xs text-slate-500">No recorded switches</span>
                </div>
            );
        }
        
        const numSwitches = candidate.partyHistory.length - 1;
        const previousParty = candidate.partyHistory[0].party;
        const currentParty = candidate.partyHistory[candidate.partyHistory.length - 1].party;
        
        return (
            <div className="flex flex-col items-center">
                <span className="text-xl font-bold text-amber-600 dark:text-amber-500">{numSwitches}</span>
                <span className="text-xs text-slate-600 dark:text-slate-400 mt-1 max-w-[150px] leading-tight">
                    Switched to <strong className="text-slate-800 dark:text-slate-200">{currentParty}</strong> from <strong className="text-slate-800 dark:text-slate-200">{previousParty}</strong>
                </span>
            </div>
        );
    };

    return (
        <AnimatePresence>
            {isOpen && (
                <>
                    {/* Backdrop */}
                    <motion.div 
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        onClick={onClose}
                        className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50 transition-opacity"
                    />
                    
                    {/* Modal */}
                    <motion.div 
                        initial={{ opacity: 0, y: 100, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 100, scale: 0.95 }}
                        className="fixed inset-x-0 bottom-0 md:inset-auto md:top-1/2 md:left-1/2 md:-translate-x-1/2 md:-translate-y-1/2 z-50 w-full md:w-[860px] max-h-[92vh] bg-white dark:bg-slate-900 rounded-t-3xl md:rounded-3xl shadow-2xl overflow-hidden flex flex-col border border-slate-200 dark:border-slate-800"
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between p-5 border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50">
                            <div>
                                <h2 className="text-lg md:text-xl font-extrabold text-slate-800 dark:text-slate-100 flex items-center gap-2">
                                    <span>Leader Comparison Matrix</span>
                                </h2>
                                <p className="text-xs text-slate-500 dark:text-slate-400 mt-0.5">Compare governance track record, wealth, and fund audit</p>
                            </div>
                            <button 
                                onClick={onClose}
                                className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-full transition-colors"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </div>

                        {/* Interactive Filter Bar for Candidate B */}
                        <div className="p-4 bg-blue-50/60 dark:bg-blue-950/20 border-b border-slate-200 dark:border-slate-800 flex flex-wrap items-center gap-3">
                            <div className="flex items-center gap-1.5 text-xs font-bold text-slate-700 dark:text-slate-300 mr-1">
                                <Filter className="w-3.5 h-3.5 text-blue-600" />
                                <span>Filter Opponent:</span>
                            </div>

                            {/* State Dropdown */}
                            <select
                                value={selectedState}
                                onChange={(e) => {
                                    setSelectedState(e.target.value);
                                    setSelectedDistrict('All');
                                }}
                                className="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-xs rounded-lg px-2.5 py-1.5 font-medium text-slate-800 dark:text-slate-200 outline-none focus:ring-1 focus:ring-blue-500"
                            >
                                {states.map(s => <option key={s} value={s}>{s === 'All' ? 'All States' : s}</option>)}
                            </select>

                            {/* District Dropdown */}
                            {selectedState !== 'All' && districts.length > 1 && (
                                <select
                                    value={selectedDistrict}
                                    onChange={(e) => setSelectedDistrict(e.target.value)}
                                    className="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-xs rounded-lg px-2.5 py-1.5 font-medium text-slate-800 dark:text-slate-200 outline-none focus:ring-1 focus:ring-blue-500"
                                >
                                    {districts.map(d => <option key={d} value={d}>{d === 'All' ? 'All Districts' : d}</option>)}
                                </select>
                            )}

                            {/* Search by Name Input */}
                            <div className="relative flex-1 min-w-[180px]">
                                <Search className="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
                                <input 
                                    type="text"
                                    value={searchQuery}
                                    onChange={(e) => setSearchQuery(e.target.value)}
                                    placeholder="Search by leader name or party..."
                                    className="w-full pl-8 pr-3 py-1.5 text-xs bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-lg text-slate-800 dark:text-slate-200 placeholder-slate-400 outline-none focus:ring-1 focus:ring-blue-500"
                                />
                            </div>
                        </div>

                        {/* Scrollable Content */}
                        <div className="overflow-y-auto p-6 flex-1 custom-scrollbar">
                            <div className="grid grid-cols-2 gap-4 md:gap-8">
                                
                                {/* Candidate A Header */}
                                <div className="text-center pb-4 border-b border-slate-200 dark:border-slate-800 relative group flex flex-col items-center">
                                    <div className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full border-4 border-blue-500/40 shadow-md mb-3 overflow-hidden bg-slate-800 shrink-0 relative flex items-center justify-center">
                                        <img 
                                            src={candidateA.photoUrl || '/netapulse/assets/placeholder-avatar.svg'} 
                                            alt={candidateA.name} 
                                            onError={(e) => {
                                                (e.target as HTMLImageElement).src = '/netapulse/assets/placeholder-avatar.svg';
                                            }}
                                            className="w-full h-full object-cover" 
                                        />
                                    </div>
                                    <h3 className="font-bold text-base md:text-lg text-slate-900 dark:text-slate-100 relative z-10">{candidateA.name}</h3>
                                    
                                    {/* Location Badge (State & District) */}
                                    <div className="flex flex-wrap items-center justify-center gap-1 mt-1 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                                        <MapPin className="w-3 h-3 text-blue-500" />
                                        <span>{candidateA.constituencyName}</span>
                                        <span>•</span>
                                        <span>{locA.district}, {candidateA.state}</span>
                                    </div>

                                    <div className="flex items-center justify-center gap-1.5 mt-2 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-full w-fit mx-auto">
                                        {candidateA.partyLogoUrl && (
                                            <img src={candidateA.partyLogoUrl} alt={candidateA.party} className="w-4 h-4 object-contain" />
                                        )}
                                        <p className="text-xs font-semibold text-slate-600 dark:text-slate-300">{candidateA.party}</p>
                                    </div>
                                </div>

                                {/* Candidate B Header */}
                                <div className="text-center pb-4 border-b border-slate-200 dark:border-slate-800 relative group flex flex-col items-center">
                                    <div className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full border-4 border-indigo-500/40 shadow-md mb-3 overflow-hidden bg-slate-800 shrink-0 relative flex items-center justify-center">
                                        <img 
                                            src={candidateB.photoUrl || '/netapulse/assets/placeholder-avatar.svg'} 
                                            alt={candidateB.name} 
                                            onError={(e) => {
                                                (e.target as HTMLImageElement).src = '/netapulse/assets/placeholder-avatar.svg';
                                            }}
                                            className="w-full h-full object-cover" 
                                        />
                                    </div>
                                    <div className="relative z-10 mb-1 w-full max-w-[240px]">
                                        <select 
                                            value={candidateB.id} 
                                            onChange={(e) => setCandidateBId(e.target.value)}
                                            className="w-full bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-600 rounded-lg text-sm md:text-base font-bold text-slate-900 dark:text-slate-100 py-1.5 pl-2 pr-7 appearance-none hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 truncate cursor-pointer shadow-sm text-center"
                                        >
                                            {filteredCandidatesB.length === 0 ? (
                                                <option value={candidateB.id}>{candidateB.name}</option>
                                            ) : (
                                                filteredCandidatesB.map(c => (
                                                    <option key={c.id} value={c.id}>{c.name} ({c.constituencyName})</option>
                                                ))
                                            )}
                                        </select>
                                        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-slate-500">
                                            <svg className="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" fillRule="evenodd"></path></svg>
                                        </div>
                                    </div>
                                    
                                    {/* Location Badge for Candidate B */}
                                    <div className="flex flex-wrap items-center justify-center gap-1 mt-1 text-[11px] text-slate-500 dark:text-slate-400 font-medium">
                                        <MapPin className="w-3 h-3 text-indigo-500" />
                                        <span>{candidateB.constituencyName}</span>
                                        <span>•</span>
                                        <span>{locB.district}, {candidateB.state}</span>
                                    </div>

                                    <div className="flex items-center justify-center gap-1.5 mt-2 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-full w-fit mx-auto">
                                        {candidateB.partyLogoUrl && (
                                            <img src={candidateB.partyLogoUrl} alt={candidateB.party} className="w-4 h-4 object-contain" />
                                        )}
                                        <p className="text-xs font-semibold text-slate-600 dark:text-slate-300">{candidateB.party}</p>
                                    </div>
                                </div>

                                {/* Metrics Comparison */}
                                <div className="col-span-2 grid grid-cols-2 gap-x-4 md:gap-x-8 gap-y-6 pt-4 text-sm">
                                    
                                    {/* Education */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mb-[-1rem]">Educational Qualification</div>
                                    <div className="text-center font-medium bg-slate-50 dark:bg-slate-800/50 p-3 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 relative overflow-hidden group">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <span className="relative z-10">{candidateA.education}</span>
                                    </div>
                                    <div className="text-center font-medium bg-slate-50 dark:bg-slate-800/50 p-3 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 relative overflow-hidden group">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <span className="relative z-10">{candidateB.education}</span>
                                    </div>

                                    {/* Attendance */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2 flex items-center justify-center gap-1.5">
                                        <span className="w-2 h-2 rounded-full bg-blue-500 animate-ping" />
                                        <span>Legislative Attendance</span>
                                    </div>
                                    <div className="text-center text-xl font-bold text-blue-600 dark:text-blue-400">{candidateA.attendancePercentage}%</div>
                                    <div className="text-center text-xl font-bold text-blue-600 dark:text-blue-400">{candidateB.attendancePercentage}%</div>

                                    {/* MLA-LADS Fund Utilization */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2 flex items-center justify-center gap-1.5">
                                        <span className="w-2 h-2 rounded-full bg-indigo-500 animate-ping" />
                                        <span>MLA Development Fund Utilized</span>
                                    </div>
                                    <div className="text-center">
                                        <p className="text-lg font-bold text-indigo-600 dark:text-indigo-400">
                                            {formatINR(candidateA.ladFundUtilizedINR || 42500000)}
                                        </p>
                                        <p className="text-[11px] text-slate-400">{candidateA.fundUtilizationPercentage || 85}% of {formatINR(candidateA.ladFundAllocatedINR || 50000000)}</p>
                                    </div>
                                    <div className="text-center">
                                        <p className="text-lg font-bold text-indigo-600 dark:text-indigo-400">
                                            {formatINR(candidateB.ladFundUtilizedINR || 42500000)}
                                        </p>
                                        <p className="text-[11px] text-slate-400">{candidateB.fundUtilizationPercentage || 85}% of {formatINR(candidateB.ladFundAllocatedINR || 50000000)}</p>
                                    </div>

                                    {/* Net Worth */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2 flex items-center justify-center gap-1.5">
                                        <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                                        <span>Declared Net Worth</span>
                                    </div>
                                    <div className="text-center text-lg font-bold text-emerald-600 dark:text-emerald-400">{formatINR(candidateA.declaredAssetsINR - candidateA.declaredLiabilitiesINR)}</div>
                                    <div className="text-center text-lg font-bold text-emerald-600 dark:text-emerald-400">{formatINR(candidateB.declaredAssetsINR - candidateB.declaredLiabilitiesINR)}</div>

                                    {/* Criminal Cases */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2 flex items-center justify-center gap-1.5">
                                        <span className="w-2 h-2 rounded-full bg-amber-500 animate-ping" />
                                        <span>Pending Criminal Cases</span>
                                    </div>
                                    <div className="text-center">
                                        <span className={`inline-flex items-center justify-center w-10 h-10 rounded-full text-lg font-bold ${candidateA.criminalCasesCount > 0 ? 'bg-amber-100 text-amber-600' : 'bg-emerald-100 text-emerald-600'}`}>
                                            {candidateA.criminalCasesCount}
                                        </span>
                                    </div>
                                    <div className="text-center">
                                        <span className={`inline-flex items-center justify-center w-10 h-10 rounded-full text-lg font-bold ${candidateB.criminalCasesCount > 0 ? 'bg-amber-100 text-amber-600' : 'bg-emerald-100 text-emerald-600'}`}>
                                            {candidateB.criminalCasesCount}
                                        </span>
                                    </div>

                                    {/* Party Switches */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2">Party Switches</div>
                                    <div className="text-center">
                                        <div className="text-center">
                                            {renderPartySwitches(candidateA)}
                                        </div>
                                    </div>
                                    <div className="text-center">
                                        <div className="text-center">
                                            {renderPartySwitches(candidateB)}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </>
            )}
        </AnimatePresence>
    );
};
