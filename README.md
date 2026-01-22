# 🎌 A Comprehensive Data-Driven Analysis of the Anime Industry (1980–2024)

**Author:** Samir Rana  
**Type:** Portfolio Research Paper (IEEE-style)

A comprehensive data analysis project exploring **9,999 anime** titles using Python, Pandas, Matplotlib, Seaborn, and Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📊 Project Overview

This project performs a 4-phase comprehensive analysis of anime data from MyAnimeList:

| Phase | Focus | Visualizations |
|-------|-------|----------------|
| Phase 1-2 | Core Analysis (Scores, Genres, Studios, Trends) | 7 |
| Phase 3 | People Analysis (Directors, Voice Actors) | 2 |
| Phase 4 | Advanced Analytics (ML, Networks, Seasonal) | 16 |
| **Total** | | **25+** |

## 🔑 Key Findings

- **No Score Inflation**: Average scores stable at ~7.0 for 30+ years
- **5x Production Growth**: Annual releases surpassed 1,000 by 2020, yet quality maintained
- **Popularity = Quality**: Strong correlation between member count and ratings
- **Talent Matters**: Top directors and voice actors linked to highest-rated content
- **ML Fails to Predict**: R²=0.02 - creativity defies algorithmic prediction!

## 📁 Project Structure

```
Anime-Data-Analysis/
├── data/
│   ├── raw/                    # Original CSV data files
│   │   ├── anime.csv
│   │   ├── anime_characters.csv
│   │   ├── anime_companies.csv
│   │   ├── anime_genres.csv
│   │   ├── anime_staff.csv
│   │   ├── anime_voice_actors.csv
│   │   ├── entities.csv
│   │   └── dataset-metadata.json
│   └── cleaned/                # Cleaned CSV data files
├── output/
│   ├── images/                 # Generated visualizations (26 PNGs)
│   └── reports/                # PDF and markdown reports
│       ├── IEEE_Anime_Research_Report.pdf
│       └── IEEE_Research_Report.md
├── scripts/                    # Analysis Python scripts
│   ├── 01_load_inspect.py
│   ├── 02_clean.py
│   ├── 03_analyze.py
│   ├── 04_seasonal.py
│   ├── 05_characters.py
│   ├── 06_networks.py
│   ├── 07_temporal.py
│   ├── 08_ml_model.py
│   ├── 09_comparative.py
│   └── generate_ieee_pdf.py    # IEEE-style PDF report generator
├── requirements.txt
├── LICENSE
└── README.md
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ybsa/Anime-Data_analysis.git
cd Anime-Data_analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Analysis Scripts
```bash
# Run core analysis (generates visualizations)
python scripts/03_analyze.py

# Run Phase 4 analyses
python scripts/04_seasonal.py
python scripts/05_characters.py
python scripts/06_networks.py
python scripts/07_temporal.py
python scripts/08_ml_model.py
python scripts/09_comparative.py
```

### 4. Generate IEEE-Style PDF Report
```bash
python scripts/generate_ieee_pdf.py
# Output: output/reports/IEEE_Anime_Research_Report.pdf
```

## 📈 Visualizations

### Core Analysis
- Score Distribution
- Industry Trends (1990-2024)
- Top 15 Genres
- Popularity vs Score
- Top Studios
- Format Comparison
- Duration vs Quality

### People Analysis
- Top Directors (>5 titles)
- Top Voice Actors (>15 roles)

### Advanced Analytics
- Seasonal patterns (scores, genres, volume)
- Character role distribution
- Genre evolution over decades
- Episode count trends
- Score inflation analysis
- Director-Studio collaboration networks
- Studio genre specialization heatmap
- ML feature importance
- Prediction accuracy scatter plot
- Studio quality vs volume comparison
- Format popularity trends

## 🛠️ Technologies Used

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: scikit-learn (Random Forest)
- **PDF Generation**: FPDF2

## 📄 Data Source

Dataset sourced from [MyAnimeList](https://myanimelist.net) containing:
- 9,999 anime titles
- 39,871 unique characters
- Staff, studio, and voice actor relationships

## 📝 Reports

- **IEEE-Style PDF Report**: `output/reports/IEEE_Anime_Research_Report.pdf` (16 pages)
- **Markdown Report**: `output/reports/IEEE_Research_Report.md`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Made with ❤️ for anime fans and data enthusiasts*
