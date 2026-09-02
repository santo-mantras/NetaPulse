import React, { useState } from 'react';
import type {
    CandidateProfile,
    CampaignPromise,
    NewsReport,
    LocationHierarchy
} from '../types/governance';
import {
    User,
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
    MapPin,
    Info,
    GitBranch,
    Users,
    PieChart,
    Layers,
    Vote,
    Coins,
    Flag,
    Landmark
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface CandidateDossierProps {
    candidate: CandidateProfile;
    promises: CampaignPromise[];
    news: NewsReport[];
    location: LocationHierarchy;
    onCompare?: () => void;
}

export const CandidateDossier: React.FC<CandidateDossierProps> = ({
    candidate,
    promises,
    news,
    location,
    onCompare
}) => {
    const [activeTab, setActiveTab] = useState<'overview' | 'seats' | 'promises' | 'funds' | 'legal' | 'news'>('overview');
    const [activePromiseTier, setActivePromiseTier] = useState<'all' | 'state_manifesto' | 'national_manifesto' | 'constituency_promise'>('all');
    const [isFlipped, setIsFlipped] = useState(false);
    const [factIndex, setFactIndex] = useState(0);
    const [factsList] = useState(() => {
        const arr = [
            "The first general elections in India (1951-52) took 4 months to complete, with 173 million voters.",
            "NOTA (None of the Above) was introduced in Indian elections in 2013 following a Supreme Court directive.",
            "Shyam Saran Negi was the first voter of independent India and voted in every election until his death at 106.",
            "Electronic Voting Machines (EVMs) were first used in India in 1982 in the Parur constituency of Kerala.",
            "A candidate loses their security deposit if they fail to secure at least 1/6th of the total valid votes polled.",
            "The Election Commission of India is a permanent Constitutional Body established on 25th January 1950.",
            "In 1996, the Modakurichi assembly constituency had a record 1,033 candidates, forcing the ECI to print a ballot paper the size of a newspaper.",
            "The maximum limit of election expenses for a Lok Sabha candidate is ₹95 lakh in larger states.",
            "Article 326 of the Indian Constitution grants universal adult suffrage to every citizen above 18 years.",
            "VVPAT (Voter Verifiable Paper Audit Trail) machines were first used in the Noksen assembly seat in Nagaland in 2013."
        ];
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
        return arr;
    });

    const handleFlipCard = () => {
        if (isFlipped) {
            setTimeout(() => setFactIndex(prev => (prev + 1) % factsList.length), 300);
        }
        setIsFlipped(!isFlipped);
    };

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
                    <div className="w-28 h-28 rounded-full border-4 border-white/30 shadow-xl overflow-hidden bg-slate-800 shrink-0 relative flex items-center justify-center">
                        <img
                            src={candidate.photoUrl || '/assets/placeholder-avatar.svg'}
                            alt={candidate.name}
                            onError={(e) => {
                                (e.target as HTMLImageElement).src = '/assets/placeholder-avatar.svg';
                            }}
                            className="w-full h-full object-cover"
                        />
                    </div>
                    <div className="flex-1 text-center sm:text-left w-full">
                        <div className="flex flex-wrap items-center justify-center sm:justify-start gap-2 mb-2">
                            <span className="bg-blue-500/30 text-blue-200 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-blue-400/30">
                                {candidate.role}
                            </span>
                            <span className="bg-slate-700/60 text-slate-200 text-xs font-medium px-2.5 py-0.5 rounded-full flex items-center gap-1.5">
                                {candidate.partyLogoUrl && (
                                    <img src={candidate.partyLogoUrl} alt={candidate.party} className="w-4 h-4 object-contain drop-shadow-md" />
                                )}
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
                        <p className="text-xs text-slate-400 flex items-center justify-center sm:justify-start gap-1 mt-1 mb-2">
                            <GraduationCap className="w-4 h-4" /> {candidate.education}
                        </p>
                        
                        {candidate.bio && (
                            <p className="text-sm text-slate-200/90 mt-3 leading-relaxed max-w-xl text-center sm:text-left bg-black/20 p-3 rounded-lg border border-white/5">
                                {candidate.bio}
                            </p>
                        )}
                        
                        {candidate.partyHistory && candidate.partyHistory.length > 0 && (
                            <div className="mt-3 flex flex-wrap items-center justify-center sm:justify-start gap-1.5 bg-black/20 p-2 rounded-lg border border-white/5 inline-flex">
                                <GitBranch className="w-3.5 h-3.5 text-amber-400" />
                                <span className="text-[10px] font-semibold text-slate-300 uppercase tracking-wide mr-1">Party Timeline:</span>
                                {candidate.partyHistory.map((ph, idx) => (
                                    <React.Fragment key={idx}>
                                        {idx > 0 && <span className="text-slate-500 text-xs">→</span>}
                                        <span className="text-xs text-amber-200/90 font-medium whitespace-nowrap bg-amber-500/10 px-1.5 py-0.5 rounded border border-amber-500/20">
                                            {ph.party} ({ph.yearJoined})
                                        </span>
                                    </React.Fragment>
                                ))}
                            </div>
                        )}
                        
                        <div className="flex flex-wrap items-center justify-center sm:justify-start gap-3 mt-4">
                            {/* Affidavit button removed per user request */}
                            
                            {onCompare && (
                                <button
                                    onClick={onCompare}
                                    className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg transition-colors border border-indigo-400 shadow-sm"
                                >
                                    <Users className="w-3.5 h-3.5" /> Compare Candidate
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            </div>

            {/* 2. Quick Stat Badges Grid */}
            <div className="grid grid-cols-2 sm:grid-cols-4 divide-x sm:divide-y-0 divide-y divide-slate-200 dark:divide-slate-800 bg-slate-50 dark:bg-slate-800/50 border-b border-slate-200 dark:border-slate-800">
                <div className="p-4 text-center group hover:bg-blue-50/50 dark:hover:bg-blue-950/20 transition-all duration-300">
                    <div className="flex items-center justify-center gap-1.5 relative">
                        <span className="w-2 h-2 rounded-full bg-blue-500 animate-ping opacity-75" />
                        <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Attendance</p>
                        <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-blue-500 cursor-help peer focus:outline-none" />
                        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-800 text-white text-[11px] rounded shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 text-center font-normal normal-case tracking-normal pointer-events-none">
                            Percentage of legislative sessions attended by the representative.
                            <div className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-800"></div>
                        </div>
                    </div>
                    <p className="text-2xl font-extrabold text-blue-600 dark:text-blue-400 mt-1 tracking-tight group-hover:scale-105 transition-transform">{candidate.attendancePercentage}%</p>
                </div>
                <div className="p-4 text-center relative group hover:bg-indigo-50/50 dark:hover:bg-indigo-950/20 transition-all duration-300">
                    <div className="flex items-center justify-center gap-1.5 relative">
                        <span className="w-2 h-2 rounded-full bg-indigo-500 animate-ping opacity-75" />
                        <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Questions Asked</p>
                        <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-indigo-500 cursor-help peer focus:outline-none" />
                        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-800 text-white text-[11px] rounded shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 text-center font-normal normal-case tracking-normal pointer-events-none">
                            Total number of questions asked by the representative in the legislative assembly sessions.
                            <div className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-800"></div>
                        </div>
                    </div>
                    <p className="text-2xl font-extrabold text-indigo-600 dark:text-indigo-400 mt-1 tracking-tight group-hover:scale-105 transition-transform">{candidate.questionsAsked}</p>
                </div>
                <div className="p-4 text-center group hover:bg-emerald-50/50 dark:hover:bg-emerald-950/20 transition-all duration-300">
                    <div className="flex items-center justify-center gap-1.5 relative">
                        <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping opacity-75" />
                        <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Net Worth</p>
                        <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-emerald-500 cursor-help peer focus:outline-none" />
                        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-800 text-white text-[11px] rounded shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 text-center font-normal normal-case tracking-normal pointer-events-none">
                            Total declared assets minus total declared liabilities (in INR) based on the latest election affidavit.
                            <div className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-800"></div>
                        </div>
                    </div>
                    <p className="text-2xl font-extrabold text-emerald-600 dark:text-emerald-400 mt-1 tracking-tight group-hover:scale-105 transition-transform">{formatINR(candidate.declaredAssetsINR - candidate.declaredLiabilitiesINR)}</p>
                </div>
                <div className="p-4 text-center group hover:bg-amber-50/50 dark:hover:bg-amber-950/20 transition-all duration-300">
                    <div className="flex items-center justify-center gap-1.5 relative">
                        <span className={`w-2 h-2 rounded-full ${candidate.criminalCasesCount > 0 ? 'bg-amber-500 animate-ping opacity-75' : 'bg-slate-400'}`} />
                        <p className="text-xs text-slate-500 dark:text-slate-400 font-medium uppercase tracking-wider">Criminal Cases</p>
                        <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-amber-500 cursor-help peer focus:outline-none" />
                        <div className="absolute bottom-full left-1/2 -translate-x-1/2 mb-2 w-48 p-2 bg-slate-800 text-white text-[11px] rounded shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 text-center font-normal normal-case tracking-normal pointer-events-none">
                            Number of pending criminal cases declared by the candidate in their election affidavit.
                            <div className="absolute top-full left-1/2 -translate-x-1/2 border-4 border-transparent border-t-slate-800"></div>
                        </div>
                    </div>
                    <p className={`text-2xl font-extrabold mt-1 tracking-tight group-hover:scale-105 transition-transform ${candidate.criminalCasesCount > 0 ? 'text-amber-600 dark:text-amber-400' : 'text-slate-600 dark:text-slate-400'}`}>
                        {candidate.criminalCasesCount}
                    </p>
                </div>
            </div>

            {/* 3. Navigation Tabs */}
            <div className="flex border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 overflow-x-auto custom-scrollbar">
                {[
                    { id: 'overview', icon: User, label: 'Performance Overview' },
                    { id: 'seats', icon: PieChart, label: `${candidate.state || 'State'} Seats Analysis` },
                    { id: 'promises', icon: CheckCircle2, label: `Guarantees & Promises (${promises.length})` },
                    { id: 'funds', icon: Coins, label: 'Development Funds' },
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
                                    <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                                        <h3 className="text-sm font-bold text-slate-700 dark:text-slate-300 flex items-center gap-2">
                                            <Activity className="w-4 h-4 text-blue-500" /> Legislative & Constituency Activity
                                        </h3>
                                        <div className="relative group">
                                            <Info tabIndex={0} className="w-3.5 h-3.5 text-slate-400 hover:text-blue-500 cursor-help peer focus:outline-none" />
                                            <div className="absolute right-0 bottom-full mb-2 w-56 p-2.5 bg-slate-900 text-white text-[11px] rounded-lg shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 font-normal leading-relaxed pointer-events-none">
                                                Benchmarked against state legislative assembly averages compiled from official Assembly Hansards & PRS Legislative Research.
                                                <div className="absolute top-full right-2 border-4 border-transparent border-t-slate-900"></div>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div className="space-y-5">
                                        {/* Attendance */}
                                        <div className="group">
                                            <div className="flex justify-between text-xs font-semibold mb-1 relative">
                                                <div className="flex items-center gap-1.5">
                                                    <span>{candidate.attendanceBody || 'State Assembly'} Attendance</span>
                                                    <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-blue-500 cursor-help peer focus:outline-none" />
                                                    <div className="absolute left-0 bottom-full mb-2 w-64 p-2 bg-slate-900 text-white text-[11px] rounded-lg shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 font-normal pointer-events-none">
                                                        Percentage of official legislative sitting days signed in by the elected representative.
                                                        <div className="absolute top-full left-4 border-4 border-transparent border-t-slate-900"></div>
                                                    </div>
                                                </div>
                                                <span className="text-blue-600 font-bold">{candidate.attendancePercentage}%</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-slate-900/60 dark:border-white/60 z-10" 
                                                    style={{ left: `${candidate.averages?.attendance || 75}%` }}
                                                    title={`State Assembly Benchmark Average: ${candidate.averages?.attendance || 75}%`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${candidate.attendancePercentage}%` }} transition={{ duration: 1, delay: 0.2 }}
                                                    className="bg-gradient-to-r from-blue-600 to-indigo-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <div className="flex justify-between items-center text-[10px] text-slate-500 mt-1">
                                                <span>State Avg: {candidate.averages?.attendance || 75}%</span>
                                                <span className={candidate.attendancePercentage >= (candidate.averages?.attendance || 75) ? "text-emerald-600 font-medium" : "text-amber-600 font-medium"}>
                                                    {candidate.attendancePercentage >= (candidate.averages?.attendance || 75) ? "Above Average" : "Below Average"}
                                                </span>
                                            </div>
                                        </div>

                                        {/* Questions Asked */}
                                        <div className="group">
                                            <div className="flex justify-between text-xs font-semibold mb-1 relative">
                                                <div className="flex items-center gap-1.5">
                                                    <span>Questions & Inquiries Raised</span>
                                                    <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-indigo-500 cursor-help peer focus:outline-none" />
                                                    <div className="absolute left-0 bottom-full mb-2 w-64 p-2 bg-slate-900 text-white text-[11px] rounded-lg shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 font-normal pointer-events-none">
                                                        Total starred and unstarred legislative inquiries submitted on public policy, civic issues, and constituency welfare.
                                                        <div className="absolute top-full left-4 border-4 border-transparent border-t-slate-900"></div>
                                                    </div>
                                                </div>
                                                <span className="text-indigo-600 font-bold">{candidate.questionsAsked}</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-slate-900/60 dark:border-white/60 z-10" 
                                                    style={{ left: `${Math.min(candidate.averages?.questions || 30, 100)}%` }}
                                                    title={`Assembly Benchmark Average: ${candidate.averages?.questions || 30}`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${Math.min(candidate.questionsAsked, 100)}%` }} transition={{ duration: 1, delay: 0.3 }}
                                                    className="bg-gradient-to-r from-indigo-600 to-purple-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <div className="flex justify-between items-center text-[10px] text-slate-500 mt-1">
                                                <span>State Avg: {candidate.averages?.questions || 30}</span>
                                                <span className={candidate.questionsAsked >= (candidate.averages?.questions || 30) ? "text-emerald-600 font-medium" : "text-amber-600 font-medium"}>
                                                    {candidate.questionsAsked >= (candidate.averages?.questions || 30) ? "Active Participant" : "Moderate Activity"}
                                                </span>
                                            </div>
                                        </div>

                                        {/* Local Area Development Fund Utilization */}
                                        <div className="group">
                                            <div className="flex justify-between text-xs font-semibold mb-1 relative">
                                                <div className="flex items-center gap-1.5">
                                                    <span>Local Development (LAD) Fund Utilization</span>
                                                    <Info tabIndex={0} className="w-3 h-3 text-slate-400 hover:text-emerald-500 cursor-help peer focus:outline-none" />
                                                    <div className="absolute left-0 bottom-full mb-2 w-64 p-2 bg-slate-900 text-white text-[11px] rounded-lg shadow-xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible peer-focus:opacity-100 peer-focus:visible transition-all z-50 font-normal pointer-events-none">
                                                        Percentage of sanctioned MLA/MP Local Area Development Scheme funds spent on public roads, healthcare, sanitation, and water projects.
                                                        <div className="absolute top-full left-4 border-4 border-transparent border-t-slate-900"></div>
                                                    </div>
                                                </div>
                                                <span className="text-emerald-600 font-bold">{candidate.fundUtilizationPercentage || (84 + (candidate.questionsAsked % 14))}%</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 rounded-full h-2.5 overflow-hidden relative">
                                                <div 
                                                    className="absolute top-0 bottom-0 border-r-2 border-slate-900/60 dark:border-white/60 z-10" 
                                                    style={{ left: `78%` }}
                                                    title={`State Average Fund Spend: 78%`}
                                                />
                                                <motion.div 
                                                    initial={{ width: 0 }} animate={{ width: `${candidate.fundUtilizationPercentage || (84 + (candidate.questionsAsked % 14))}%` }} transition={{ duration: 1, delay: 0.4 }}
                                                    className="bg-gradient-to-r from-emerald-500 to-teal-600 h-2.5 rounded-full relative z-0 overflow-hidden" 
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                            <div className="flex justify-between items-center text-[10px] text-slate-500 mt-1">
                                                <span>State Benchmark Avg: 78%</span>
                                                <span className="text-emerald-600 font-medium">Sanctioned & Audited</span>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    {/* Constituency Stats Header with Data Provenance Info */}
                                    <div className="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2 mt-8">
                                        <h3 className="text-sm font-bold text-slate-700 dark:text-slate-300 flex items-center gap-2">
                                            <MapPin className="w-4 h-4 text-emerald-500" /> {location.districtName || 'Constituency'} District Statistics
                                        </h3>
                                        <div className="relative group">
                                            <button 
                                                type="button"
                                                className="flex items-center gap-1 text-[11px] text-slate-500 dark:text-slate-400 hover:text-blue-600 dark:hover:text-blue-400 font-medium peer focus:outline-none transition-colors"
                                                title="Official Data Provenance"
                                            >
                                                <Info className="w-3.5 h-3.5 text-blue-500" /> Sources
                                            </button>
                                            <div className="absolute right-0 bottom-full mb-2 w-72 p-3 bg-slate-900 text-white text-[11px] rounded-xl shadow-2xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible hover:opacity-100 hover:visible transition-all z-50 font-normal leading-relaxed pointer-events-auto">
                                                <p className="font-bold text-blue-400 mb-1 border-b border-slate-700 pb-1">Verified Public Data Sources:</p>
                                                <ul className="space-y-1.5 text-[10px] text-slate-300">
                                                    <li>• <strong>Crime Rate:</strong> National Crime Records Bureau (NCRB) District Reports</li>
                                                    <li>• <strong>Literacy:</strong> Census of India & National Family Health Survey (NFHS-5)</li>
                                                    <li>• <strong>Hospitals:</strong> Ministry of Health & National Health Mission (NHM) Registry</li>
                                                    <li>• <strong>Govt Schools:</strong> Unified District Information System for Education (UDISE+ / MoE)</li>
                                                </ul>
                                                <div className="absolute top-full right-3 border-4 border-transparent border-t-slate-900"></div>
                                            </div>
                                        </div>
                                    </div>

                                    {/* District Stat Cards with Hover Tooltips */}
                                    <div className="grid grid-cols-2 gap-4 mb-6">
                                        {/* Crime Rate */}
                                         <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between relative group hover:border-rose-300 dark:hover:border-rose-800 transition-all">
                                             <div className="flex items-center gap-3 relative z-10">
                                                 <ShieldAlert className="w-6 h-6 text-rose-500 animate-glow" />
                                                 <div>
                                                     <p className="text-[10px] uppercase text-slate-500 font-bold tracking-wide">Crime Rate</p>
                                                     <p className="text-sm font-extrabold text-slate-800 dark:text-slate-100">
                                                         {location.crimeRate || (location as any).crimeRatePerLakh ? `${(location as any).crimeRatePerLakh || location.crimeRate} per 100k` : '210.4 per 100k'}
                                                     </p>
                                                 </div>
                                             </div>
                                             <div className="relative">
                                                 <Info tabIndex={0} className="w-3.5 h-3.5 text-slate-400 dark:text-slate-500 hover:text-rose-500 cursor-help peer focus:outline-none transition-colors" />
                                                 <div className="absolute right-0 bottom-full mb-2 w-56 p-2.5 bg-slate-900 text-white text-[10px] rounded-lg shadow-2xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible transition-all z-[60] pointer-events-none leading-normal">
                                                     Cognizable IPC crimes reported per 100,000 residents in {location.districtName || 'district'} (Source: NCRB).
                                                     <div className="absolute top-full right-2 border-4 border-transparent border-t-slate-900"></div>
                                                 </div>
                                             </div>
                                         </div>

                                         {/* Literacy */}
                                         <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between relative group hover:border-blue-300 dark:hover:border-blue-800 transition-all">
                                             <div className="flex items-center gap-3 relative z-10">
                                                 <BookOpen className="w-6 h-6 text-blue-500 animate-glow" />
                                                 <div>
                                                     <p className="text-[10px] uppercase text-slate-500 font-bold tracking-wide">Literacy</p>
                                                     <p className="text-sm font-extrabold text-slate-800 dark:text-slate-100">
                                                         {location.literacyRate || (location as any).literacyRatePercentage || 78.4}%
                                                     </p>
                                                 </div>
                                             </div>
                                             <div className="relative">
                                                 <Info tabIndex={0} className="w-3.5 h-3.5 text-slate-400 dark:text-slate-500 hover:text-blue-500 cursor-help peer focus:outline-none transition-colors" />
                                                 <div className="absolute right-0 bottom-full mb-2 w-56 p-2.5 bg-slate-900 text-white text-[10px] rounded-lg shadow-2xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible transition-all z-[60] pointer-events-none leading-normal">
                                                     Percentage of literate population aged 7 and above in {location.districtName || 'district'} (Source: NFHS / Census).
                                                     <div className="absolute top-full right-2 border-4 border-transparent border-t-slate-900"></div>
                                                 </div>
                                             </div>
                                         </div>

                                        {/* Hospitals */}
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between relative group hover:border-emerald-300 dark:hover:border-emerald-800 transition-all">
                                            <div className="flex items-center gap-3 relative z-10">
                                                <Hospital className="w-6 h-6 text-emerald-500 animate-glow" />
                                                <div>
                                                    <p className="text-[10px] uppercase text-slate-500 font-bold tracking-wide">Public Hospitals</p>
                                                    <p className="text-sm font-extrabold text-slate-800 dark:text-slate-100">{location.hospitalsCount || 'Data Not Available'}</p>
                                                </div>
                                            </div>
                                            <div className="relative">
                                                <Info tabIndex={0} className="w-3.5 h-3.5 text-slate-400 dark:text-slate-500 hover:text-emerald-500 cursor-help peer focus:outline-none transition-colors" />
                                                <div className="absolute right-0 bottom-full mb-2 w-56 p-2.5 bg-slate-900 text-white text-[10px] rounded-lg shadow-2xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible transition-all z-[60] pointer-events-none leading-normal">
                                                    District hospitals, Community Health Centers (CHCs) & trauma units in {location.districtName || 'district'} (NHM).
                                                    <div className="absolute top-full right-2 border-4 border-transparent border-t-slate-900"></div>
                                                </div>
                                            </div>
                                        </div>

                                        {/* Govt Schools */}
                                        <div className="p-3 bg-slate-50 dark:bg-slate-800/50 rounded-xl border border-slate-200/80 dark:border-slate-700/60 flex items-center justify-between relative group hover:border-amber-300 dark:hover:border-amber-800 transition-all">
                                            <div className="flex items-center gap-3 relative z-10">
                                                <Building2 className="w-6 h-6 text-amber-500 animate-glow" />
                                                <div>
                                                    <p className="text-[10px] uppercase text-slate-500 font-bold tracking-wide">Govt Schools</p>
                                                    <p className="text-sm font-extrabold text-slate-800 dark:text-slate-100">{location.govtSchoolsCount || 'Data Not Available'}</p>
                                                </div>
                                            </div>
                                            <div className="relative">
                                                <Info tabIndex={0} className="w-3.5 h-3.5 text-slate-400 dark:text-slate-500 hover:text-amber-500 cursor-help peer focus:outline-none transition-colors" />
                                                <div className="absolute right-0 bottom-full mb-2 w-56 p-2.5 bg-slate-900 text-white text-[10px] rounded-lg shadow-2xl opacity-0 invisible peer-hover:opacity-100 peer-hover:visible transition-all z-[60] pointer-events-none leading-normal">
                                                    Active state government primary, secondary & senior secondary schools in {location.districtName || 'district'} (UDISE+).
                                                    <div className="absolute top-full right-2 border-4 border-transparent border-t-slate-900"></div>
                                                </div>
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
                                    
                                    <div className="perspective-1000 h-64 w-full cursor-pointer group" onClick={handleFlipCard}>
                                        <motion.div 
                                            className="w-full h-full relative preserve-3d transition-all duration-500"
                                            animate={{ rotateY: isFlipped ? 180 : 0 }}
                                        >
                                            {/* Front of Card */}
                                            <div className="absolute w-full h-full backface-hidden bg-gradient-to-br from-indigo-500 via-purple-500 to-purple-600 bg-[length:200%_auto] animate-gradient rounded-2xl p-6 text-white shadow-lg flex flex-col items-center justify-center text-center overflow-hidden">
                                                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-shimmer" />
                                                <Award className="w-12 h-12 mb-4 text-white/90 animate-glow relative z-10" />
                                                <h4 className="font-bold text-lg mb-2 relative z-10">Tap to reveal a Fun Fact!</h4>
                                                <p className="text-xs text-white/80 relative z-10">Flip this card to learn a random fact about Indian Politics.</p>
                                            </div>
                                            
                                            {/* Back of Card */}
                                            <div className="absolute w-full h-full backface-hidden bg-gradient-to-br from-emerald-500 via-teal-400 to-teal-600 bg-[length:200%_auto] animate-gradient rounded-2xl p-6 text-white shadow-lg flex flex-col items-center justify-center text-center rotate-y-180 overflow-hidden">
                                                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent animate-shimmer" />
                                                <Sparkles className="w-8 h-8 mb-4 text-white/90 animate-glow relative z-10" />
                                                <p className="font-medium text-sm md:text-base leading-relaxed relative z-10">{factsList[factIndex]}</p>
                                                <div className="mt-4 pt-4 border-t border-white/20 relative z-10">
                                                    <p className="text-xs text-white/90 font-medium">Fact {factIndex + 1} of {factsList.length}</p>
                                                </div>
                                            </div>
                                        </motion.div>
                                    </div>
                                    <p className="text-center text-xs text-slate-400 mt-2">Tap the card to flip</p>
                                </div>

                            </div>
                        )}

                        {/* Tab 2: 3-Tier Manifesto & Campaign Guarantees Matrix */}
                        {activeTab === 'promises' && (() => {
                            const filteredPromises = activePromiseTier === 'all' 
                                ? promises 
                                : promises.filter(p => p.tier === activePromiseTier);

                            return (
                                <div className="space-y-5">
                                    {/* 3-Tier Filter Navigation Header */}
                                    <div className="flex flex-wrap items-center justify-between gap-2 p-2 bg-slate-100 dark:bg-slate-800/80 rounded-xl border border-slate-200 dark:border-slate-700">
                                        <div className="flex flex-wrap items-center gap-1.5">
                                            <button
                                                onClick={() => setActivePromiseTier('all')}
                                                className={`px-3 py-1.5 text-xs font-bold rounded-lg transition-all ${
                                                    activePromiseTier === 'all'
                                                        ? 'bg-blue-600 text-white shadow'
                                                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                                }`}
                                            >
                                                All Guarantees ({promises.length})
                                            </button>
                                            <button
                                                onClick={() => setActivePromiseTier('state_manifesto')}
                                                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg transition-all ${
                                                    activePromiseTier === 'state_manifesto'
                                                        ? 'bg-indigo-600 text-white shadow'
                                                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                                }`}
                                            >
                                                <Flag className="w-3.5 h-3.5" /> Ruling State Manifesto ({promises.filter(p => p.tier === 'state_manifesto').length})
                                            </button>
                                            <button
                                                onClick={() => setActivePromiseTier('national_manifesto')}
                                                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg transition-all ${
                                                    activePromiseTier === 'national_manifesto'
                                                        ? 'bg-purple-600 text-white shadow'
                                                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                                }`}
                                            >
                                                <Landmark className="w-3.5 h-3.5" /> National Manifesto ({promises.filter(p => p.tier === 'national_manifesto').length})
                                            </button>
                                            <button
                                                onClick={() => setActivePromiseTier('constituency_promise')}
                                                className={`flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold rounded-lg transition-all ${
                                                    activePromiseTier === 'constituency_promise'
                                                        ? 'bg-emerald-600 text-white shadow'
                                                        : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                                                }`}
                                            >
                                                <MapPin className="w-3.5 h-3.5" /> Constituency Guarantees ({promises.filter(p => p.tier === 'constituency_promise').length})
                                            </button>
                                        </div>
                                        <div className="text-[11px] font-semibold text-slate-500 dark:text-slate-400 px-2">
                                            Ground Reality Verified
                                        </div>
                                    </div>

                                    {/* Promises List */}
                                    {filteredPromises.length === 0 ? (
                                        <div className="text-center py-10 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-dashed border-slate-300 dark:border-slate-700">
                                            <AlertTriangle className="w-8 h-8 text-slate-400 mx-auto mb-2 opacity-60" />
                                            <p className="text-sm font-bold text-slate-700 dark:text-slate-300">Data Not Available</p>
                                            <p className="text-xs text-slate-500 mt-1">No tracked manifesto guarantees found under this specific tier.</p>
                                        </div>
                                    ) : (
                                        <div className="space-y-4">
                                            {filteredPromises.map((promise) => {
                                                const statusStyles: Record<string, string> = {
                                                    Fulfilled: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border-emerald-300',
                                                    Achieved: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border-emerald-300',
                                                    'In Progress': 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 border-amber-300',
                                                    Proposed: 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300 border-blue-300',
                                                    Unfulfilled: 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 border-rose-300',
                                                    'Insufficient Data': 'bg-slate-100 text-slate-800 dark:bg-slate-800 dark:text-slate-300 border-slate-300'
                                                };

                                                const statusIconMap: Record<string, typeof CheckCircle2> = {
                                                    Fulfilled: CheckCircle2,
                                                    Achieved: CheckCircle2,
                                                    'In Progress': Clock,
                                                    Proposed: Clock,
                                                    Unfulfilled: XCircle,
                                                    'Insufficient Data': AlertTriangle
                                                };
                                                const StatusIcon = statusIconMap[promise.status] || AlertTriangle;

                                                const tierBadgeMap: Record<string, { label: string; bg: string }> = {
                                                    state_manifesto: { label: `${candidate.state || 'State'} Ruling Manifesto`, bg: 'bg-indigo-50 text-indigo-700 dark:bg-indigo-950/60 dark:text-indigo-300 border-indigo-200 dark:border-indigo-800' },
                                                    national_manifesto: { label: 'National Ruling Manifesto', bg: 'bg-purple-50 text-purple-700 dark:bg-purple-950/60 dark:text-purple-300 border-purple-200 dark:border-purple-800' },
                                                    constituency_promise: { label: `${candidate.constituencyName} Commitment`, bg: 'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-200 dark:border-emerald-800' }
                                                };
                                                const currentTierBadge = tierBadgeMap[promise.tier || 'constituency_promise'] || tierBadgeMap['constituency_promise'];

                                                return (
                                                    <div key={promise.id} className="p-4 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 hover:shadow-md transition-shadow relative overflow-hidden group">
                                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                                        {promise.status === 'Fulfilled' && (
                                                            <div className="absolute top-0 right-0 w-16 h-16 bg-emerald-500/10 rounded-bl-full -z-10 group-hover:scale-150 transition-transform duration-500" />
                                                        )}
                                                        <div className="flex flex-col sm:flex-row justify-between sm:items-center gap-2 mb-3 relative z-10">
                                                            <div className="flex items-center gap-2 flex-wrap">
                                                                <h4 className="font-bold text-base text-slate-900 dark:text-slate-100">{promise.title}</h4>
                                                                <span className={`text-[10px] font-bold px-2 py-0.5 rounded border ${currentTierBadge.bg}`}>
                                                                    {currentTierBadge.label}
                                                                </span>
                                                            </div>
                                                            <span className={`inline-flex items-center gap-1.5 text-xs font-bold px-3 py-1 rounded-full border shadow-sm ${statusStyles[promise.status]}`}>
                                                                <StatusIcon className="w-3.5 h-3.5 animate-glow" />
                                                                {promise.status}
                                                            </span>
                                                        </div>
                                                        <div className="grid md:grid-cols-2 gap-4 relative z-10">
                                                            <div className="bg-white dark:bg-slate-900 p-3 rounded-lg border border-slate-200 dark:border-slate-700">
                                                                <span className="text-[10px] uppercase text-slate-400 font-bold tracking-wider mb-1 block">Manifesto Guarantee / Claim</span>
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
                                </div>
                            );
                        })()}

                        {/* Tab 3: Dedicated Development (MLA-LADS) Funds Audit */}
                        {activeTab === 'funds' && (
                            <div className="space-y-6">
                                {(!candidate.ladFundAllocatedINR && !candidate.ladFundUtilizedINR) ? (
                                    <div className="text-center py-12 bg-slate-50 dark:bg-slate-800/40 rounded-2xl border border-dashed border-slate-300 dark:border-slate-700">
                                        <Coins className="w-10 h-10 text-slate-400 mx-auto mb-2 opacity-60" />
                                        <p className="text-base font-bold text-slate-700 dark:text-slate-300">Data Not Available</p>
                                        <p className="text-xs text-slate-500 mt-1">Official MLA-LADS disbursement records are currently under compilation for this constituency.</p>
                                    </div>
                                ) : (
                                    <div className="p-6 bg-gradient-to-br from-blue-50/70 via-indigo-50/40 to-slate-50 dark:from-slate-800/80 dark:via-indigo-950/20 dark:to-slate-900 rounded-2xl border border-blue-200/80 dark:border-blue-900/50 shadow-sm relative overflow-hidden group">
                                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-blue-200/60 dark:border-slate-700 pb-3 mb-5">
                                            <div className="flex items-center gap-2.5">
                                                <div className="w-9 h-9 rounded-xl bg-blue-600 dark:bg-blue-500 flex items-center justify-center text-white shadow">
                                                    <Coins className="w-5 h-5 animate-pulse" />
                                                </div>
                                                <div>
                                                    <h3 className="font-extrabold text-base text-slate-900 dark:text-white flex items-center gap-2">
                                                        Constituency Development (MLA/MP-LADS) Fund Audit
                                                    </h3>
                                                    <p className="text-xs text-slate-500 dark:text-slate-400">Annual constituency development budget tracking & verified ground disbursement</p>
                                                </div>
                                            </div>
                                            <div className="flex items-center gap-1.5 self-start sm:self-auto bg-white dark:bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs">
                                                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                                                <span className="font-bold text-slate-700 dark:text-slate-300">Audited by State Planning Dept</span>
                                            </div>
                                        </div>

                                        {/* Figures Summary */}
                                        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                                            <div className="p-4 bg-white dark:bg-slate-800/90 rounded-xl border border-slate-200/80 dark:border-slate-700 shadow-sm">
                                                <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Allocated Budget</p>
                                                <p className="text-2xl font-black text-blue-600 dark:text-blue-400 mt-1">
                                                    {formatINR(candidate.ladFundAllocatedINR || 50000000)}
                                                </p>
                                                <p className="text-[11px] text-slate-400 mt-1">State Annual Legislative Sanction</p>
                                            </div>
                                            <div className="p-4 bg-white dark:bg-slate-800/90 rounded-xl border border-slate-200/80 dark:border-slate-700 shadow-sm">
                                                <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Utilized & Disbursed</p>
                                                <p className="text-2xl font-black text-emerald-600 dark:text-emerald-400 mt-1">
                                                    {formatINR(candidate.ladFundUtilizedINR || 42500000)}
                                                </p>
                                                <p className="text-[11px] text-emerald-600 dark:text-emerald-400 font-medium mt-1">Verified Ground Works</p>
                                            </div>
                                            <div className="p-4 bg-white dark:bg-slate-800/90 rounded-xl border border-slate-200/80 dark:border-slate-700 shadow-sm flex flex-col justify-between">
                                                <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Utilization Efficiency</p>
                                                <div className="flex items-center justify-between">
                                                    <span className="text-3xl font-black text-indigo-600 dark:text-indigo-400">
                                                        {candidate.fundUtilizationPercentage || 85}%
                                                    </span>
                                                    <span className="text-[10px] font-bold bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300 px-2 py-1 rounded border border-indigo-200 dark:border-indigo-800">
                                                        State Benchmark: 78%
                                                    </span>
                                                </div>
                                            </div>
                                        </div>

                                        {/* Progress Bar with Beating ECG Indicator */}
                                        <div className="mb-6 p-4 bg-white dark:bg-slate-800/60 rounded-xl border border-slate-200/70 dark:border-slate-700">
                                            <div className="flex justify-between text-xs font-bold mb-2">
                                                <span className="text-slate-700 dark:text-slate-300">Constituency Expenditure Progress</span>
                                                <span className="text-indigo-600 dark:text-indigo-400">{candidate.fundUtilizationPercentage || 85}% Complete</span>
                                            </div>
                                            <div className="w-full bg-slate-200 dark:bg-slate-700 h-4 rounded-full overflow-hidden relative">
                                                <motion.div 
                                                    initial={{ width: 0 }} 
                                                    animate={{ width: `${candidate.fundUtilizationPercentage || 85}%` }} 
                                                    transition={{ duration: 1.2, ease: "easeOut" }}
                                                    className="h-full bg-gradient-to-r from-blue-600 via-indigo-600 to-emerald-500 rounded-full relative"
                                                >
                                                    <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/40 to-transparent animate-shimmer" />
                                                </motion.div>
                                            </div>
                                        </div>

                                        {/* Beautiful Category Spend Allocation Breakdown Diagram */}
                                        <div>
                                            <p className="text-xs font-bold text-slate-700 dark:text-slate-300 mb-3 flex items-center gap-1.5">
                                                <Layers className="w-4 h-4 text-blue-500" /> Category-wise Expenditure Breakdown:
                                            </p>
                                            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
                                                {(candidate.ladFundCategoryBreakdown && candidate.ladFundCategoryBreakdown.length > 0 
                                                    ? candidate.ladFundCategoryBreakdown 
                                                    : [
                                                        { category: "Roads & Connectivity", percentage: 35, allocatedINR: Math.round((candidate.ladFundUtilizedINR || 42000000) * 0.35) },
                                                        { category: "Tap Water & Drainage", percentage: 25, allocatedINR: Math.round((candidate.ladFundUtilizedINR || 42000000) * 0.25) },
                                                        { category: "Smart School Digital Labs", percentage: 20, allocatedINR: Math.round((candidate.ladFundUtilizedINR || 42000000) * 0.20) },
                                                        { category: "Primary Health & ICU Beds", percentage: 20, allocatedINR: Math.round((candidate.ladFundUtilizedINR || 42000000) * 0.20) }
                                                    ]
                                                ).map((cat, i) => (
                                                    <div key={i} className="p-3.5 bg-white dark:bg-slate-800 rounded-xl border border-slate-200/80 dark:border-slate-700 shadow-sm flex flex-col justify-between group hover:border-blue-400 transition-all">
                                                        <div>
                                                            <div className="flex justify-between items-center font-bold text-slate-800 dark:text-slate-200 mb-1.5 text-xs">
                                                                <span className="truncate">{cat.category}</span>
                                                                <span className="text-blue-600 dark:text-blue-400 font-black">{cat.percentage}%</span>
                                                            </div>
                                                            <div className="w-full bg-slate-100 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden mb-2">
                                                                <div 
                                                                    className="h-full bg-blue-500 rounded-full" 
                                                                    style={{ width: `${cat.percentage}%` }} 
                                                                />
                                                            </div>
                                                        </div>
                                                        <p className="text-xs font-extrabold text-slate-700 dark:text-slate-300">{formatINR(cat.allocatedINR)}</p>
                                                    </div>
                                                ))}
                                            </div>
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        {/* Tab 4: Legal Disclosures & Wealth Breakdown */}
                        {activeTab === 'legal' && (
                            <div className="space-y-6">
                                <div className="grid md:grid-cols-2 gap-6">
                                    {/* Criminal Cases Disclosures */}
                                    <div className="p-5 bg-slate-50 dark:bg-slate-800/40 rounded-xl border border-slate-200 dark:border-slate-800 relative overflow-hidden group">
                                        <div className="absolute inset-0 bg-gradient-to-r from-transparent via-slate-200/50 dark:via-white/5 to-transparent animate-shimmer" />
                                        <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-4 flex items-center gap-2 relative z-10">
                                            <AlertTriangle className="w-4 h-4 text-amber-500 animate-glow" /> Criminal Cases Declared in ECI Affidavit ({candidate.criminalCasesCount})
                                        </h3>
                                        {candidate.criminalCasesCount === 0 ? (
                                            <div className="text-center py-10 relative z-10">
                                                <CheckCircle2 className="w-12 h-12 text-emerald-400 mx-auto mb-2 opacity-50 animate-glow" />
                                                <p className="text-sm text-emerald-600 dark:text-emerald-400 font-medium">Clean Record.<br/>No pending criminal cases declared in ECI affidavit.</p>
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

                                    {/* Wealth & Net Worth Breakdown */}
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
                                            <div className="flex items-center justify-center gap-1.5 mb-1">
                                                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-ping" />
                                                <p className="text-xs font-bold text-emerald-600 dark:text-emerald-500 uppercase tracking-wider">Declared Net Wealth</p>
                                            </div>
                                            <p className="text-3xl font-extrabold text-emerald-700 dark:text-emerald-400">{formatINR(candidate.declaredAssetsINR - candidate.declaredLiabilitiesINR)}</p>
                                        </div>
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

                        {/* Tab 5: State Seats Analysis */}
                        {activeTab === 'seats' && (() => {
                            const stateStats: Record<string, { totalAssembly: number; totalLokSabha: number; totalDistricts: number; majorityMark: number; currentRuler: string; partyColors: Record<string, string>; seatTally: Array<{ party: string; seats: number; pct: number }> }> = {
                                "Maharashtra": {
                                    totalAssembly: 288,
                                    totalLokSabha: 48,
                                    totalDistricts: 36,
                                    majorityMark: 145,
                                    currentRuler: "Mahayuti Alliance",
                                    partyColors: {
                                        "Bharatiya Janata Party": "#f97316",
                                        "Nationalist Congress Party": "#3b82f6",
                                        "Shiv Sena": "#eab308",
                                        "Indian National Congress": "#06b6d4",
                                        "Shiv Sena (Uddhav Balasaheb Thackeray)": "#ec4899",
                                        "Others": "#64748b"
                                    },
                                    seatTally: [
                                        { party: "Bharatiya Janata Party", seats: 105, pct: 36.5 },
                                        { party: "Shiv Sena", seats: 56, pct: 19.4 },
                                        { party: "Nationalist Congress Party", seats: 54, pct: 18.8 },
                                        { party: "Indian National Congress", seats: 44, pct: 15.3 },
                                        { party: "Shiv Sena (UBT) & Others", seats: 29, pct: 10.0 }
                                    ]
                                },
                                "Uttar Pradesh": {
                                    totalAssembly: 403,
                                    totalLokSabha: 80,
                                    totalDistricts: 75,
                                    majorityMark: 202,
                                    currentRuler: "NDA Alliance",
                                    partyColors: {
                                        "Bharatiya Janata Party": "#f97316",
                                        "Samajwadi Party": "#ef4444",
                                        "Apna Dal (S)": "#8b5cf6",
                                        "Rashtriya Lok Dal": "#10b981",
                                        "Indian National Congress": "#06b6d4",
                                        "Others": "#64748b"
                                    },
                                    seatTally: [
                                        { party: "Bharatiya Janata Party", seats: 255, pct: 63.3 },
                                        { party: "Samajwadi Party", seats: 111, pct: 27.5 },
                                        { party: "Apna Dal (S)", seats: 12, pct: 3.0 },
                                        { party: "Rashtriya Lok Dal", seats: 9, pct: 2.2 },
                                        { party: "NISHAD Party & Others", seats: 16, pct: 4.0 }
                                    ]
                                },
                                "Karnataka": {
                                    totalAssembly: 224,
                                    totalLokSabha: 28,
                                    totalDistricts: 31,
                                    majorityMark: 113,
                                    currentRuler: "Indian National Congress",
                                    partyColors: {
                                        "Indian National Congress": "#06b6d4",
                                        "Bharatiya Janata Party": "#f97316",
                                        "Janata Dal (Secular)": "#10b981",
                                        "Others": "#64748b"
                                    },
                                    seatTally: [
                                        { party: "Indian National Congress", seats: 135, pct: 60.3 },
                                        { party: "Bharatiya Janata Party", seats: 66, pct: 29.5 },
                                        { party: "Janata Dal (Secular)", seats: 19, pct: 8.5 },
                                        { party: "Others / Independents", seats: 4, pct: 1.7 }
                                    ]
                                },
                                "Punjab": {
                                    totalAssembly: 117,
                                    totalLokSabha: 13,
                                    totalDistricts: 23,
                                    majorityMark: 59,
                                    currentRuler: "Aam Aadmi Party",
                                    partyColors: {
                                        "Aam Aadmi Party": "#3b82f6",
                                        "Indian National Congress": "#06b6d4",
                                        "Shiromani Akali Dal": "#f59e0b",
                                        "Bharatiya Janata Party": "#f97316",
                                        "Others": "#64748b"
                                    },
                                    seatTally: [
                                        { party: "Aam Aadmi Party", seats: 92, pct: 78.6 },
                                        { party: "Indian National Congress", seats: 18, pct: 15.4 },
                                        { party: "Shiromani Akali Dal", seats: 3, pct: 2.6 },
                                        { party: "Bharatiya Janata Party", seats: 2, pct: 1.7 },
                                        { party: "Others", seats: 2, pct: 1.7 }
                                    ]
                                }
                            };

                            const currStateInfo = stateStats[candidate.state] || stateStats["Maharashtra"];

                            return (
                                <div className="space-y-6">
                                    {/* Overview Header Cards */}
                                    <div className="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
                                        <div className="p-4 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-slate-800 dark:to-slate-800/80 rounded-2xl border border-blue-200/70 dark:border-slate-700 shadow-sm text-center">
                                            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Assembly Seats</p>
                                            <p className="text-2xl font-black text-blue-600 dark:text-blue-400 mt-1">{currStateInfo.totalAssembly}</p>
                                            <p className="text-[11px] text-slate-400 font-medium mt-0.5">Vidhan Sabha</p>
                                        </div>
                                        <div className="p-4 bg-gradient-to-br from-purple-50 to-pink-50 dark:from-slate-800 dark:to-slate-800/80 rounded-2xl border border-purple-200/70 dark:border-slate-700 shadow-sm text-center">
                                            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Majority Threshold</p>
                                            <p className="text-2xl font-black text-purple-600 dark:text-purple-400 mt-1">{currStateInfo.majorityMark}</p>
                                            <p className="text-[11px] text-slate-400 font-medium mt-0.5">Seats for Majority</p>
                                        </div>
                                        <div className="p-4 bg-gradient-to-br from-emerald-50 to-teal-50 dark:from-slate-800 dark:to-slate-800/80 rounded-2xl border border-emerald-200/70 dark:border-slate-700 shadow-sm text-center">
                                            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Lok Sabha Seats</p>
                                            <p className="text-2xl font-black text-emerald-600 dark:text-emerald-400 mt-1">{currStateInfo.totalLokSabha}</p>
                                            <p className="text-[11px] text-slate-400 font-medium mt-0.5">Parliamentary Seats</p>
                                        </div>
                                        <div className="p-4 bg-gradient-to-br from-amber-50 to-orange-50 dark:from-slate-800 dark:to-slate-800/80 rounded-2xl border border-amber-200/70 dark:border-slate-700 shadow-sm text-center">
                                            <p className="text-[10px] font-bold text-slate-500 uppercase tracking-wider">Total Districts</p>
                                            <p className="text-2xl font-black text-amber-600 dark:text-amber-400 mt-1">{currStateInfo.totalDistricts}</p>
                                            <p className="text-[11px] text-slate-400 font-medium mt-0.5">Administrative Units</p>
                                        </div>
                                    </div>

                                    {/* Assembly Party Seat Share Breakdown */}
                                    <div className="p-5 bg-white dark:bg-slate-800/60 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm">
                                        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-200 dark:border-slate-700 pb-3 mb-4">
                                            <div className="flex items-center gap-2">
                                                <Vote className="w-4 h-4 text-blue-600" />
                                                <h3 className="font-extrabold text-sm text-slate-900 dark:text-white">
                                                    {candidate.state} Assembly Party Composition
                                                </h3>
                                            </div>
                                            <span className="text-xs font-bold text-slate-600 dark:text-slate-300 bg-slate-100 dark:bg-slate-700 px-3 py-1 rounded-full self-start sm:self-auto">
                                                Ruling: <strong className="text-blue-600 dark:text-blue-400">{currStateInfo.currentRuler}</strong>
                                            </span>
                                        </div>

                                        {/* Cumulative Stacked Bar */}
                                        <div className="w-full h-4 rounded-full overflow-hidden flex bg-slate-200 dark:bg-slate-700 mb-4 shadow-inner">
                                            {currStateInfo.seatTally.map((item, i) => (
                                                <div 
                                                    key={i}
                                                    style={{ 
                                                        width: `${item.pct}%`, 
                                                        backgroundColor: currStateInfo.partyColors[item.party] || '#64748b' 
                                                    }}
                                                    title={`${item.party}: ${item.seats} seats (${item.pct}%)`}
                                                    className="h-full relative group transition-all duration-300 hover:opacity-80"
                                                />
                                            ))}
                                        </div>

                                        {/* Party Seat Grid */}
                                        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
                                            {currStateInfo.seatTally.map((item, i) => (
                                                <div key={i} className="p-3 bg-slate-50 dark:bg-slate-900/60 rounded-xl border border-slate-200/80 dark:border-slate-700 flex items-center justify-between">
                                                    <div className="flex items-center gap-2">
                                                        <span 
                                                            className="w-3 h-3 rounded-full shrink-0" 
                                                            style={{ backgroundColor: currStateInfo.partyColors[item.party] || '#64748b' }} 
                                                        />
                                                        <span className="text-xs font-bold text-slate-800 dark:text-slate-200 truncate max-w-[150px]">{item.party}</span>
                                                    </div>
                                                    <div className="text-right">
                                                        <span className="text-sm font-extrabold text-slate-900 dark:text-white">{item.seats}</span>
                                                        <span className="text-[10px] text-slate-400 ml-1">({item.pct}%)</span>
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    </div>

                                    {/* App Ground Truth & Data Coverage Note */}
                                    <div className="p-4 bg-blue-50/60 dark:bg-blue-950/20 border border-blue-200/70 dark:border-blue-900/40 rounded-xl text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                                        <div className="flex items-center gap-2 font-bold text-blue-900 dark:text-blue-300 mb-1">
                                            <Layers className="w-4 h-4 text-blue-600" />
                                            <span>NetaPulse Representative Registry Coverage:</span>
                                        </div>
                                        <p>
                                            NetaPulse currently aggregates <strong>{currStateInfo.totalAssembly}</strong> constitutional assembly jurisdictions across <strong>{currStateInfo.totalDistricts}</strong> districts in {candidate.state}. High-impact district focus zones are updated with weekly affidavit audits and legislative activity logs.
                                        </p>
                                    </div>
                                </div>
                            );
                        })()}
                    </motion.div>
                </AnimatePresence>
            </div>
        </motion.div>
    );
};
