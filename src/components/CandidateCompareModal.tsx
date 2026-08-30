import React, { useState, useEffect } from 'react';
import type { CandidateProfile } from '../types/governance';
import { X, User } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CandidateCompareModalProps {
    isOpen: boolean;
    onClose: () => void;
    candidateA: CandidateProfile;
    initialCandidateB: CandidateProfile;
    availableCandidates: CandidateProfile[];
}

export const CandidateCompareModal: React.FC<CandidateCompareModalProps> = ({ isOpen, onClose, candidateA, initialCandidateB, availableCandidates }) => {
    const [candidateBId, setCandidateBId] = useState(initialCandidateB.id);
    
    // Update local state if the initial candidate changes from outside
    useEffect(() => {
        setCandidateBId(initialCandidateB.id);
    }, [initialCandidateB.id]);

    const candidateB = availableCandidates.find(c => c.id === candidateBId) || initialCandidateB;

    
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
                        className="fixed inset-0 z-40 bg-slate-900/60 backdrop-blur-sm"
                    />
                    
                    {/* Modal */}
                    <motion.div 
                        initial={{ opacity: 0, y: 100, scale: 0.95 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: 100, scale: 0.95 }}
                        className="fixed inset-x-0 bottom-0 md:inset-auto md:top-1/2 md:left-1/2 md:-translate-x-1/2 md:-translate-y-1/2 z-50 w-full md:w-[800px] max-h-[90vh] bg-white dark:bg-slate-900 rounded-t-3xl md:rounded-3xl shadow-2xl overflow-hidden flex flex-col border border-slate-200 dark:border-slate-800"
                    >
                        {/* Header */}
                        <div className="flex items-center justify-between p-6 border-b border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/50">
                            <h2 className="text-xl font-bold text-slate-800 dark:text-slate-100">Side-by-Side Comparison</h2>
                            <button 
                                onClick={onClose}
                                className="p-2 text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 rounded-full transition-colors"
                            >
                                <X className="w-5 h-5" />
                            </button>
                        </div>

                        {/* Scrollable Content */}
                        <div className="overflow-y-auto p-6 flex-1 custom-scrollbar">
                            <div className="grid grid-cols-2 gap-4 md:gap-8">
                                
                                {/* Candidate A Header */}
                                <div className="text-center pb-4 border-b border-slate-200 dark:border-slate-800 relative group">
                                    {candidateA.photoUrl ? (
                                        <img 
                                            src={candidateA.photoUrl} 
                                            alt={candidateA.name} 
                                            onError={(e) => {
                                                (e.target as HTMLImageElement).src = '/my-leader/assets/placeholder-avatar.svg';
                                            }}
                                            className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full object-cover border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 animate-glow relative z-10 bg-slate-100 dark:bg-slate-800" 
                                        />
                                    ) : (
                                        <div className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 flex items-center justify-center bg-slate-100 dark:bg-slate-800 text-slate-400 relative z-10">
                                            <User className="w-10 h-10 opacity-50" />
                                        </div>
                                    )}
                                    <h3 className="font-bold text-lg text-slate-900 dark:text-slate-100 relative z-10">{candidateA.name}</h3>
                                    <div className="flex items-center justify-center gap-1.5 mt-1 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-full w-fit mx-auto">
                                        {candidateA.partyLogoUrl && (
                                            <img src={candidateA.partyLogoUrl} alt={candidateA.party} className="w-4 h-4 object-contain" />
                                        )}
                                        <p className="text-xs font-semibold text-slate-500">{candidateA.party}</p>
                                    </div>
                                </div>

                                {/* Candidate B Header */}
                                <div className="text-center pb-4 border-b border-slate-200 dark:border-slate-800 relative group flex flex-col items-center">
                                    {candidateB.photoUrl ? (
                                        <img 
                                            src={candidateB.photoUrl} 
                                            alt={candidateB.name} 
                                            onError={(e) => {
                                                (e.target as HTMLImageElement).src = '/my-leader/assets/placeholder-avatar.svg';
                                            }}
                                            className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full object-cover border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 animate-glow relative z-10 bg-slate-100 dark:bg-slate-800" 
                                        />
                                    ) : (
                                        <div className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 flex items-center justify-center bg-slate-100 dark:bg-slate-800 text-slate-400 relative z-10">
                                            <User className="w-10 h-10 opacity-50" />
                                        </div>
                                    )}
                                    <div className="relative z-10 mb-1">
                                        <select 
                                            value={candidateB.id} 
                                            onChange={(e) => setCandidateBId(e.target.value)}
                                            className="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-600 rounded-lg text-lg font-bold text-slate-900 dark:text-slate-100 py-1 pl-2 pr-6 appearance-none hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 max-w-[180px] sm:max-w-[220px] truncate cursor-pointer shadow-sm"
                                        >
                                            {availableCandidates.filter(c => c.id !== candidateA.id).map(c => (
                                                <option key={c.id} value={c.id}>{c.name}</option>
                                            ))}
                                        </select>
                                        <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-slate-500">
                                            <svg className="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clipRule="evenodd" fillRule="evenodd"></path></svg>
                                        </div>
                                    </div>
                                    <div className="flex items-center justify-center gap-1.5 mt-1 bg-slate-100 dark:bg-slate-800 px-2.5 py-1 rounded-full w-fit mx-auto">
                                        {candidateB.partyLogoUrl && (
                                            <img src={candidateB.partyLogoUrl} alt={candidateB.party} className="w-4 h-4 object-contain" />
                                        )}
                                        <p className="text-xs font-semibold text-slate-500">{candidateB.party}</p>
                                    </div>
                                </div>

                                {/* Metrics Comparison */}
                                <div className="col-span-2 grid grid-cols-2 gap-x-4 md:gap-x-8 gap-y-6 pt-4 text-sm">
                                    
                                    {/* Education */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mb--4">Educational Qualification</div>
                                    <div className="text-center font-medium bg-slate-50 dark:bg-slate-800/50 p-3 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 relative overflow-hidden group">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <span className="relative z-10">{candidateA.education}</span>
                                    </div>
                                    <div className="text-center font-medium bg-slate-50 dark:bg-slate-800/50 p-3 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 relative overflow-hidden group">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <span className="relative z-10">{candidateB.education}</span>
                                    </div>

                                    {/* Attendance */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2">Legislative Attendance</div>
                                    <div className="text-center text-xl font-bold text-blue-600 dark:text-blue-400">{candidateA.attendancePercentage}%</div>
                                    <div className="text-center text-xl font-bold text-blue-600 dark:text-blue-400">{candidateB.attendancePercentage}%</div>

                                    {/* Net Worth */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2">Declared Net Worth</div>
                                    <div className="text-center text-lg font-bold text-emerald-600 dark:text-emerald-400">{formatINR(candidateA.declaredAssetsINR - candidateA.declaredLiabilitiesINR)}</div>
                                    <div className="text-center text-lg font-bold text-emerald-600 dark:text-emerald-400">{formatINR(candidateB.declaredAssetsINR - candidateB.declaredLiabilitiesINR)}</div>

                                    {/* Criminal Cases */}
                                    <div className="col-span-2 text-center text-xs font-bold uppercase tracking-wider text-slate-400 mt-2">Pending Criminal Cases</div>
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
