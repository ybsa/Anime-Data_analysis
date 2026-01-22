# A Comprehensive Data-Driven Analysis of the Anime Industry (1980–2024)

**Author:** Samir Rana  
**Type:** Portfolio Research Paper (IEEE-style)  
**Dataset:** MyAnimeList Anime Dataset (9,999 titles)

---

## Abstract

The global anime industry has experienced rapid expansion over the past two decades, driven by streaming platforms, international audiences, and evolving production models. This study presents a comprehensive data-driven analysis of 9,999 anime titles sourced from MyAnimeList, covering releases from 1980 to 2024. Using descriptive analytics, temporal trend analysis, people-centric evaluation, and machine learning techniques, this research examines whether large-scale growth has impacted content quality and identifies the factors most strongly associated with highly rated anime. Results show that average user scores have remained stable at approximately 7.0 for over thirty years, indicating no observable score inflation despite a nearly fivefold increase in production volume. Popularity exhibits a strong positive correlation with ratings, while directors and voice actors emerge as consistent quality signals. Machine learning models demonstrate very low predictive power (R² = 0.02), highlighting the inherently subjective and creative nature of anime quality. These findings suggest that while data can guide strategic decisions, creative success in anime remains fundamentally resistant to algorithmic prediction.

---

## Keywords

Anime Industry, Data Analysis, Machine Learning, MyAnimeList, Content Strategy, Temporal Analysis, Network Analysis

---

## I. Introduction

Anime has evolved from a niche entertainment medium into a global cultural and economic force. Over the past two decades, annual anime production has increased dramatically, raising concerns about market saturation and potential quality degradation. At the same time, large-scale user-driven platforms such as MyAnimeList have generated extensive data that enables quantitative evaluation of industry trends.

This research aims to assess the long-term health of the anime industry by examining production growth, audience ratings, genre evolution, and the influence of creative talent. The primary objectives are:

1. **Determine whether quality has declined** as production output increased
2. **Identify reliable indicators** of high-quality productions
3. **Evaluate the extent** to which anime success can be predicted using machine learning methods

The analysis is structured in four phases: core descriptive analytics, industry trend analysis, people-focused analysis, and advanced analytics including machine learning and network analysis.

---

## II. Related Work

Prior research on media analytics has explored popularity bias in user ratings, survivorship effects in episodic content, and the challenges of predicting creative success using metadata alone. Studies on film and television industries suggest that audience ratings often correlate with visibility rather than intrinsic quality, while creative leadership plays a central role in long-term success.

However, comprehensive large-scale analyses focused specifically on anime remain limited. This study contributes to the literature by combining industry-scale descriptive analysis with advanced analytics applied exclusively to anime content.

---

## III. Dataset and Methodology

### A. Data Source

The dataset consists of 9,999 anime entries obtained from MyAnimeList (MAL), one of the largest anime databases, supported by millions of user ratings and reviews. The data includes titles released between 1980 and 2024.

### B. Data Components

The analysis integrates multiple structured files:

| File | Description |
|------|-------------|
| `anime.csv` | Core metadata (title, score, members, episodes, type, dates) |
| `anime_genres.csv` | Genre/tag mappings for each title |
| `anime_companies.csv` | Studio and producer relationships |
| `anime_staff.csv` | Staff credits including directors |
| `anime_voice_actors.csv` | Voice actor casting information |
| `anime_characters.csv` | Character data (39,871 unique characters) |
| `entities.csv` | Lookup table for names |

### C. Data Cleaning and Preparation

Entries with missing or unreliable scores were removed, accounting for less than five percent of the dataset. Data cleaning steps included:

- Removing entries with missing scores (<5% of data)
- Standardizing date formats
- Handling null values in optional fields
- Filtering to entries with sufficient user engagement for statistical validity
- Removing duplicate anime IDs (1 duplicate found)

### D. Analytical Approach

The study follows a four-phase analytical framework:

1. **Phase 1-2:** Core descriptive analysis of scores, genres, studios, and formats
2. **Phase 3:** People-focused analysis of directors and voice actors
3. **Phase 4:** Advanced analytics including machine learning, network analysis, and temporal trend evaluation

**Tools & Libraries:**
- Python 3.11 with Pandas 2.0 for data manipulation
- Matplotlib and Seaborn for static visualizations
- Scikit-learn 1.3 for machine learning modeling
- Plotly Dash for interactive dashboard

---

## IV. Results and Visual Analysis

### A. Score Distribution and Rating Stability

The distribution of anime scores follows a near-normal pattern centered between 6.5 and 7.0. Extremely low and extremely high scores are rare, indicating a balanced and credible rating system.

![Figure 1: Distribution of Anime Scores](score_distribution.png)

**Figure 1.** Distribution of anime scores across 9,999 titles. The distribution is centered around 6.8-7.0 with a slight positive skew.

**Key Observations:**
- Median score is approximately 6.8, indicating most anime are rated "average" to "good"
- The long right tail (scores 8.5+) represents approximately 5% of all anime
- Minimal rating inflation compared to other entertainment platforms
- Very few anime score below 4.0 or above 9.0

Longitudinal analysis confirms that average scores have remained stable for more than three decades, providing no evidence of systemic score inflation.

![Figure 2: Score Inflation Analysis Over Decades](score_inflation.png)

**Figure 2.** Dual-panel analysis showing average scores and score variance across decades (1990-2024). No significant inflation detected.

---

### B. Production Growth Versus Quality

Annual anime production increased nearly fivefold after 2005, surpassing 1,000 releases per year by 2020. Despite this growth, average user scores remained consistent.

![Figure 3: Anime Production Volume Over Time](anime_over_years.png)

**Figure 3.** Annual anime releases from 1980-2024, showing exponential growth particularly after 2005.

![Figure 4: Industry Trends - Quantity vs Quality](trends_over_time.png)

**Figure 4.** Dual-axis visualization comparing production volume (bars) and average scores (line) over time. Quality remains stable despite 5x growth.

**Key Findings:**
- **Explosive Growth:** 5x increase in annual production volume since 2005
- **Quality Maintained:** Average scores hover around 6.5-7.0 throughout
- **No "Race to Bottom":** Industry scaling did not sacrifice quality
- Recent slight dip (2020+) may reflect COVID production challenges

---

### C. Genre and Format Trends

Action and Comedy dominate the genre landscape, while niche genres such as Psychological and Thriller appear less frequently but often achieve higher average ratings.

![Figure 5: Top 15 Anime Genres](top_genres.png)

**Figure 5.** Horizontal bar chart showing the 15 most common genres across the dataset. Action leads with 3,000+ entries.

**Genre Insights:**
- **ACTION** dominates with 3,000+ tagged entries
- **COMEDY** ranks second, often paired with other genres
- **SHOUNEN** (young male demographic) reflects primary market focus
- Niche genres (Psychological, Thriller) appear less frequently but often correlate with higher scores

![Figure 6: Average Score by Anime Format](format_comparison.png)

**Figure 6.** Comparison of average scores across different anime formats (TV, Movie, OVA, Special, etc.).

Analysis across formats shows that television series and films perform similarly in terms of ratings, while original video animations and supplementary formats tend to score lower.

---

### D. Popularity and Audience Ratings

Popularity, measured by user membership counts, exhibits a strong positive correlation with average scores. Highly popular anime consistently achieve higher ratings than low-visibility titles.

![Figure 7: Average Score by Popularity Group](score_vs_popularity_binned.png)

**Figure 7.** Anime grouped by member count showing clear positive correlation between popularity and ratings.

| Popularity Group | Average Score |
|-----------------|---------------|
| <10k members | ~6.5 |
| 10k-100k members | ~6.8 |
| 100k-1M members | ~7.5 |
| >1M members | ~8.0+ |

**Important Caveat:** This correlation does NOT prove causation. Two competing explanations exist:
1. **Quality drives popularity** - good anime naturally attract more viewers
2. **Bandwagon effect** - popular anime receive higher ratings because raters are predisposed to like what others like

The truth likely involves both factors.

---

## V. People and Talent Analysis

### A. Directors

Directors with multiple projects demonstrate high consistency in producing well-rated anime. Repeated collaboration between directors and studios is common, suggesting the presence of stable creative partnerships.

![Figure 8: Top Anime Directors (Minimum 5 Titles)](top_directors.png)

**Figure 8.** Directors with highest average scores across their filmographies (minimum 5 titles). Consistency is key.

**Key Findings:**
- Top directors are often associated with specific franchises
- **Consistency is key:** Top-ranked directors rarely produce "flops"
- Director tracking is a viable strategy for predicting quality
- Auteur directors develop recognizable styles that build dedicated fanbases

---

### B. Voice Actors

Prominent voice actors (seiyuu) frequently appear in top-rated anime, indicating that casting decisions serve as both quality indicators and signals of production investment.

![Figure 9: Top Voice Actors (Minimum 15 Roles)](top_voice_actors.png)

**Figure 9.** Voice actors with highest average scores across their roles (minimum 15 roles).

**Key Findings:**
- Star seiyuu (Hiroshi Kamiya, Tomokazu Sugita) consistently appear in top-rated content
- Casting popular voice actors signals high production value and budget
- Strong correlation between popular seiyuu and high ratings
- Voice acting talent is a genuine quality differentiator, not just marketing

---

## VI. Advanced Analytics

### A. Temporal Trends

Genre preferences have shifted significantly since the 1980s, with Action becoming increasingly dominant in modern production.

![Figure 10: Genre Evolution Over Decades](genre_evolution.png)

**Figure 10.** Stacked area chart showing how genre popularity has evolved from 1980 to 2020.

Episode counts have trended downward, with 12 to 13 episode seasons now representing the industry standard.

![Figure 11: Episode Count Trends (1990-2024)](episode_trends.png)

**Figure 11.** Average episode counts for TV anime over time, showing shift toward seasonal (12-13 episode) formats.

**Key Insights:**
- Modern standard is 12-13 episodes (one "cour" or broadcast quarter)
- Business model shift: prove concept in one season, renew if successful
- Long-running formats (50+ episodes) have largely given way to seasonal projects

---

### B. Machine Learning Evaluation

A Random Forest regression model was trained to predict anime scores using available metadata.

![Figure 12: Feature Importance for Score Prediction](feature_importance.png)

**Figure 12.** Feature importance from Random Forest model trained to predict anime scores.

**Model Performance:**

| Metric | Value |
|--------|-------|
| Train R² Score | 0.12 |
| **Test R² Score** | **0.02** |
| Test MAE | 0.50 |
| Test RMSE | 0.61 |

![Figure 13: Actual vs Predicted Scores](prediction_accuracy.png)

**Figure 13.** Scatter plot comparing actual scores to model predictions. Poor clustering around diagonal indicates low predictive power.

**Why the Model Fails (And Why That's Interesting):**

The model's poor performance is itself a significant finding: anime quality cannot be predicted from basic metadata. This suggests that subjective factors (story, art, direction, cultural timing) matter far more than structural features. **Creativity defies algorithmic prediction** - which is perhaps reassuring for the art form.

---

### C. Network and Studio Analysis

Network analysis reveals strong director-studio partnerships and clear genre specialization among major studios.

![Figure 14: Director-Studio Collaboration Network](director_studio_network.png)

**Figure 14.** Top 15 director-studio collaboration pairs showing established creative partnerships.

![Figure 15: Studio Genre Specialization Heatmap](studio_genre_heatmap.png)

**Figure 15.** Heatmap showing genre specialization patterns across major anime studios.

**Key Findings:**
- Clear partnership patterns exist - directors tend to work repeatedly with the same studios
- Studios show distinct genre preferences and specialization
- High-performing studios balance production volume with consistent quality
- Genre specialization correlates with quality - expertise compounds

---

## VII. Discussion

The findings indicate that the anime industry has matured into a scalable production ecosystem capable of maintaining quality despite rapid growth. Several key themes emerge:

**1. Industry Health**
- Production has grown 5x in two decades while maintaining average quality around 7.0
- No score inflation detected - the rating system has maintained integrity
- The seasonal production model has professionalized content development

**2. Quality Drivers**
- Talent matters: Directors, studios, and voice actors are genuine quality predictors
- Popularity correlates with quality (though causation is complex)
- Longer series correlate with higher scores due to survivorship bias
- Format and genre have minimal direct impact on quality

**3. The Limits of Data**
- ML models fail to predict scores (R²=0.02) - creativity defies algorithms
- This is arguably good news: art remains irreducibly human
- Data can inform decisions but not replace creative judgment

**Strategic Implications:**
- **For Studios:** Invest in director relationships and systematic quality processes
- **For Platforms:** Prioritize acquisitions from top studios; use director as discovery filter
- **For Viewers:** Trust directors and studios over genre alone when selecting content

---

## VIII. Conclusion and Future Work

This research demonstrates that large-scale data analysis can provide valuable insights into the structure and evolution of the anime industry. Key conclusions:

1. **Production growth has not resulted in declining quality** - average scores remain stable at ~7.0 despite 5x increase in output
2. **No evidence of rating inflation** is observed over 30+ years
3. **Popularity, directors, and voice actors** correlate strongly with success
4. **Machine learning models fail to accurately predict quality** (R²=0.02), highlighting the subjective nature of creative evaluation

### Future Work

Potential directions for future research include:

- **Narrative Analysis:** Incorporating story structure and thematic elements
- **Visual Style Metrics:** Quantifying animation quality and artistic direction
- **Audience Sentiment Modeling:** Using NLP on user reviews for deeper insights
- **International Markets:** Comparing reception across different regions
- **Economic Analysis:** Correlating production budgets with quality outcomes

---

## References

[1] MyAnimeList, "Anime Database," https://myanimelist.net

[2] T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning*. Springer, 2009.

[3] Scikit-learn Developers, "Machine Learning in Python," 2023.

[4] F. Pedregosa et al., "Scikit-learn: Machine Learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825-2830, 2011.

[5] J.D. Hunter, "Matplotlib: A 2D Graphics Environment," *Computing in Science & Engineering*, vol. 9, no. 3, pp. 90-95, 2007.

[6] W. McKinney, "Data Structures for Statistical Computing in Python," *Proc. 9th Python in Science Conf.*, pp. 51-56, 2010.

---

*Report generated using Python, Pandas, Seaborn, Matplotlib, and Scikit-learn.*  
*Analysis Date: January 2026*  
*Total Visualizations: 15*
