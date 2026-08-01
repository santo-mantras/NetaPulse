# Jumlebaaz: Comprehensive Product Specification & Implementation Roadmap

## 1. Project Overview & Product Vision
**Jumlebaaz** is an open-access, non-partisan, mobile-first civic technology platform designed to bring citizens closer to their elected political representatives (Members of Parliament - MPs, Members of Legislative Assemblies - MLAs, and Municipal Corporators) [6]. 

By synthesizing official government disclosures, legislative logs, and mainstream investigative journalism into intuitive visual dashboards, Jumlebaaz transforms complex, fragmented political data into an easy-to-use, device-agnostic tool that boosts civic awareness and political engagement.

---

## 2. Core Architectural Principles & User Constraints

### A. Manual Location Selection (Strictly No Browser Geolocation)
* **Rationale**: Automatic GPS coordinate lookup is frequently rejected by users, inaccurate near constituency boundaries, or prone to CORS/API latency.
* **Implementation**: Location is established via a cascading dropdown workflow indexed by official **Local Government Directory (LGD) codes** [5, 25]:
  $$\text{State / UT} \longrightarrow \text{District} \longrightarrow \text{Assembly Constituency (AC) / Parliamentary Constituency (PC)}$$
* **Secondary Lookup**: A direct search bar allowing voters to search by candidate, MP, or MLA name.

### B. Map-Free Data Visualization
* **Rationale**: Rendering GIS boundary shapefiles (Mapbox, Leaflet, deck.gl, TopoJSON) introduces heavy bundle overhead (>10 MB), projection issues, touch gesture conflicts, and missing boundary bugs.
* **Visual Substitutes**: Interactive UI components built with **Recharts** (SVG) and **shadcn/ui** primitives:
  * **Legislative Pulse Wheels**: Radar/spider charts mapping parliamentary activity.
  * **Asset Growth Bars**: Visual stacked bar charts tracking net-worth evolution across election cycles.
  * **Promise Outcome Badges**: Status cards categorizing manifesto promises.

### C. Cross-Device & Mobile-First Optimization
* **Responsive Layouts**: Utility-first grid systems (Tailwind CSS) that automatically adapt from multi-column desktop dashboards to single-column, touch-optimized mobile drawers and swipeable cards.
* **Lightweight Footprint**: Eliminating spatial boundary files keeps the initial JavaScript bundle size under **150 KB**, ensuring instant loads on 3G/4G mobile networks.

### D. Primary Official Data vs. Secondary Media Integration
* **Primary Sourcing (Ground Truth)**: Official Election Commission of India (ECI) candidate affidavits [2, 3, 30], Parliamentary activity logs via PRS Legislative Research [28, 36], and LGD codes [5, 31].
* **Secondary Sourcing (Investigative Context)**: Investigative coverage from major dailies (*The Times of India*, *The Hindu*, *The Indian Express*, *Mint*) covering asset growth audits, court case developments, and sting operations.
* **Trust Verification**: Media articles carry explicit **"Trust Verification Badges"** and citation drawers cross-referencing news claims with primary ECI charge sheets or official records [45].

### E. Antigravity Runtime & Hosting Philosophy
* **Pre-Rendered SPA**: The client operates as a read-only React Single Page Application (SPA) served via global CDNs [6].
* **Zero Session State Overhead**: By eliminating real-time database writes and user authentication during browsing, hosting costs remain virtually zero while guaranteeing 100% uptime during high-traffic election spikes [6].

---

## 3. Detailed Feature Modules & UI Layouts

```
+-------------------------------------------------------------------+
|                       JUMLEBAAZ HUB HEADER                        |
|  [Ticker]: Lok Sabha Winter Session: Avg MP Attendance is 82%     |
+-------------------------------------------------------------------+
|  LOCATION SELECTOR (LGD-Indexed Cascading Dropdowns)              |
|  [Select State v]   [Select District v]   [Select Constituency v] |
+-------------------------------------------------------------------+
|  REPRESENTATIVE DOSSIER: Rajesh Kumar (AC-208 Vadgaon Sheri)      |
|  Party: XYZ Party | Role: MLA | Attendance: 88% | Questions: 42   |
+-------------------------------------------------------------------+
|  LEGISLATIVE PULSE (Radar)       |  ASSET DISCLOSURE (Bar)        |
|      Attendance (88%)            |   Assets: ₹14.2 Cr            |
|         /\                       |   Liabilities: ₹1.1 Cr        |
|   Bills/  \ Questions            |   [ Visual Stacked Bar ]       |
|   (2) /____\ (42)                |                                |
+-------------------------------------------------------------------+
|  PROMISE TRACKER MATRIX (5 Met | 4 Pending | 3 Unfulfilled/Jumla)  |
+-------------------------------------------------------------------+
|  INVESTIGATIVE NEWS SPOTLIGHT (TOI / Hindu / Express / Mint)      |
|  • [Mint] "Asset audit shows +140% net-worth growth (2019-2024)" |
|  [ Trust Badge: Cross-Referenced with ECI Affidavit ]             |
+-------------------------------------------------------------------+
```

### Module 1: Location Selector & Civic Pulse Header
* **LGD Cascading Dropdowns**: Select State $\rightarrow$ Select District $\rightarrow$ Select Assembly/Parliamentary Constituency.
* **Civic Pulse Ticker**: Scrollable highlight bar showcasing recent parliamentary session averages and verified news alerts.
* **Direct Representative Search**: Instant fuzzy-search input for searching leaders by name.

### Module 2: Interactive Representative Dossier
* **Header Profile**: Candidate photo, party affiliation, tenure, and constituency LGD badge.
* **Legislative Activity Radar Chart (Recharts)**: Plots 5 core axes against state and national benchmarks:
  1. Parliamentary Attendance %
  2. Questions Raised
  3. Private Member Bills Introduced
  4. Committee Participation
  5. Local Area Development (MPLAD/MLALAD) Fund Utilization
* **Financial Disclosure Stacked Bar**: Visualizes Movable Assets, Immovable Assets, Liabilities, and Net Worth Growth between election terms.
* **Legal & Affidavit Drawer**: Categorized breakdown of declared criminal charges, case numbers, IPC sections, and direct links to official scanned ECI PDF affidavits [2, 3].

### Module 3: Promise Tracker Matrix (Manifesto vs. Outcomes)
* **Categorized Status Badges**:
  * **Fulfilled** (Green): Verified via gazette notifications or municipal audits.
  * **In Progress** (Amber): Active construction or partial budget allocation.
  * **Unfulfilled / Jumla** (Red): Unstarted or abandoned campaign promises.
  * **Insufficient Data** (Gray): Pending verification.

### Module 4: Media & Investigative Spotlight
* **Mainstream News Stream**: Curated investigative reports from *The Hindu*, *The Indian Express*, *Times of India*, and *Mint*.
* **Trust & Verification Badges**: Indicates whether the news story is cross-referenced with official court filings or ECI disclosures.

### Module 5: Side-by-Side Candidate Comparison Engine
* A swipeable mobile modal enabling voters during election seasons to compare 2 or 3 contesting candidates across:
  * Educational Qualifications
  * Declared Assets vs. Liabilities
  * Criminal Cases & Legal Background
  * Legislative Performance Index

---

## 4. Technical Stack & Data Schema

### Technology Stack
* **Frontend Framework**: React 19 + Vite + TypeScript [22]
* **Styling & Components**: Tailwind CSS v4, shadcn/ui, Radix UI Primitives, Lucide React [22]
* **Data Visualization**: Recharts (SVG-based) [8, 9, 10]
* **Data Format**: Pre-compiled, read-optimized static JSON files

### Data Schema Definition (`src/types/governance.ts`)

```typescript
export interface LocationHierarchy {
  stateLgdCode: number;
  stateName: string;
  districtLgdCode: number;
  districtName: string;
  assemblyConstituencyCode: string;
  assemblyConstituencyName: string;
  parliamentaryConstituencyCode: string;
  parliamentaryConstituencyName: string;
}

export interface CandidateProfile {
  id: string;
  name: string;
  role: 'MLA' | 'MP' | 'Corporator';
  party: string;
  photoUrl: string;
  constituencyName: string;
  attendancePercentage: number;
  questionsAsked: number;
  privateMemberBills: number;
  declaredAssetsINR: number;
  declaredLiabilitiesINR: number;
  criminalCasesCount: number;
  criminalCasesDetails: {
    charges: string;
    caseNumber: string;
    status: string;
  }[];
  education: string;
  affidavitPdfUrl: string;
}

export interface CampaignPromise {
  id: string;
  title: string;
  category: string;
  status: 'Fulfilled' | 'In Progress' | 'Unfulfilled' | 'Insufficient Data';
  declaredInManifesto: string;
  verifiedOutcome: string;
  sourceCitation: string;
}

export interface NewsReport {
  id: string;
  publisher: 'The Hindu' | 'Times of India' | 'Indian Express' | 'Mint' | 'Other';
  title: string;
  summary: string;
  url: string;
  publishedDate: string;
  category: 'Asset Growth' | 'Court Case' | 'Sting/Investigation' | 'Local Activity';
  verificationStatus: 'Cross-Referenced with Affidavit' | 'Under Review' | 'Media Report';
}
```

---

## 5. Development Setup & Execution Strategy in Antigravity IDE

### Execution Steps
1. **Scaffold Vite React Workspace**:
   ```bash
   npm create vite@latest jumlebaaz -- --template react-ts
   cd jumlebaaz
   npm install recharts lucide-react clsx tailwind-merge
   npm install -D tailwindcss postcss autoprefixer
   npx tailwindcss init -p
   ```
2. **Populate Interfaces & Static Data**: Place `src/types/governance.ts` and `src/data/mockGovernanceData.ts`.
3. **AI Model Selection Strategy**:
   * **Initial Scaffolding & Recharts Setup**: Use a high-capacity model (e.g., **Gemini 3.1 Pro** / **Claude 3.5 Sonnet**) to ensure clean state logic for cascading selectors and error-free SVG charts.
   * **Styling & Iterative Customization**: Use **Gemini 3.1 Pro Low** for fast, low-cost Tailwind adjustments, card layout tweaks, and mock data expansions.
4. **Launch & Verify**:
   ```bash
   npm run dev
   ```
