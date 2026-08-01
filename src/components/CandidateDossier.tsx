import React, { useState } from 'react';
import type {
    CandidateProfile,
    CampaignPromise,
    NewsReport,
    LocationHierarchy
} from '../types/governance';
import {
    User,
    FileText,
    AlertTriangle,
    CheckCircle2,
    XCircle,
    Clock,
    ExternalLink,
    ShieldCheck,
    Building2,
    GraduationCap,
    Scale,
    Newspaper,
    Award,
    Sparkles,
    Briefcase,
    Activity,
    BookOpen,
    Hospital,
    ShieldAlert,
    MapPin
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CandidateDossierProps {
    candidate: CandidateProfile;
    promises: CampaignPromise[];
    news: NewsReport[];
    location: LocationHierarchy;
}

export const CandidateDossier: React.FC<CandidateDossierProps> = ({
    candidate,
    promises,
    news,
    location
}) => {
    const [activeTab, setActiveTab] = useState<'overview' | 'promises' | 'legal' | 'news'>('overview');
    const [isFlipped, setIsFlipped] = useState(false);

    // Format currency in Indian Numbering System (Lakhs / Crores)
    const formatINR = (amount: number) => {
        if (amount >= 10000000) {
            return `₹${(amount / 10000000).toFixed(2)} Cr`;
        } else if (amount >= 100000) {
            return `₹${(amount / 100000).toFixed(2)} Lakh`;
        }
        return `₹${amount.toLocaleString('en-IN')}`;
    };

    return (
        <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="w-full max-w-4xl mx-auto bg-white dark:bg-slate-900 rounded-xl shadow-lg border border-slate-200 dark:border-slate-800 overflow-hidden text-slate-900 dark:text-slate-100"
        >
            {/* 1. Candidate Header / Identity Card */}
            <div className="p-6 bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white relative overflow-hidden">
                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent animate-shimmer" />
                <div className="flex flex-col sm:flex-row items-center sm:items-start gap-6 relative z-10">
                    <img
                        src={candidate.photoUrl}
                        alt={candidate.name}
                        className="w-28 h-28 rounded-full object-cover border-4 border-white/20 shadow-md animate-glow"
                    />
                    <div className="flex-1 text-center sm:text-left">
                        <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 mb-2">
                            <span className="bg-blue-500/30 text-blue-200 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-blue-400/30">
                                {candidate.role}
                            </span>
                            <span className="bg-slate-700/60 text-slate-200 text-xs font-medium px-2.5 py-0.5 rounded-full">
                                {candidate.party}
                            </span>
                            <span className="bg-emerald-500/30 text-emerald-200 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-emerald-400/30">
                                Term {candidate.termsServed}
                            </span>
                        </div>
                        <h1 className="text-2xl font-bold tracking-tight">{candidate.name}</h1>
                        <p className="text-sm text-slate-300 flex items-center justify-center sm:justify-start gap-1 mt-1">
                            <Building2 className="w-4 h-4" /> {candidate.constituencyName}
                        </p>
                        <p className="text-xs text-slate-400 flex items-center justify-center sm:justify-start gap-1 mt-1">
                            <GraduationCap className="w-4 h-4" /> {candidate.education}
                        </p>
                    </div>

                    {/* Affidavit Direct Citation Link */}
                    <a
                        href={candidate.affidavitPdfUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-blue-200 bg-white/10 hover:bg-white/20 rounded-lg transition-colors border border-white/10 mt-4 sm:mt-0"
                    >
                        <FileText className="w-3.5 h-3.5" /> ECI Affidavit <ExternalLink className="w-3 h-3" />
                    </a>
                </div>
            </div>

            {/* 2. Quick Stat Badges Grid */}
            <div className="grid grid-cols-2 sm:grid-cols-4 divide-x sm:divide-y-0 divide-y divide-slate-200 dark:divide-slate-800 bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-800">
                <div className="p-4 text-center">
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Attendance</p>
                    <p className="text-2xl font-extrabold text-blue-600 dark:text-blue-400 mt-1">{candidate.attendancePercentage}%</p>
                </div>
                <div className="p-4 text-center">
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Questions</p>
                    <p className="text-2xl font-extrabold text-indigo-600 dark:text-indigo-400 mt-1">{candidate.questionsAsked}</p>
                </div>
                <div className="p-4 text-center">
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Net Worth</p>
                    <p className="text-2xl font-extrabold text-emerald-600 dark:text-emerald-400 mt-1">{formatINR(candidate.declaredAssetsINR - candidate.declaredLiabilitiesINR)}</p>
                </div>
                <div className="p-4 text-center">
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Criminal Cases</p>
                    <p className={`text-2xl font-extrabold mt-1 ${candidate.criminalCasesCount > 0 ? 'text-amber-600 dark:text-amber-400' : 'text-slate-600 dark:text-slate-400'}`}>
                        {candidate.criminalCasesCount}
                    </p>
                </div>
            </div>

            {/* 3. Navigation Tabs */}
            <div className="flex border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 overflow-x-auto custom-scrollbar">
                {[
                    { id: 'overview', icon: User, label: 'Performance Overview' },
                    { id: 'promises', icon: CheckCircle2, label: `Promises (${promises.length})` },
                    { id: 'legal', icon: Scale, label: 'Legal & Assets' },
                    { id: 'news', icon: Newspaper, label: `Media Spotlight (${news.length})` }
                ].map((tab) => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id as any)}
                        className={`flex items-center gap-2 px-5 py-4 text-sm font-semibold border-b-2 whitespace-nowrap transition-colors relative ${
                            activeTab === tab.id
                                ? 'border-blue-600 text-blue-600 dark:border-blue-400 dark:text-blue-400'
                                : 'border-transparent text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200'
                        }`}
                    >
                        <tab.icon className="w-4 h-4" /> {tab.label}
                    </button>
                ))}
            </div>

            {/* Tab Contents */}
            <div className="p-6 overflow-hidden">
                <AnimatePresence mode="wait">
                    <motion.div
                        key={activeTab}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: 10 }}
                        transition={{ duration: 0.2 }}
                    >
                        {/* Tab 1: Overview & Simple Bars */}
                        {activeTab === 'overview' && (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">

                                {/* Legislative Performance Bars */}
                                <div className="space-y-6">
                                    <h3 className="text-sm font-bold text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 pb-2 flex items-center gap-2">
                                        <Activity className="w-4 h-4" /> Legislative Performance
                                    </h3>
                                    
                                    <div className="space-y-4">
                                        <div>
                                            <div className="flex justify-between text-xs font-semibold mb-1">
                                                <span>{candidate.attendanceBody} Attendance</span>
                                                <span className="text-blue-600">{candidate.attendancePercentage}%</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-black/50 dark:border-white/50 z-10" 
                                                    style={{ left: `${candidate.averages?.attendance || 75}%` }}
                                                    title={`Avg: ${candidate.averages?.attendance || 75}%`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${candidate.attendancePercentage}%` }} transition={{ duration: 1, delay: 0.2 }}
                                                    className="bg-blue-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <p className="text-[10px] text-slate-500 mt-1">Avg: {candidate.averages?.attendance || 75}%</p>
                                        </div>

                                        <div>
                                            <div className="flex justify-between text-xs font-semibold mb-1">
                                                <span>Questions Asked</span>
                                                <span className="text-indigo-600">{candidate.questionsAsked}</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-black/50 dark:border-white/50 z-10" 
                                                    style={{ left: `${Math.min(candidate.averages?.questions || 30, 100)}%` }}
                                                    title={`Avg: ${candidate.averages?.questions || 30}`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${Math.min(candidate.questionsAsked, 100)}%` }} transition={{ duration: 1, delay: 0.3 }}
                                                    className="bg-indigo-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <p className="text-[10px] text-slate-500 mt-1">Avg: {candidate.averages?.questions || 30}</p>
                                        </div>

                                        <div>
                                            <div className="flex justify-between text-xs font-semibold mb-1">
                                                <span>Private Member Bills</span>
                                                <span className="text-purple-600">{candidate.privateMemberBills}</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-black/50 dark:border-white/50 z-10" 
                                                    style={{ left: `${Math.min((candidate.averages?.bills || 1) * 10, 100)}%` }}
                                                    title={`Avg: ${candidate.averages?.bills || 1}`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${Math.min(candidate.privateMemberBills * 10, 100)}%` }} transition={{ duration: 1, delay: 0.4 }}
                                                    className="bg-purple-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <p className="text-[10px] text-slate-500 mt-1">Avg: {candidate.averages?.bills || 1}</p>
                                        </div>
                                    </div>
                                    
                                    {/* Constituency Stats */}
                                    <h3 className="text-sm font-bold text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 pb-2 flex items-center gap-2 mt-8">
                                        <MapPin className="w-4 h-4" /> {location.districtName || 'Constituency'} District Stats
                                    </h3>
                                    <div className="grid grid-cols-2 gap-4 mb-6">
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-100 dark:border-slate-700/50 flex items-center gap-3 relative overflow-hidden group">
                                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                            <ShieldAlert className="w-6 h-6 text-rose-500 animate-glow relative z-10" />
                                            <div className="relative z-10">
                                                <p className="text-[10px] uppercase text-slate-500 font-bold">Crime Rate</p>
                                                <p className="text-sm font-bold">{location.crimeRate}</p>
                                            </div>
                                        </div>
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-100 dark:border-slate-700/50 flex items-center gap-3 relative overflow-hidden group">
                                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                            <BookOpen className="w-6 h-6 text-blue-500 animate-glow relative z-10" />
                                            <div className="relative z-10">
                                                <p className="text-[10px] uppercase text-slate-500 font-bold">Literacy</p>
                                                <p className="text-sm font-bold">{location.literacyRate}%</p>
                                            </div>
                                        </div>
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-100 dark:border-slate-700/50 flex items-center gap-3 relative overflow-hidden group">
                                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                            <Hospital className="w-6 h-6 text-emerald-500 animate-glow relative z-10" />
                                            <div className="relative z-10">
                                                <p className="text-[10px] uppercase text-slate-500 font-bold">Hospitals</p>
                                                <p className="text-sm font-bold">{location.hospitalsCount}</p>
                                            </div>
                                        </div>
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-lg border border-slate-100 dark:border-slate-700/50 flex items-center gap-3 relative overflow-hidden group">
                                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                            <Building2 className="w-6 h-6 text-amber-500 animate-glow relative z-10" />
                                            <div className="relative z-10">
                                                <p className="text-[10px] uppercase text-slate-500 font-bold">Govt Schools</p>
                                                <p className="text-sm font-bold">{location.govtSchoolsCount}</p>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    {/* Regional Insight Alert */}
                                    {location.regionalInsight && (
                                        <div className="bg-gradient-to-r from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20 border border-blue-200 dark:border-blue-800/50 rounded-xl p-4 shadow-sm">
                                            <div className="flex items-start gap-3">
                                                <div className="bg-blue-100 dark:bg-blue-800/50 p-2 rounded-full mt-1">
                                                    <Sparkles className="w-4 h-4 text-blue-600 dark:text-blue-400" />
                                                </div>
                                                <div>
                                                    <h4 className="font-bold text-sm text-blue-900 dark:text-blue-300 mb-1">
                                                        {location.regionalInsight.title}
                                                    </h4>
                                                    <p className="text-xs text-blue-800/80 dark:text-blue-200/80 mb-2 leading-relaxed">
                                                        <span className="font-semibold block text-[10px] uppercase tracking-wider mb-0.5 text-blue-700/70 dark:text-blue-400/70">Historical Fact</span>
                                                        {location.regionalInsight.historicalFact}
                                                    </p>
                                                    <p className="text-xs text-rose-800/90 dark:text-rose-200/90 leading-relaxed bg-rose-50/50 dark:bg-rose-900/10 p-2 rounded-md border border-rose-100/50 dark:border-rose-900/30">
                                                        <span className="font-semibold block text-[10px] uppercase tracking-wider mb-0.5 text-rose-700/70 dark:text-rose-400/70">Current Challenge</span>
                                                        {location.regionalInsight.currentChallenge}
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    )}
                                </div>

                                {/* Flip Card Interactions */}
                                <div className="space-y-6">
                                    <h3 className="text-sm font-bold text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 pb-2 flex items-center gap-2">
                                        <Sparkles className="w-4 h-4 text-amber-500" /> Did you know?
                                    </h3>
                                    
                                    <div className="perspective-1000 h-64 w-full cursor-pointer group" onClick={() => setIsFlipped(!isFlipped)}>
                                        <motion.div 
                                            className="w-full h-full relative preserve-3d transition-all duration-500"
                                            animate={{ rotateY: isFlipped ? 180 : 0 }}
                                        >
                                            {/* Front of Card */}
                                            <div className="absolute w-full h-full backface-hidden bg-gradient-to-br from-indigo-500 via-purple-500 to-purple-600 bg-[length:200%_auto] animate-gradient rounded-2xl p-6 text-white shadow-lg flex flex-col items-center justify-center text-center overflow-hidden">
                                                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-shimmer" />
                                                <Award className="w-12 h-12 mb-4 text-white/90 animate-glow relative z-10" />
                                                <h4 className="font-bold text-lg mb-2 relative z-10">Tap to reveal a Fun Fact!</h4>
                                                <p className="text-xs text-white/80 relative z-10">Flip this card to learn something unique about {candidate.name}.</p>
                                            </div>
                                            
                                            {/* Back of Card */}
                                            <div className="absolute w-full h-full backface-hidden bg-gradient-to-br from-emerald-500 via-teal-400 to-teal-600 bg-[length:200%_auto] animate-gradient rounded-2xl p-6 text-white shadow-lg flex flex-col items-center justify-center text-center rotate-y-180 overflow-hidden">
                                                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-shimmer" />
                                                <Sparkles className="w-8 h-8 mb-4 text-white/90 animate-glow relative z-10" />
                                                <p className="font-medium text-sm md:text-base leading-relaxed relative z-10">{candidate.funFact}</p>
                                                <div className="mt-4 pt-4 border-t border-white/20 relative z-10">
                                                    <p className="text-xs text-white/90"><span className="font-bold">Political Fact:</span> {candidate.politicalFact}</p>
                                                </div>
                                            </div>
                                        </motion.div>
                                    </div>
                                    <p className="text-center text-xs text-slate-400 mt-2">Tap the card to flip</p>
                                </div>

                            </div>
                        )}

                        {/* Tab 2: Campaign Promises Matrix */}
                        {activeTab === 'promises' && (
                            <div className="space-y-4">
                                {promises.length === 0 ? (
                                    <p className="text-sm text-slate-500 p-4 bg-slate-50 dark:bg-slate-800 rounded-lg">No promises tracked yet.</p>
                                ) : promises.map((promise) => {
                                    const statusStyles = {
                                        Fulfilled: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border-emerald-300',
                                        'In Progress': 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border-amber-300',
                                        Unfulfilled: 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border-rose-300',
                                        'Insufficient Data': 'bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-300 border-slate-300'
                                    };

                                    const StatusIcon = {
                                        Fulfilled: CheckCircle2,
                                        'In Progress': Clock,
                                        Unfulfilled: XCircle,
                                        'Insufficient Data': AlertTriangle
                                    }[promise.status];

                                    return (
                                        <div key={promise.id} className="p-4 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 hover:shadow-md transition-shadow relative overflow-hidden group">
                                            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                            {promise.status === 'Fulfilled' && (
                                                <div className="absolute top-0 right-0 w-16 h-16 bg-emerald-500/10 rounded-bl-full -z-10 group-hover:scale-150 transition-transform duration-500" />
                                            )}
                                            <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-2 mb-3 relative z-10">
                                                <h4 className="font-bold text-base">{promise.title}</h4>
                                                <span className={`inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full border shadow-sm ${statusStyles[promise.status]}`}>
                                                    <StatusIcon className="w-3.5 h-3.5 animate-glow" />
                                                    {promise.status}
                                                </span>
                                            </div>
                                            <div className="grid md:grid-cols-2 gap-4 relative z-10">
                                                <div className="bg-white dark:bg-slate-900 p-3 rounded-lg border border-slate-200 dark:border-slate-700">
                                                    <span className="text-[10px] uppercase text-slate-400 font-bold tracking-wider mb-1 block">Manifesto Claim</span>
                                                    <p className="text-xs text-slate-700 dark:text-slate-300">"{promise.declaredInManifesto}"</p>
                                                </div>
                                                <div className="bg-white dark:bg-slate-900 p-3 rounded-lg border border-slate-200 dark:border-slate-700">
                                                    <span className="text-[10px] uppercase text-slate-400 font-bold tracking-wider mb-1 block">Verified Ground Reality</span>
                                                    <p className="text-xs font-medium text-slate-800 dark:text-slate-200">{promise.verifiedOutcome}</p>
                                                </div>
                                            </div>
                                            <p className="text-[10px] text-slate-400 mt-3 text-right flex justify-end items-center gap-1 relative z-10">
                                                <ShieldCheck className="w-3 h-3 animate-glow" /> Source: {promise.sourceCitation}
                                            </p>
                                        </div>
                                    );
                                })}
                            </div>
                        )}

                        {/* Tab 3: Legal Disclosures */}
                        {activeTab === 'legal' && (
                            <div className="grid md:grid-cols-2 gap-6">
                                <div className="p-5 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 relative overflow-hidden group">
                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                    <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-4 flex items-center gap-2 relative z-10">
                                        <AlertTriangle className="w-4 h-4 text-amber-500 animate-glow" /> Criminal Cases ({candidate.criminalCasesCount})
                                    </h3>
                                    {candidate.criminalCasesCount === 0 ? (
                                        <div className="text-center py-8 relative z-10">
                                            <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-2 opacity-50 animate-glow" />
                                            <p className="text-sm text-emerald-600 dark:text-emerald-400 font-medium">Clean Record.<br/>No pending criminal cases declared.</p>
                                        </div>
                                    ) : (
                                        <div className="space-y-3 relative z-10">
                                            {candidate.criminalCasesDetails.map((item, idx) => (
                                                <div key={idx} className="p-4 bg-white dark:bg-slate-900 rounded-lg border border-rose-200 dark:border-rose-900/50 shadow-sm">
                                                    <p className="font-bold text-rose-600 dark:text-rose-400 text-sm mb-2">{item.charges}</p>
                                                    <div className="flex justify-between items-center text-xs">
                                                        <span className="text-slate-500 font-mono bg-slate-100 dark:bg-slate-800 px-2 py-1 rounded">Case: {item.caseNumber}</span>
                                                        <span className="font-bold text-amber-600 dark:text-amber-500 bg-amber-50 dark:bg-amber-900/30 px-2 py-1 rounded">{item.status}</span>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    )}
                                </div>

                                <div className="p-5 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 flex flex-col justify-between relative overflow-hidden group">
                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                    <div className="relative z-10">
                                        <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-4 flex items-center gap-2">
                                            <Briefcase className="w-4 h-4 text-emerald-500 animate-glow" /> Wealth Breakdown
                                        </h3>
                                        <div className="space-y-4 text-sm">
                                            <div className="flex justify-between items-center py-3 border-b border-slate-200 dark:border-slate-700">
                                                <span className="text-slate-600 dark:text-slate-400 font-medium">Gross Movable Assets</span>
                                                <span className="font-bold text-slate-800 dark:text-slate-200">{formatINR(candidate.declaredAssetsINR * 0.4)}</span>
                                            </div>
                                            <div className="flex justify-between items-center py-3 border-b border-slate-200 dark:border-slate-700">
                                                <span className="text-slate-600 dark:text-slate-400 font-medium">Immovable Property</span>
                                                <span className="font-bold text-slate-800 dark:text-slate-200">{formatINR(candidate.declaredAssetsINR * 0.6)}</span>
                                            </div>
                                            <div className="flex justify-between items-center py-3 border-b border-slate-200 dark:border-slate-700">
                                                <span className="text-slate-600 dark:text-slate-400 font-medium">Liabilities & Loans</span>
                                                <span className="font-bold text-rose-600 dark:text-rose-400 bg-rose-50 dark:bg-rose-900/20 px-2 py-1 rounded">{formatINR(candidate.declaredLiabilitiesINR)}</span>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="mt-6 p-4 bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800 rounded-xl text-center relative z-10">
                                        <p className="text-xs font-bold text-emerald-600 dark:text-emerald-500 uppercase tracking-wider mb-1">Declared Net Wealth</p>
                                        <p className="text-3xl font-extrabold text-emerald-700 dark:text-emerald-400">{formatINR(candidate.declaredAssetsINR - candidate.declaredLiabilitiesINR)}</p>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Tab 4: Secondary News Spotlight */}
                        {activeTab === 'news' && (
                            <div className="grid md:grid-cols-2 gap-4">
                                {news.length === 0 ? (
                                    <p className="text-sm text-slate-500 col-span-2 p-4 bg-slate-50 dark:bg-slate-800 rounded-lg text-center">No major media spotlights found.</p>
                                ) : news.map((item) => (
                                    <div key={item.id} className="p-5 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 hover:border-blue-300 dark:hover:border-blue-700 transition-colors group flex flex-col justify-between relative overflow-hidden">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <div className="relative z-10">
                                            <div className="flex justify-between items-center mb-3">
                                                <span className="text-[10px] font-extrabold text-white bg-slate-800 dark:bg-slate-700 px-2.5 py-1 rounded-full uppercase tracking-wider">{item.publisher}</span>
                                                <span className="text-xs font-medium text-slate-500">{item.publishedDate}</span>
                                            </div>
                                            <h4 className="font-bold text-base mb-2 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">{item.title}</h4>
                                            <p className="text-sm text-slate-600 dark:text-slate-300 mb-4 leading-relaxed">{item.summary}</p>
                                        </div>
                                        <div className="flex justify-between items-center pt-4 border-t border-slate-200 dark:border-slate-700 relative z-10">
                                            <span className="inline-flex items-center gap-1.5 text-xs font-bold text-emerald-700 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-900/30 px-2.5 py-1 rounded border border-emerald-200 dark:border-emerald-800">
                                                <ShieldCheck className="w-3.5 h-3.5 animate-glow" /> {item.verificationStatus}
                                            </span>
                                            <a
                                                href={item.url}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className="inline-flex items-center gap-1 text-sm text-blue-600 dark:text-blue-400 font-bold hover:underline"
                                            >
                                                Read Source <ExternalLink className="w-4 h-4" />
                                            </a>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </motion.div>
                </AnimatePresence>
            </div>
        </motion.div>
    );
};
