import React, { useState, useEffect, useMemo } from 'react';
import type { LocationHierarchy, CandidateProfile } from '../types/governance';
import { Search, MapPin, User, RotateCcw, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface LocationSelectorProps {
    locations: LocationHierarchy[];
    candidates: CandidateProfile[];
    onLocationSelect: (location: LocationHierarchy) => void;
    onSearch: (query: string) => void;
}

export const LocationSelector: React.FC<LocationSelectorProps> = ({ locations, candidates, onLocationSelect, onSearch }) => {
    // 1. States sorted alphabetically (A-Z)
    const states = useMemo(() => {
        return Array.from(new Set(locations.map(l => l.stateName)))
            .sort((a, b) => a.localeCompare(b));
    }, [locations]);

    // Default initial selection: Assam Chief Minister Himanta Biswa Sarma (Jalukbari, Kamrup Metropolitan)
    // Ensures first impression has authentic leader profile with verified portrait
    const defaultState = 'Assam';
    const defaultDistrict = 'Kamrup Metropolitan';
    const defaultConstituency = 'AC-AS-51 Jalukbari';

    const [selectedState, setSelectedState] = useState(defaultState);
    const [selectedDistrict, setSelectedDistrict] = useState(defaultDistrict);
    const [selectedConstituency, setSelectedConstituency] = useState(defaultConstituency);
    const [searchQuery, setSearchQuery] = useState('');
    
    // Autocomplete state
    const [suggestions, setSuggestions] = useState<CandidateProfile[]>([]);
    const [showSuggestions, setShowSuggestions] = useState(false);

    // 2. Districts sorted alphabetically (A-Z)
    const availableDistricts = useMemo(() => {
        return Array.from(new Set(
            locations.filter(l => l.stateName === selectedState).map(l => l.districtName)
        )).sort((a, b) => a.localeCompare(b));
    }, [locations, selectedState]);

    // 3. Constituencies sorted alphabetically by constituency name (A-Z, Option A)
    const availableConstituencies = useMemo(() => {
        return locations
            .filter(l => l.stateName === selectedState && l.districtName === selectedDistrict)
            .sort((a, b) => a.assemblyConstituencyName.localeCompare(b.assemblyConstituencyName))
            .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);
    }, [locations, selectedState, selectedDistrict]);

    // Reset all selections to default Assam CM state
    const handleReset = () => {
        setSelectedState(defaultState);
        setSelectedDistrict(defaultDistrict);
        setSelectedConstituency(defaultConstituency);
        setSearchQuery('');
        onSearch('');
        setShowSuggestions(false);
    };

    // Initial select trigger or when constituency changes
    useEffect(() => {
        const loc = locations.find(l => 
            l.stateName === selectedState &&
            l.districtName === selectedDistrict &&
            `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}` === selectedConstituency
        );
        if (loc) {
            onLocationSelect(loc);
        }
    }, [selectedState, selectedDistrict, selectedConstituency, locations, onLocationSelect]);

    // Handle cascading resets with alphabetical order
    const handleStateChange = (state: string) => {
        setSelectedState(state);
        setSearchQuery('');
        onSearch('');
        setShowSuggestions(false);

        const newDistricts = Array.from(new Set(locations.filter(l => l.stateName === state).map(l => l.districtName)))
            .sort((a, b) => a.localeCompare(b));
        const firstDist = newDistricts[0] || '';
        setSelectedDistrict(firstDist);

        const newConst = locations
            .filter(l => l.stateName === state && l.districtName === firstDist)
            .sort((a, b) => a.assemblyConstituencyName.localeCompare(b.assemblyConstituencyName))
            .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);
        setSelectedConstituency(newConst[0] || '');
    };

    const handleDistrictChange = (dist: string) => {
        setSelectedDistrict(dist);
        setSearchQuery('');
        onSearch('');
        setShowSuggestions(false);

        const newConst = locations
            .filter(l => l.stateName === selectedState && l.districtName === dist)
            .sort((a, b) => a.assemblyConstituencyName.localeCompare(b.assemblyConstituencyName))
            .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);
        setSelectedConstituency(newConst[0] || '');
    };

    const handleSearchInput = (value: string) => {
        setSearchQuery(value);
        onSearch(value);
        
        if (value.trim().length > 0) {
            const q = value.toLowerCase().trim();
            const matches = candidates
                .filter(c => c.name.toLowerCase().includes(q) || c.constituencyName.toLowerCase().includes(q) || (c.party && c.party.toLowerCase().includes(q)))
                .sort((a, b) => {
                    // Priority 1: Exact start of name match
                    const aNameStart = a.name.toLowerCase().startsWith(q) ? -2 : 0;
                    const bNameStart = b.name.toLowerCase().startsWith(q) ? -2 : 0;
                    // Priority 2: Executive leadership (CM / LOP / MP)
                    const aRoleWeight = (a.role && (a.role.toLowerCase().includes('chief minister') || a.role.toLowerCase().includes('leader of opposition') || a.role.toLowerCase().includes('lop'))) ? -1 : 0;
                    const bRoleWeight = (b.role && (b.role.toLowerCase().includes('chief minister') || b.role.toLowerCase().includes('leader of opposition') || b.role.toLowerCase().includes('lop'))) ? -1 : 0;
                    return (aNameStart + aRoleWeight) - (bNameStart + bRoleWeight);
                })
                .slice(0, 10);
            setSuggestions(matches);
            setShowSuggestions(true);
        } else {
            setShowSuggestions(false);
        }
    };

    const handleClearSearch = () => {
        setSearchQuery('');
        onSearch('');
        setShowSuggestions(false);
    };

    const handleSelectSuggestion = (candidate: CandidateProfile) => {
        setSearchQuery(candidate.name);
        setShowSuggestions(false);
        onSearch(candidate.name);
        
        const loc = locations.find(l => 
            l.assemblyConstituencyName === candidate.constituencyName && 
            (!candidate.state || l.stateName === candidate.state)
        );
        if (loc) {
            setSelectedState(loc.stateName);
            setSelectedDistrict(loc.districtName);
            setSelectedConstituency(`${loc.assemblyConstituencyCode} ${loc.assemblyConstituencyName}`);
            onLocationSelect(loc);
        }
    };

    return (
        <motion.div 
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            className="w-full max-w-5xl mx-auto bg-white/90 dark:bg-slate-900/90 backdrop-blur-md rounded-2xl shadow-xl border border-slate-200/50 dark:border-slate-700/50 p-6 md:p-8"
        >
            <div className="flex items-center justify-between mb-6 text-slate-800 dark:text-slate-100">
                <div className="flex items-center gap-3">
                    <div className="p-2 bg-blue-100 dark:bg-blue-900/50 rounded-lg text-blue-600 dark:text-blue-400">
                        <MapPin className="w-5 h-5" />
                    </div>
                    <h2 className="text-xl font-bold">Select Constituency</h2>
                </div>
                
                {/* Reset Filters / Clear Selection Button */}
                <button
                    onClick={handleReset}
                    className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:text-blue-600 dark:hover:text-blue-400 bg-slate-100 dark:bg-slate-800 hover:bg-blue-50 dark:hover:bg-blue-950/40 rounded-lg border border-slate-200 dark:border-slate-700 transition-all shadow-sm group"
                    title="Reset to default selection"
                >
                    <RotateCcw className="w-3.5 h-3.5 group-hover:-rotate-45 transition-transform" />
                    <span>Reset Selection</span>
                </button>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div className="flex flex-col gap-1.5">
                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">State / UT</label>
                    <select 
                        value={selectedState} 
                        onChange={(e) => handleStateChange(e.target.value)}
                        className="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 transition-colors outline-none"
                    >
                        {states.map(s => (
                            <option key={s} value={s}>
                                {s === 'Delhi' ? 'Delhi (UT)' : s}
                            </option>
                        ))}
                    </select>
                </div>

                <div className="flex flex-col gap-1.5">
                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">District</label>
                    <select 
                        value={selectedDistrict} 
                        onChange={(e) => handleDistrictChange(e.target.value)}
                        className="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 transition-colors outline-none"
                    >
                        {availableDistricts.map(d => <option key={d} value={d}>{d}</option>)}
                    </select>
                </div>

                <div className="flex flex-col gap-1.5">
                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Constituency</label>
                    <select 
                        value={selectedConstituency} 
                        onChange={(e) => setSelectedConstituency(e.target.value)}
                        className="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 transition-colors outline-none"
                    >
                        {availableConstituencies.map(c => <option key={c} value={c}>{c}</option>)}
                    </select>
                </div>
            </div>

            <div className="relative z-50">
                <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <Search className="w-5 h-5 text-slate-400" />
                </div>
                <input 
                    type="text" 
                    value={searchQuery}
                    onChange={(e) => handleSearchInput(e.target.value)}
                    onFocus={() => { if (searchQuery.trim().length > 0) setShowSuggestions(true); }}
                    onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
                    className="block w-full p-4 pl-10 pr-10 text-sm text-slate-900 border border-slate-300 rounded-xl bg-slate-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-slate-800 dark:border-slate-700 dark:placeholder-slate-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 outline-none transition-all shadow-inner" 
                    placeholder="Or search by MP/MLA / Candidate Name..." 
                />
                {searchQuery && (
                    <button
                        onClick={handleClearSearch}
                        className="absolute inset-y-0 right-0 flex items-center pr-3.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors"
                        title="Clear search"
                    >
                        <X className="w-4 h-4" />
                    </button>
                )}
                
                <AnimatePresence>
                    {showSuggestions && suggestions.length > 0 && (
                        <motion.ul 
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -10 }}
                            className="absolute z-50 w-full mt-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl shadow-2xl max-h-80 overflow-auto divide-y divide-slate-100 dark:divide-slate-700/50"
                        >
                            {suggestions.map(c => (
                                <li 
                                    key={c.id} 
                                    onClick={() => handleSelectSuggestion(c)}
                                    className="px-4 py-3 hover:bg-slate-50 dark:hover:bg-slate-700/50 cursor-pointer flex items-center gap-3 transition-colors"
                                >
                                    {c.photoUrl ? (
                                        <img 
                                            src={c.photoUrl} 
                                            alt="" 
                                            onError={(e) => {
                                                (e.target as HTMLImageElement).src = '/assets/placeholder-avatar.svg';
                                            }}
                                            className="w-10 h-10 rounded-full object-cover bg-slate-200 dark:bg-slate-700 border border-slate-200 dark:border-slate-600" 
                                        />
                                    ) : (
                                        <div className="w-10 h-10 rounded-full bg-slate-200 dark:bg-slate-700 border border-slate-200 dark:border-slate-600 flex items-center justify-center text-slate-400">
                                            <User className="w-5 h-5 opacity-50" />
                                        </div>
                                    )}
                                    <div>
                                        <div className="flex items-center gap-2">
                                            <p className="text-sm font-bold text-slate-900 dark:text-slate-100">{c.name}</p>
                                            {(() => {
                                                if (!c.role) return null;
                                                const r = c.role.toLowerCase();
                                                if (r.includes('deputy chief minister') || r.includes('deputy cm')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded border bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border-indigo-300 dark:border-indigo-700/50">
                                                            Deputy CM
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('chief minister') && !r.includes('former')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded border bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-300 dark:border-amber-700/50">
                                                            Chief Minister
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('leader of opposition') || r.includes('lop')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded border bg-rose-500/10 text-rose-600 dark:text-rose-400 border-rose-300 dark:border-rose-700/50">
                                                            {r.includes('lok sabha') ? 'LOP (Lok Sabha)' : 'Leader of Opposition'}
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('mp') || r.includes('lok sabha')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded border bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-300 dark:border-emerald-700/50">
                                                            MP
                                                        </span>
                                                    );
                                                }
                                                return null;
                                            })()}
                                        </div>
                                        <p className="text-xs text-slate-500 dark:text-slate-400">{c.constituencyName} • {c.party} {c.state ? `(${c.state})` : ''}</p>
                                    </div>
                                </li>
                            ))}
                        </motion.ul>
                    )}
                </AnimatePresence>
            </div>
        </motion.div>
    );
};
