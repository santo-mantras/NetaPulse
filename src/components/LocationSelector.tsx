import React, { useState, useEffect, useMemo } from 'react';
import type { LocationHierarchy, CandidateProfile } from '../types/governance';
import { Search, MapPin, User, RotateCcw, X, Filter, ShieldCheck, AlertCircle } from 'lucide-react';
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
    
    // Multi-Filter states
    const [genderFilter, setGenderFilter] = useState<'ALL' | 'FEMALE' | 'MALE'>('ALL');
    const [partyFilter, setPartyFilter] = useState<string>('ALL');
    const [casesFilter, setCasesFilter] = useState<'ALL' | 'CLEAN' | 'ACTIVE'>('ALL');
    const [roleFilter, setRoleFilter] = useState<'ALL' | 'PM' | 'UNION' | 'CM' | 'DCM' | 'LOP' | 'MP' | 'MLA'>('ALL');

    // Autocomplete state
    const [suggestions, setSuggestions] = useState<CandidateProfile[]>([]);
    const [showSuggestions, setShowSuggestions] = useState(false);

    // Available top parties derived dynamically
    const topParties = useMemo(() => {
        const counts: Record<string, number> = {};
        candidates.forEach(c => {
            if (c.party) {
                counts[c.party] = (counts[c.party] || 0) + 1;
            }
        });
        return Object.entries(counts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 10)
            .map(([party]) => party);
    }, [candidates]);

    const activeFiltersCount = useMemo(() => {
        let count = 0;
        if (genderFilter !== 'ALL') count++;
        if (partyFilter !== 'ALL') count++;
        if (casesFilter !== 'ALL') count++;
        if (roleFilter !== 'ALL') count++;
        return count;
    }, [genderFilter, partyFilter, casesFilter, roleFilter]);

    // Helper to score executive leadership priority
    const getRoleExecutiveScore = (role?: string) => {
        if (!role) return 0;
        const r = role.toLowerCase();
        if (r.includes('prime minister')) return -15; // Top national priority (e.g. Narendra Modi)
        if (r.includes('union') || r.includes('cabinet minister')) return -8; // Union Cabinet (Amit Shah, Rajnath Singh, Nitin Gadkari)
        if (r.includes('chief minister') && !r.includes('former')) return -6; // State CMs
        if (r.includes('leader of opposition') || r.includes('lop')) return -4;
        if (r.includes('deputy')) return -3;
        if (r.includes('mp') || r.includes('lok sabha')) return -2;
        return 0;
    };

    // Multi-filter evaluation helper
    const applyFilters = (
        query: string,
        gFilter: 'ALL' | 'FEMALE' | 'MALE',
        pFilter: string,
        cFilter: 'ALL' | 'CLEAN' | 'ACTIVE',
        rFilter: 'ALL' | 'PM' | 'UNION' | 'CM' | 'DCM' | 'LOP' | 'MP' | 'MLA'
    ) => {
        const q = query.toLowerCase().trim();
        const hasQuery = q.length > 0;
        const hasActiveFilter = gFilter !== 'ALL' || pFilter !== 'ALL' || cFilter !== 'ALL' || rFilter !== 'ALL';

        if (!hasQuery && !hasActiveFilter) {
            setSuggestions([]);
            setShowSuggestions(false);
            return;
        }

        const matches = candidates.filter(c => {
            // 1. Text Query Filter
            if (hasQuery) {
                const nameMatch = c.name.toLowerCase().includes(q);
                const constMatch = c.constituencyName.toLowerCase().includes(q);
                const partyMatch = c.party && c.party.toLowerCase().includes(q);
                const stateMatch = c.state && c.state.toLowerCase().includes(q);
                if (!nameMatch && !constMatch && !partyMatch && !stateMatch) return false;
            }

            // 2. Gender Filter
            if (gFilter === 'FEMALE' && c.gender !== 'Female') return false;
            if (gFilter === 'MALE' && c.gender !== 'Male') return false;

            // 3. Party Filter
            if (pFilter !== 'ALL' && c.party !== pFilter) return false;

            // 4. Criminal Cases Filter
            if (cFilter === 'CLEAN' && (c.criminalCasesCount || 0) > 0) return false;
            if (cFilter === 'ACTIVE' && (c.criminalCasesCount || 0) === 0) return false;

            // 5. Role Filter
            if (rFilter !== 'ALL') {
                const roleLower = (c.role || '').toLowerCase();
                if (rFilter === 'PM' && !roleLower.includes('prime minister')) return false;
                if (rFilter === 'UNION' && !roleLower.includes('union')) return false;
                if (rFilter === 'CM' && (!roleLower.includes('chief minister') || roleLower.includes('deputy') || roleLower.includes('former'))) return false;
                if (rFilter === 'DCM' && !roleLower.includes('deputy')) return false;
                if (rFilter === 'LOP' && (!roleLower.includes('opposition') && !roleLower.includes('lop'))) return false;
                if (rFilter === 'MP' && !roleLower.includes('mp') && !roleLower.includes('lok sabha')) return false;
                if (rFilter === 'MLA' && c.role !== 'MLA') return false;
            }

            return true;
        }).sort((a, b) => {
            if (hasQuery) {
                const aNameLower = a.name.toLowerCase();
                const bNameLower = b.name.toLowerCase();
                // Check if full name starts with query (-10), or any word in name starts with query (-6) e.g. "Modi" in "Narendra Modi"
                const aNameStart = aNameLower.startsWith(q) ? -10 : (aNameLower.split(' ').some(w => w.startsWith(q)) ? -6 : 0);
                const bNameStart = bNameLower.startsWith(q) ? -10 : (bNameLower.split(' ').some(w => w.startsWith(q)) ? -6 : 0);
                
                const aRoleWeight = getRoleExecutiveScore(a.role);
                const bRoleWeight = getRoleExecutiveScore(b.role);
                return (aNameStart + aRoleWeight) - (bNameStart + bRoleWeight);
            }
            // If no text query, sort by executive leadership first, then alphabetical
            const aRoleWeight = getRoleExecutiveScore(a.role);
            const bRoleWeight = getRoleExecutiveScore(b.role);
            if (aRoleWeight !== bRoleWeight) return aRoleWeight - bRoleWeight;
            return a.name.localeCompare(b.name);
        }).slice(0, 15);

        setSuggestions(matches);
        setShowSuggestions(true);
    };

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
        setGenderFilter('ALL');
        setPartyFilter('ALL');
        setCasesFilter('ALL');
        setRoleFilter('ALL');
        onSearch('');
        setShowSuggestions(false);
    };

    const handleClearFilters = () => {
        setGenderFilter('ALL');
        setPartyFilter('ALL');
        setCasesFilter('ALL');
        setRoleFilter('ALL');
        applyFilters(searchQuery, 'ALL', 'ALL', 'ALL', 'ALL');
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
        applyFilters(value, genderFilter, partyFilter, casesFilter, roleFilter);
    };

    const handleClearSearch = () => {
        setSearchQuery('');
        onSearch('');
        if (activeFiltersCount > 0) {
            applyFilters('', genderFilter, partyFilter, casesFilter, roleFilter);
        } else {
            setShowSuggestions(false);
        }
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

            <div className="relative z-50 space-y-3">
                <div className="relative">
                    <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                        <Search className="w-5 h-5 text-slate-400" />
                    </div>
                    <input 
                        type="text" 
                        value={searchQuery}
                        onChange={(e) => handleSearchInput(e.target.value)}
                        onFocus={() => { if (searchQuery.trim().length > 0 || activeFiltersCount > 0) setShowSuggestions(true); }}
                        onBlur={() => setTimeout(() => setShowSuggestions(false), 250)}
                        className="block w-full p-3.5 pl-10 pr-10 text-sm text-slate-900 border border-slate-300 rounded-xl bg-slate-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-slate-800 dark:border-slate-700 dark:placeholder-slate-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 outline-none transition-all shadow-inner" 
                        placeholder="Search MP/MLA by name, constituency, or use filters below..." 
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
                </div>

                {/* Multi-Filter Toolbar */}
                <div className="flex flex-wrap items-center gap-2 pt-1 border-t border-slate-100 dark:border-slate-800/80">
                    <div className="flex items-center gap-1 text-[11px] font-bold text-slate-500 dark:text-slate-400 uppercase tracking-wider pr-1">
                        <Filter className="w-3.5 h-3.5 text-blue-500" />
                        <span>Filters:</span>
                    </div>

                    {/* Gender Filter Pills */}
                    <div className="flex items-center bg-slate-100 dark:bg-slate-800 p-0.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs">
                        <button
                            type="button"
                            onClick={() => {
                                setGenderFilter('ALL');
                                applyFilters(searchQuery, 'ALL', partyFilter, casesFilter, roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium transition-all ${
                                genderFilter === 'ALL'
                                    ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
                            }`}
                        >
                            All Gender
                        </button>
                        <button
                            type="button"
                            onClick={() => {
                                setGenderFilter('FEMALE');
                                applyFilters(searchQuery, 'FEMALE', partyFilter, casesFilter, roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium flex items-center gap-1 transition-all ${
                                genderFilter === 'FEMALE'
                                    ? 'bg-fuchsia-600 text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-fuchsia-600'
                            }`}
                        >
                            <span>♀</span> Women
                        </button>
                        <button
                            type="button"
                            onClick={() => {
                                setGenderFilter('MALE');
                                applyFilters(searchQuery, 'MALE', partyFilter, casesFilter, roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium flex items-center gap-1 transition-all ${
                                genderFilter === 'MALE'
                                    ? 'bg-blue-600 text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-blue-600'
                            }`}
                        >
                            <span>♂</span> Men
                        </button>
                    </div>

                    {/* Party Filter Dropdown */}
                    <div className="relative">
                        <select
                            value={partyFilter}
                            onChange={(e) => {
                                setPartyFilter(e.target.value);
                                applyFilters(searchQuery, genderFilter, e.target.value, casesFilter, roleFilter);
                            }}
                            className={`text-xs px-2.5 py-1.5 rounded-lg border font-medium outline-none transition-colors ${
                                partyFilter !== 'ALL'
                                    ? 'bg-blue-50 dark:bg-blue-900/30 border-blue-400 text-blue-700 dark:text-blue-300 font-bold'
                                    : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                            }`}
                        >
                            <option value="ALL">All Parties</option>
                            {topParties.map(p => (
                                <option key={p} value={p}>{p}</option>
                            ))}
                        </select>
                    </div>

                    {/* Criminal Case Filter Pills */}
                    <div className="flex items-center bg-slate-100 dark:bg-slate-800 p-0.5 rounded-lg border border-slate-200 dark:border-slate-700 text-xs">
                        <button
                            type="button"
                            onClick={() => {
                                setCasesFilter('ALL');
                                applyFilters(searchQuery, genderFilter, partyFilter, 'ALL', roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium transition-all ${
                                casesFilter === 'ALL'
                                    ? 'bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
                            }`}
                        >
                            All Records
                        </button>
                        <button
                            type="button"
                            onClick={() => {
                                setCasesFilter('CLEAN');
                                applyFilters(searchQuery, genderFilter, partyFilter, 'CLEAN', roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium flex items-center gap-1 transition-all ${
                                casesFilter === 'CLEAN'
                                    ? 'bg-emerald-600 text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-emerald-600'
                            }`}
                        >
                            <ShieldCheck className="w-3.5 h-3.5" /> Clean (0 Cases)
                        </button>
                        <button
                            type="button"
                            onClick={() => {
                                setCasesFilter('ACTIVE');
                                applyFilters(searchQuery, genderFilter, partyFilter, 'ACTIVE', roleFilter);
                            }}
                            className={`px-2 py-1 rounded-md font-medium flex items-center gap-1 transition-all ${
                                casesFilter === 'ACTIVE'
                                    ? 'bg-amber-600 text-white shadow-xs'
                                    : 'text-slate-600 dark:text-slate-400 hover:text-amber-600'
                            }`}
                        >
                            <AlertCircle className="w-3.5 h-3.5" /> Declared Cases
                        </button>
                    </div>

                    {/* Role Filter Dropdown */}
                    <div className="relative">
                        <select
                            value={roleFilter}
                            onChange={(e) => {
                                setRoleFilter(e.target.value as any);
                                applyFilters(searchQuery, genderFilter, partyFilter, casesFilter, e.target.value as any);
                            }}
                            className={`text-xs px-2.5 py-1.5 rounded-lg border font-medium outline-none transition-colors ${
                                roleFilter !== 'ALL'
                                    ? 'bg-indigo-50 dark:bg-indigo-900/30 border-indigo-400 text-indigo-700 dark:text-indigo-300 font-bold'
                                    : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                            }`}
                        >
                            <option value="ALL">All Roles</option>
                            <option value="PM">Prime Minister</option>
                            <option value="UNION">Union Minister</option>
                            <option value="CM">Chief Minister</option>
                            <option value="DCM">Deputy CM</option>
                            <option value="LOP">Leader of Opposition</option>
                            <option value="MP">MP (Lok Sabha)</option>
                            <option value="MLA">MLA (Assembly)</option>
                        </select>
                    </div>

                    {/* Reset Filters button if active */}
                    {activeFiltersCount > 0 && (
                        <button
                            type="button"
                            onClick={handleClearFilters}
                            className="text-xs px-2.5 py-1 rounded-lg bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 border border-rose-200 dark:border-rose-800 hover:bg-rose-100 font-semibold transition-colors flex items-center gap-1"
                            title="Reset all active filters"
                        >
                            <RotateCcw className="w-3 h-3" />
                            <span>Reset ({activeFiltersCount})</span>
                        </button>
                    )}
                </div>
                
                <AnimatePresence>
                    {showSuggestions && suggestions.length > 0 && (
                        <motion.ul 
                            initial={{ opacity: 0, y: -10 }}
                            animate={{ opacity: 1, y: 0 }}
                            exit={{ opacity: 0, y: -10 }}
                            className="absolute z-50 w-full mt-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl shadow-2xl max-h-84 overflow-auto divide-y divide-slate-100 dark:divide-slate-700/50"
                        >
                            <div className="px-4 py-2 bg-slate-50 dark:bg-slate-800/90 text-[11px] font-bold text-slate-500 uppercase tracking-wider flex items-center justify-between border-b border-slate-100 dark:border-slate-700">
                                <span>Found {suggestions.length} Matches</span>
                                <span className="text-[10px] text-slate-400 normal-case">Click to load profile & constituency</span>
                            </div>
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
                                            className="w-10 h-10 rounded-full object-cover bg-slate-200 dark:bg-slate-700 border border-slate-200 dark:border-slate-600 shrink-0" 
                                        />
                                    ) : (
                                        <div className="w-10 h-10 rounded-full bg-slate-200 dark:bg-slate-700 border border-slate-200 dark:border-slate-600 flex items-center justify-center text-slate-400 shrink-0">
                                            <User className="w-5 h-5 opacity-50" />
                                        </div>
                                    )}
                                    <div className="flex-1 min-w-0">
                                        <div className="flex flex-wrap items-center gap-1.5">
                                            <p className="text-sm font-bold text-slate-900 dark:text-slate-100 truncate">{c.name}</p>
                                            
                                            {/* Gender Badge */}
                                            {c.gender === 'Female' ? (
                                                <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-fuchsia-500/10 text-fuchsia-600 dark:text-fuchsia-400 border-fuchsia-300 dark:border-fuchsia-700/50">
                                                    ♀ Female
                                                </span>
                                            ) : (
                                                <span className="text-[10px] font-medium px-1.5 py-0.2 rounded border bg-slate-500/10 text-slate-600 dark:text-slate-400 border-slate-200 dark:border-slate-700">
                                                    ♂ Male
                                                </span>
                                            )}

                                            {/* Executive Role Badge */}
                                            {(() => {
                                                if (!c.role) return null;
                                                const r = c.role.toLowerCase();
                                                if (r.includes('prime minister')) {
                                                    return (
                                                        <span className="text-[10px] font-extrabold px-1.5 py-0.2 rounded border bg-amber-500/20 text-amber-700 dark:text-amber-300 border-amber-400/60 shadow-xs">
                                                            🇮🇳 Prime Minister
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('union')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-purple-500/15 text-purple-700 dark:text-purple-300 border-purple-400/50">
                                                            Union Minister
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('deputy chief minister') || r.includes('deputy cm')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border-indigo-300 dark:border-indigo-700/50">
                                                            Deputy CM
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('chief minister') && !r.includes('former')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-300 dark:border-amber-700/50">
                                                            Chief Minister
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('leader of opposition') || r.includes('lop')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-rose-500/10 text-rose-600 dark:text-rose-400 border-rose-300 dark:border-rose-700/50">
                                                            {r.includes('lok sabha') ? 'LOP (Lok Sabha)' : 'Leader of Opposition'}
                                                        </span>
                                                    );
                                                }
                                                if (r.includes('mp') || r.includes('lok sabha')) {
                                                    return (
                                                        <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-300 dark:border-emerald-700/50">
                                                            MP
                                                        </span>
                                                    );
                                                }
                                                return null;
                                            })()}

                                            {/* Criminal Case Tag */}
                                            {(c.criminalCasesCount || 0) === 0 ? (
                                                <span className="text-[10px] font-medium px-1.5 py-0.2 rounded border bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-300 dark:border-emerald-800">
                                                    0 Cases
                                                </span>
                                            ) : (
                                                <span className="text-[10px] font-bold px-1.5 py-0.2 rounded border bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-300 dark:border-amber-800">
                                                    {c.criminalCasesCount} {c.criminalCasesCount === 1 ? 'Case' : 'Cases'}
                                                </span>
                                            )}
                                        </div>
                                        <p className="text-xs text-slate-500 dark:text-slate-400 truncate mt-0.5">
                                            {c.constituencyName} • {c.party} {c.state ? `(${c.state})` : ''}
                                        </p>
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
