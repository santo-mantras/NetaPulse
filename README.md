---
title: NetaPulse
emoji: 🗳️
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
---

# NetaPulse 🗳️

**सत्यान्न प्रमदितव्यम् — Transparent Governance & Civic Accountability Platform**

NetaPulse empowers Indian citizens to audit elected representatives (MLAs/MPs) across 476 constituencies in **Maharashtra, Uttar Pradesh, Karnataka, and Punjab** using verified data from Election Commission of India (ECI) affidavits, state legislative secretariats, and civic development fund records.

---

## 🌟 Key Features

- 🏛️ **Multi-State Representation**: Comprehensive constituency and district registry across **Maharashtra (274 seats)**, **Uttar Pradesh (72 seats)**, **Karnataka (71 seats)**, and **Punjab (59 seats)**.
- 💰 **MLA-LADS Development Fund Audit**: Real-time allocation vs utilization tracking, category breakdown (*Roads, Water, Smart Labs, Healthcare*), and state benchmark comparisons.
- ⚖️ **Legal Disclosures & Wealth Breakdown**: Declared movable/immovable assets, liabilities, and verified criminal case records from ECI Form 26 affidavits.
- 📊 **State Seats Analysis**: Total assembly seats, majority thresholds, Lok Sabha distribution, and live assembly party composition.
- 🔍 **Interactive Side-by-Side Comparison**: Compare track records, legislative attendance, and wealth across any candidate in India with cascading state/district filters.
- 📰 **Media Spotlight**: Dynamic news reports and direct verified news search archives.
- 💓 **Beating ECG Pulse Visuals & Dark Mode**: Modern design system with responsive animations and glassmorphism.

---

## 🛠️ Tech Stack

- **Frontend**: React 18 + TypeScript + Vite 8
- **Styling**: Tailwind CSS + Framer Motion + Lucide Icons
- **Data Engineering**: Python ETL pipeline with Master CSV Ground Truth
- **Deployment**: Containerized Docker on Hugging Face Spaces & GitHub

---

## 🚀 Local Development

```bash
# Clone the repository
git clone https://github.com/santo-mantras/NetaPulse.git
cd NetaPulse

# Install dependencies
npm install

# Run Vite dev server
npm run dev
```

---

## 🐳 Docker Deployment

```bash
# Build Docker image
docker build -t netapulse .

# Run container on port 7860
docker run -p 7860:7860 netapulse
```

---

## 📚 Data Provenance & Sources

All data is compiled strictly from public records without altering primary affidavit information:
- **Election Commission of India (ECI)**: Form 26 affidavits & candidate declarations
- **State Legislative Assemblies & Parliament**: Question hours and attendance records
- **State Planning & Finance Departments**: MLA/MP Local Area Development Scheme (LADS) disbursements
- **National Crime Records Bureau (NCRB) & Census**: District crime and literacy metrics

---

<div align="center">
  <sub>Taittiriya Upanishad — "Satyānna pramaditavyam" (Do not deviate from the truth)</sub>
</div>
