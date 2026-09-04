import { useState, useEffect } from 'react';
import { Moon, Sun, Activity } from 'lucide-react';
import { LocationSelector } from './components/LocationSelector';
import { CandidateDossier } from './components/CandidateDossier';
import { CandidateCompareModal } from './components/CandidateCompareModal';
import { NetaPulseLogo } from './components/NetaPulseLogo';
import { CivicPulseTicker } from './components/CivicPulseTicker';
import { mockLocations, mockCandidates, mockPromises, mockNews } from './data/dataAdapter';
import type { LocationHierarchy, CandidateProfile } from './types/governance';
import { motion } from 'framer-motion';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  // Default landing location: Assam Chief Minister Himanta Biswa Sarma (Jalukbari, Kamrup Metropolitan)
  const defaultLandingLoc = mockLocations.find(l => l.stateName === 'Assam' && l.assemblyConstituencyName === 'Jalukbari') || mockLocations[0];
  const [selectedLocation, setSelectedLocation] = useState<LocationHierarchy>(defaultLandingLoc);
  const [searchQuery, setSearchQuery] = useState('');
  const [isCompareModalOpen, setIsCompareModalOpen] = useState(false);
  const [resetKey, setResetKey] = useState(0);

  const handleHomeRedirect = (e: React.MouseEvent) => {
    e.preventDefault();
    setSearchQuery('');
    setSelectedLocation(defaultLandingLoc);
    setResetKey(prev => prev + 1);
    window.scrollTo({ top: 0, behavior: 'smooth' });
    window.history.pushState({}, '', '/');
  };

  // Toggle theme
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  // Derive which candidates to show based on location/search
  let primaryCandidate: CandidateProfile | null = null;
  let competitorCandidate: CandidateProfile | null = null;

  if (searchQuery.trim().length > 0) {
    const q = searchQuery.toLowerCase().trim();
    const searchResults = Object.values(mockCandidates).filter(c => 
      c.name.toLowerCase().includes(q) || 
      c.constituencyName.toLowerCase().includes(q)
    ).sort((a, b) => {
      const aNameLower = a.name.toLowerCase();
      const bNameLower = b.name.toLowerCase();
      const aNameStart = aNameLower.startsWith(q) ? -10 : (aNameLower.split(' ').some(w => w.startsWith(q)) ? -6 : 0);
      const bNameStart = bNameLower.startsWith(q) ? -10 : (bNameLower.split(' ').some(w => w.startsWith(q)) ? -6 : 0);

      const getRoleRank = (role?: string) => {
        if (!role) return 0;
        const r = role.toLowerCase();
        if (r.includes('prime minister')) return -15;
        if (r.includes('union') || r.includes('cabinet minister')) return -8;
        if (r.includes('chief minister') && !r.includes('former')) return -6;
        if (r.includes('leader of opposition') || r.includes('lop')) return -4;
        if (r.includes('deputy')) return -3;
        if (r.includes('mp') || r.includes('lok sabha')) return -2;
        return 0;
      };

      const aRoleWeight = getRoleRank(a.role);
      const bRoleWeight = getRoleRank(b.role);
      return (aNameStart + aRoleWeight) - (bNameStart + bRoleWeight);
    });
    
    if (searchResults.length > 0) {
      primaryCandidate = searchResults[0];
    }
    if (searchResults.length > 1) {
      competitorCandidate = searchResults[1];
    } else if (primaryCandidate) {
      const otherCandidates = Object.values(mockCandidates).filter(c => c.id !== primaryCandidate!.id && c.state === primaryCandidate!.state);
      if (otherCandidates.length > 0) {
        competitorCandidate = otherCandidates[0];
      }
    }
  } else {
    const locationCandidates = Object.values(mockCandidates).filter(c => 
      c.constituencyName === selectedLocation.assemblyConstituencyName &&
      (!c.state || !selectedLocation.stateName || c.state === selectedLocation.stateName)
    );
    
    if (locationCandidates.length > 0) {
      primaryCandidate = locationCandidates[0];
    }
    
    if (locationCandidates.length > 1) {
      competitorCandidate = locationCandidates[1];
    } else if (primaryCandidate) {
      // Deterministically pick another candidate in the same state/district as a competitor fallback
      const otherCandidates = Object.values(mockCandidates).filter(c => c.id !== primaryCandidate!.id && c.state === primaryCandidate!.state);
      if (otherCandidates.length > 0) {
        competitorCandidate = otherCandidates[0];
      }
    }
  }

  return (
    <div className="min-h-screen bg-slate-100 dark:bg-slate-950 transition-colors duration-300 font-sans selection:bg-blue-200 dark:selection:bg-blue-900">
      
      {/* Dynamic 5-Line Civic Pulse Ticker */}
      <CivicPulseTicker />

      {/* Header */}
      <header className="sticky top-0 z-30 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 transition-colors">
        <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
          <a 
            href="/"
            onClick={handleHomeRedirect}
            className="flex items-center gap-3 cursor-pointer group select-none focus:outline-none"
            title="NetaPulse Home"
          >
            <div className="transition-transform duration-200 group-hover:scale-105">
              <NetaPulseLogo className="w-10 h-10" />
            </div>
            <div>
              <h1 className="text-xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-blue-700 via-purple-600 to-indigo-700 dark:from-blue-400 dark:via-purple-400 dark:to-indigo-400 bg-[length:200%_auto] animate-gradient tracking-tight group-hover:opacity-90 transition-opacity">
                NetaPulse
              </h1>
              <p className="text-[10px] sm:text-xs font-bold text-slate-500 dark:text-slate-400 tracking-wide mt-0.5" title="Satyānna pramaditavyam - Do not deviate from the truth.">
                सत्यान्न प्रमदितव्यम्
              </p>
            </div>
          </a>

          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-full hover:bg-slate-200 dark:hover:bg-slate-800 text-slate-600 dark:text-slate-300 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Toggle Dark Mode"
          >
            {darkMode ? <Sun className="w-5 h-5" /> : <Moon className="w-5 h-5" />}
          </button>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-8 space-y-12">
        
        {/* Hero & Selector */}
        <section className="text-center space-y-6 pt-4 md:pt-8 relative z-50">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="max-w-2xl mx-auto">
            <h2 className="text-3xl md:text-5xl font-extrabold text-slate-900 dark:text-white tracking-tight mb-4">
              Hold Your Leaders <span className="text-blue-600 dark:text-blue-400">Accountable.</span>
            </h2>
            <p className="text-sm md:text-base text-slate-600 dark:text-slate-400 font-medium">
              Access verified affidavits, track manifesto promises, and analyze legislative performance in real-time. Zero bias. 100% data-driven.
            </p>
          </motion.div>

          <LocationSelector 
            key={resetKey}
            locations={mockLocations} 
            candidates={Object.values(mockCandidates)}
            onLocationSelect={setSelectedLocation} 
            onSearch={setSearchQuery} 
          />
        </section>

        {/* Candidate Dossier View */}
        <section className="relative z-10">
          {primaryCandidate ? (
            <CandidateDossier 
              candidate={primaryCandidate} 
              allCandidates={Object.values(mockCandidates)}
              promises={mockPromises[primaryCandidate.id] || []}
              news={mockNews[primaryCandidate.id] || []}
              location={selectedLocation}
              onCompare={() => setIsCompareModalOpen(true)}
            />
          ) : (
            <div className="text-center py-16 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-8 shadow-sm">
              <Activity className="w-12 h-12 text-slate-400 mx-auto mb-3 animate-pulse" />
              <p className="text-lg font-bold text-slate-700 dark:text-slate-300">No candidate record found for this constituency selection.</p>
              <p className="text-sm text-slate-500 mt-1">Try selecting another constituency or state from the dropdown.</p>
            </div>
          )}
        </section>

      </main>

      {/* Footer */}
      <footer className="mt-20 border-t border-slate-200 dark:border-slate-800 bg-white/50 dark:bg-slate-900/50 backdrop-blur-md py-8">
        <div className="max-w-6xl mx-auto px-4 text-center space-y-4">
          <p className="text-xs text-slate-500 dark:text-slate-400 font-medium max-w-3xl mx-auto leading-relaxed">
            Disclaimer: All data is aggregated from open public domains including the Election Commission of India (ECI), PRS Legislative Research, and mainstream media outlets. NetaPulse does not alter primary affidavit data.
          </p>
          <div className="flex flex-wrap items-center justify-center gap-3 text-xs font-bold text-slate-400 dark:text-slate-500 select-none">
            <span>ECI Portal</span>
            <span className="text-slate-300 dark:text-slate-600">•</span>
            <span>PRS India</span>
            <span className="text-slate-300 dark:text-slate-600">•</span>
            <span>Local Govt Directory</span>
          </div>
        </div>
      </footer>

      {/* Modals */}
      {primaryCandidate && competitorCandidate && (
        <CandidateCompareModal 
          isOpen={isCompareModalOpen} 
          onClose={() => setIsCompareModalOpen(false)} 
          candidateA={primaryCandidate}
          initialCandidateB={competitorCandidate}
          allCandidates={Object.values(mockCandidates)}
          locations={mockLocations}
        />
      )}

    </div>
  );
}

export default App;
