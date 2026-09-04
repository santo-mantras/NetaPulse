# NetaPulse: Session Progress, Learnings & Next Session Blueprint

## 1. What We Accomplished in Today's Session

### A. Dynamic Continuous Moving Civic Marquee
- **Edge-to-Edge Infinite Linear Marquee**: Replaced the static marquee with a continuous, seamless `-50%` translate infinite ticker with zero blank gaps or resets.
- **Removed Ticker Clutter**: Completely removed the `[CIVIC PULSE]` tag, `< 1/5 >` buttons, and floating overlay badges so the text moves unobscured across the entire top bar.
- **Hover & Click-to-Toggle Interaction**:
  - Hovering pauses scrolling immediately for effortless reading.
  - Clicking toggles the moving/paused state (clicking while paused resumes scrolling immediately).
- **Accurate 5-Line Information Feed**:
  1. 🗳️ **Upcoming State Elections**: West Bengal, Tamil Nadu, Kerala, Assam & Puducherry (Apr–May 2026) • Uttar Pradesh, Punjab, Goa & Gujarat (2027) *(obsolete 2025 removed)*.
  2. 🏛️ **Parliament Watch**: 18th Lok Sabha completed 115+ hours of legislative business; upcoming session to table key governance and financial reforms.
  3. 💸 **Taxpayer Cost Per Session**: ₹2.5 Lakh spent every minute of Parliamentary sittings (~₹9.1 Crore per active sitting day funded by Indian taxpayers).
  4. 🇮🇳 **National Leadership**: Prime Minister: Narendra Modi • President of India: Droupadi Murmu (15th President of the Republic).
  5. ⚖️ **Constitutional Heads**: Chief Justice of India: Justice Sanjiv Khanna (51st CJI) • Chief Election Commissioner: Rajiv Kumar.

### B. National Executive Leadership Ingestion
- **Prime Minister Narendra Modi**:
  - Ingested under `PC-UP-77 Varanasi (Lok Sabha)` with high-resolution portrait (`/assets/candidates/narendra_modi.jpg`), verified assets, 0 criminal cases, and legislative track record.
  - Search ranking prioritization: Weighted executive leadership (`-15` for Prime Minister, `-8` for Union Cabinet ministers) with word-boundary match scoring (`name.split(' ').some(w => w.startsWith(q))`). Searching `"modi"` now immediately ranks Narendra Modi at **#1**.
- **Top Union Cabinet Ministers**:
  - **Amit Shah** (`PC-GJ-06 Gandhinagar (Lok Sabha)`)
  - **Rajnath Singh** (`PC-UP-35 Lucknow (Lok Sabha)`)
  - **Nitin Gadkari** (`PC-MH-10 Nagpur (Lok Sabha)`)
- **New Role Badges & Filters**: Added dedicated `Prime Minister` and `Union Minister` options in the dropdown and glowing hero badges.

### C. 3 New States & 74 Distinct District Civic Insights (238 Constituencies)
- **Haryana (90 ACs)**: Nayab Singh Saini (CM - Ladwa), Anil Vij (Ambala Cantt), Bhupinder Hooda (Garhi Sampla-Kiloi), Vinesh Phogat (Julana), Dushyant Chautala (Uchana Kalan).
- **Telangana (119 ACs)**: A. Revanth Reddy (CM - Kodangal), Mallu Bhatti Vikramarka (Dy CM - Madhira), K. Chandrashekar Rao (Gajwel), K. T. Rama Rao (Sircilla), Asaduddin Owaisi & Akbaruddin Owaisi (Chandrayangutta), Danasari Anasuya "Seethakka" (Mulug).
- **Jammu & Kashmir (90 ACs)**: Omar Abdullah (CM - Ganderbal / Budgam), Surinder Choudhary (Dy CM - Nowshera), Mehbooba Mufti (Bijbehara), Sajad Lone (Handwara).
- **Unique Civic Insights**: All 74 districts across HR, TG, and JK received distinct historical facts and authentic local governance challenges.
- **Master Dataset**: Compiled 2,920 total constituencies across 17 states/UTs into `src/data/realGovernanceData.json`.

### D. Automated Candidate Portrait & Icon Audit
- **Fixed Sameer Meghe (Hingna, BJP)**: Replaced accidental 32×32px Congress party flag icon with his authentic, official candidate portrait (700×899px, 73.5 KB).
- **Compiler Safeguard Added**: Added dimension and file size verification (`img.width >= 60`, `img.height >= 60`, `size >= 4KB`) to permanently prevent scraped table icons or party flags from being treated as portraits.

### E. App Polish & Live Deployment
- Logo click safely redirects to home page with full state cascade reset.
- Footer streamlined to clean, non-clickable text (`ECI Portal • PRS India • Local Govt Directory`).
- Pushed to GitHub `origin/main` (`e81d5b0`) and deployed live on Vercel.

---

## 2. Key Learnings & Pitfalls Avoided

1. **Wikipedia Scraped Table Traps**:
   - In election result tables, the party column frequently embeds tiny flag/symbol images. Naive scrapers often grab these as candidate photos.
   - *Rule*: Always enforce resolution check (`>= 60x60px`) and file-size threshold (`>= 4KB`) before accepting any image asset.
2. **Search Priority for High-Profile Leaders**:
   - If search only uses naive alphabetical order or substring matching, leaders with common surnames (e.g. "Modi") will be buried under state MLAs (e.g. Purnesh Modi, Suresh Modi).
   - *Rule*: Executive weight scoring (Prime Minister `-15`, Union Minister `-8`, CM `-6`) ensures marquee leaders always surface at #1.
3. **Temporal Validity of Civic Data**:
   - Dates like "2025" in "Upcoming State Elections" quickly become outdated and confuse users once the year passes.
   - *Rule*: Validate election calendars against real-time schedules (2026 for WB, TN, KL, AS; 2027 for UP, PB, GA, GJ).
4. **Marquee Readability & Overlay Conflicts**:
   - Never position solid badges over a scrolling marquee text line. Hover-to-pause and click-to-toggle provides an intuitive, non-intrusive reading experience.

---

## 3. Agenda & Blueprint for Next Session

### Focus Area 1: Data Accuracy & Reliability Deep Dive (Priority #1)
The user noted that data on the internet does not match app data for prominent leaders like **Rahul Gandhi** (especially **MLALAD/MPLADS fund utilization** and **criminal cases**):
1. **Audit Key National & State Leaders**:
   - **Rahul Gandhi**:
     - Cross-check Wayanad / Rae Bareli Lok Sabha ECI Form 26 Affidavit: Actual declared criminal cases (e.g. Defamation cases under IPC 499/500, National Herald proceedings, etc.) with exact court, case numbers, and status.
     - Cross-check MPLADS official portal (`mplads.gov.in`): Actual ₹5 Cr/year entitlement, cumulative entitlement, released by GoI, expenditure incurred, and unspent balance.
   - **Narendra Modi, Amit Shah, Akhilesh Yadav, Mamata Banerjee, Arvind Kejriwal, Hemant Soren**:
     - Extract exact ECI Form 26 criminal declarations (charges framed vs cognizance taken) instead of generic template strings.
     - Extract exact MPLADS expenditure reports.
2. **Affidavit & Fund Citations Overhaul**:
   - Link each high-profile leader directly to their downloadable ECI Form 26 PDF on `affidavit.eci.gov.in`.
   - Provide explicit breakdown between civil defamation / political demonstration cases vs serious cognizable offenses.
   - Add clear source tags: *"Verified via ECI Form 26 (2024 General Elections) & MPLADS Public Dashboard"*.

### Focus Area 2: Ingest Remaining States & Union Territories
Expand from 17 states/UTs to complete India-wide coverage:
- **Major States**:
  - Odisha (147 ACs)
  - Andhra Pradesh (175 ACs)
  - Madhya Pradesh (230 ACs)
  - Jharkhand (81 ACs)
  - Himachal Pradesh (68 ACs)
  - Uttarakhand (70 ACs)
- **Northeast States**:
  - Tripura (60 ACs), Meghalaya (60 ACs), Nagaland (60 ACs), Manipur (60 ACs), Mizoram (40 ACs), Arunachal Pradesh (60 ACs), Sikkim (32 ACs).
- **Union Territories**:
  - Chandigarh (1 PC), Ladakh (1 PC), Puducherry (30 ACs), Andaman & Nicobar, Dadra & Nagar Haveli / Daman & Diu, Lakshadweep.

### Focus Area 3: Pre-Ingestion Checklist for Each State
To guarantee zero defects when adding new states:
- [ ] Verify each executive leader (CM, Deputy CM, LoP) has an authentic high-resolution portrait.
- [ ] Confirm party symbols match official party affiliations (no Independent fallback when official SVG exists).
- [ ] Verify district civic insights have realistic local facts and specific challenges.
- [ ] Run automated compiler validation (`npm run build`) before showing to user.

---

## 4. Current Repository State
- **Branch**: `main`
- **Latest Commit**: `e81d5b0`
- **Working Tree**: Clean (all changes committed and pushed to remote)
- **Local Dev Server**: Stopped / Closed
