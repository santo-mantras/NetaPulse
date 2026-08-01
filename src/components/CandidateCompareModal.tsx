import React from 'react';
import type { CandidateProfile } from '../types/governance';
import { X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CandidateCompareModalProps {
    isOpen: boolean;
    onClose: () => void;
    candidateA: CandidateProfile;
    candidateB: CandidateProfile;
}

export const CandidateCompareModal: React.FC<CandidateCompareModalProps> = ({ isOpen, onClose, candidateA, candidateB }) => {
    
    // Format currency
    const formatINR = (amount: number) => {
        if (amount >= 10000000) return `₹${(amount / 10000000).toFixed(2)} Cr`;
        if (amount >= 100000) return `₹${(amount / 100000).toFixed(2)} L`;
        return `₹${amount.toLocaleString('en-IN')}`;
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
                                    <img src={candidateA.photoUrl} alt={candidateA.name} className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full object-cover border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 animate-glow relative z-10" />
                                    <h3 className="font-bold text-lg text-slate-900 dark:text-slate-100 relative z-10">{candidateA.name}</h3>
                                    <p className="text-xs font-semibold text-slate-500 bg-slate-100 dark:bg-slate-800 px-2 py-1 rounded-full inline-block mt-1">{candidateA.party}</p>
                                </div>

                                {/* Candidate B Header */}
                                <div className="text-center pb-4 border-b border-slate-200 dark:border-slate-800 relative group">
                                    <img src={candidateB.photoUrl} alt={candidateB.name} className="w-20 h-20 md:w-24 md:h-24 mx-auto rounded-full object-cover border-4 border-slate-200 dark:border-slate-700 shadow-md mb-3 animate-glow relative z-10" />
                                    <h3 className="font-bold text-lg text-slate-900 dark:text-slate-100 relative z-10">{candidateB.name}</h3>
                                    <p className="text-xs font-semibold text-slate-500 bg-slate-100 dark:bg-slate-800 px-2 py-1 rounded-full inline-block mt-1">{candidateB.party}</p>
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
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </>
            )}
        </AnimatePresence>
    );
};
