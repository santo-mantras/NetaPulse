---
title: Jumlebaaz
emoji: 🗳️
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---

# Jumlebaaz 🗳️

**India's Political Accountability Platform** — Track your elected representatives with real data from ECI affidavits, MyNeta, and public sources.

## Features

- 📊 Real candidate data for Maharashtra (279 MLAs)
- 📸 Profile photos from Wikipedia & MyNeta
- ✅ Campaign promises tracking with status
- ⚖️ Criminal cases & asset declarations from ECI affidavits
- 📰 Media spotlight with latest news
- 🔍 Compare candidates side-by-side
- 🌗 Dark mode support

## Tech Stack

- **Frontend**: React + TypeScript + Vite
- **Styling**: Tailwind CSS
- **Data Pipelines**: Python (BeautifulSoup, requests)
- **Deployment**: Docker + Nginx

## Local Development

```bash
npm install
npm run dev
```

## Docker

```bash
docker build -t jumlebaaz .
docker run -p 7860:7860 jumlebaaz
```

## Data Sources

- [MyNeta.info](https://myneta.info) — ECI affidavit data (ADR)
- [Wikipedia](https://en.wikipedia.org) — Profile photos & info
- [Election Commission of India](https://eci.gov.in) — Official records
