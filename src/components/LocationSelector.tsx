import React, { useState, useEffect } from 'react';
import type { LocationHierarchy, CandidateProfile } from '../types/governance';
import { Search, MapPin } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface LocationSelectorProps {
    locations: LocationHierarchy[];
    candidates: CandidateProfile[];
    onLocationSelect: (location: LocationHierarchy) => void;
    onSearch: (query: string) => void;
}

export const LocationSelector: React.FC<LocationSelectorProps> = ({ locations, candidates, onLocationSelect, onSearch }) => {
    // Unique lists
    const states = Array.from(new Set(locations.map(l => l.stateName)));

    const [selectedState, setSelectedState] = useState('Maharashtra');
    const [selectedDistrict, setSelectedDistrict] = useState('Pune');
    const [selectedConstituency, setSelectedConstituency] = useState('AC-208 Vadgaon Sheri');
    const [searchQuery, setSearchQuery] = useState('');
    
    // Autocomplete state
    const [suggestions, setSuggestions] = useState<CandidateProfile[]>([]);
    const [showSuggestions, setShowSuggestions] = useState(false);

    const availableDistricts = Array.from(new Set(
        locations.filter(l => l.stateName === selectedState).map(l => l.districtName)
    ));

    const availableConstituencies = locations
        .filter(l => l.stateName === selectedState && l.districtName === selectedDistrict)
        .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);

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

    // Handle cascading resets
    const handleStateChange = (state: string) => {
        setSelectedState(state);
        const newDistricts = Array.from(new Set(locations.filter(l => l.stateName === state).map(l => l.districtName)));
        const firstDist = newDistricts[0] || '';
        setSelectedDistrict(firstDist);

        const newConst = locations
            .filter(l => l.stateName === state && l.districtName === firstDist)
            .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);
        setSelectedConstituency(newConst[0] || '');
    };

    const handleDistrictChange = (dist: string) => {
        setSelectedDistrict(dist);
        const newConst = locations
            .filter(l => l.stateName === selectedState && l.districtName === dist)
            .map(l => `${l.assemblyConstituencyCode} ${l.assemblyConstituencyName}`);
        setSelectedConstituency(newConst[0] || '');
    };

    const handleSearchInput = (value: string) => {
        setSearchQuery(value);
        onSearch(value);
        
        if (value.trim().length > 0) {
            const q = value.toLowerCase().trim();
            const matches = candidates.filter(c => c.name.toLowerCase().includes(q) || c.constituencyName.toLowerCase().includes(q)).slice(0, 5);
            setSuggestions(matches);
            setShowSuggestions(true);
        } else {
            setShowSuggestions(false);
        }
    };

    const handleSelectSuggestion = (candidate: CandidateProfile) => {
        setSearchQuery(candidate.name);
        setShowSuggestions(false);
        onSearch(candidate.name);
        
        const loc = locations.find(l => l.assemblyConstituencyName === candidate.constituencyName);
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
            <div className="flex items-center gap-3 mb-6 text-slate-800 dark:text-slate-100">
                <div className="p-2 bg-blue-100 dark:bg-blue-900/50 rounded-lg text-blue-600 dark:text-blue-400">
                    <MapPin className="w-5 h-5" />
                </div>
                <h2 className="text-xl font-bold">Select Constituency</h2>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                <div className="flex flex-col gap-1.5">
                    <label className="text-xs font-semibold text-slate-500 uppercase tracking-wider">State / UT</label>
                    <select 
                        value={selectedState} 
                        onChange={(e) => handleStateChange(e.target.value)}
                        className="bg-slate-50 dark:bg-slate-800 border border-slate-300 dark:border-slate-700 text-slate-900 dark:text-slate-100 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 transition-colors outline-none"
                    >
                        {states.map(s => <option key={s} value={s}>{s}</option>)}
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
                    className="block w-full p-4 pl-10 text-sm text-slate-900 border border-slate-300 rounded-xl bg-slate-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-slate-800 dark:border-slate-700 dark:placeholder-slate-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 outline-none transition-all shadow-inner" 
                    placeholder="Or search by MP/MLA / Candidate Name..." 
                />
                
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
                                    <img src={c.photoUrl} alt="" className="w-10 h-10 rounded-full object-cover bg-slate-200 dark:bg-slate-700 border border-slate-200 dark:border-slate-600" />
                                    <div>
                                        <p className="text-sm font-bold text-slate-900 dark:text-slate-100">{c.name}</p>
                                        <p className="text-xs text-slate-500 dark:text-slate-400">{c.constituencyName} • {c.party}</p>
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
