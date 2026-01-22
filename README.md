# 🎌 Anime Data Analysis

A comprehensive data analysis project exploring **9,999 anime** titles across multiple dimensions using Python, Pandas, Matplotlib, Seaborn, and Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📊 Project Overview

This project performs a 4-phase comprehensive analysis of anime data:

| Phase | Focus | Visualizations |
|-------|-------|----------------|
| Phase 1-2 | Core Analysis (Scores, Genres, Studios, Trends) | 7 |
| Phase 3 | People Analysis (Directors, Voice Actors) | 2 |
| Phase 4 | Advanced Analytics (ML, Networks, Seasonal) | 16 |
| **Total** | | **25+** |

## 🔑 Key Findings

- **No Score Inflation**: Average scores stable at ~7.0 for decades
- **Popularity = Quality**: Strong correlation between member count and ratings
- **Winter Dominates**: Most anime release in Winter season
- **Talent Matters**: Top directors and voice actors linked to highest-rated content
- **Scores Unpredictable**: ML model achieved R²=0.02 - creativity defies algorithms!

## 📁 Project Structure

```
Anime-Data-Analysis/
├── scripts/                    # Analysis Python scripts
│   ├── 01_load_inspect.py     # Data loading & inspection
│   ├── 02_clean.py            # Data cleaning
│   ├── 03_analyze.py          # Core analysis (Phases 1-3)
│   ├── 04_seasonal.py         # Seasonal analysis
│   ├── 05_characters.py       # Character analysis
│   ├── 06_networks.py         # Collaboration networks
│   ├── 07_temporal.py         # Temporal deep dives
│   ├── 08_ml_model.py         # Predictive modeling
│   ├── 09_comparative.py      # Comparative analysis
│   └── generate_pdf.py        # PDF report generator
├── dashboard/                  # Interactive Dash app
│   └── app.py
├── analysis_output/            # Generated visualizations & reports
├── cleaned/                    # Cleaned CSV data files
├── *.csv                       # Raw data files
├── Anime_Analysis_Report.pdf   # Comprehensive 29-page report
├── requirements.txt            # Python dependencies
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
# Run all Phase 1-3 analysis
python scripts/03_analyze.py

# Run Phase 4 analyses
python scripts/04_seasonal.py
python scripts/05_characters.py
python scripts/06_networks.py
python scripts/07_temporal.py
python scripts/08_ml_model.py
python scripts/09_comparative.py

# Generate PDF report
python scripts/generate_pdf.py
```

### 4. Launch Interactive Dashboard
```bash
cd dashboard
python app.py
# Open http://localhost:8050 in browser
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
- Single vs multi-genre performance
- Format popularity trends

## 🛠️ Technologies Used

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: scikit-learn (Random Forest)
- **Dashboard**: Dash by Plotly
- **PDF Generation**: FPDF2

## 📄 Data Source

The dataset is sourced from MyAnimeList and includes:
- `anime.csv` - Main anime information
- `anime_genres.csv` - Genre/tag mappings
- `anime_companies.csv` - Studio/producer relationships
- `anime_staff.csv` - Staff (directors, etc.)
- `anime_voice_actors.csv` - Voice actor roles
- `anime_characters.csv` - Character information
- `entities.csv` - Entity names lookup

## 📝 Reports

- **PDF Report**: `Anime_Analysis_Report.pdf` (29 pages, all charts + descriptions)
- **Markdown Summary**: `analysis_output/Anime_Analysis_Report.md`
- **Phase 4 Summary**: `analysis_output/Phase4_Summary.md`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Made with ❤️ for anime fans and data enthusiasts*
