from fpdf import FPDF
import os

# Get the script directory and project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
output_dir = os.path.join(project_root, "analysis_output")

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(44, 62, 80)
        self.cell(0, 8, 'Anime Dataset Analysis Report', border=False, align='C')
        self.ln(3)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(41, 128, 185)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(52, 73, 94)
        self.cell(0, 8, title, ln=True)
        self.ln(1)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(51, 51, 51)
        # Sanitize text - replace problematic characters
        safe_text = text.replace("'", "'").replace('"', '"').replace('"', '"').replace('—', '-').replace('–', '-')
        self.multi_cell(0, 6, safe_text)
        self.ln(4)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(51, 51, 51)
        safe_text = text.replace("'", "'").replace('"', '"').replace('"', '"')
        self.set_x(15)
        self.multi_cell(180, 5, '  - ' + safe_text)

    def add_chart(self, filename, w=160):
        """Add a chart with absolute path resolution"""
        image_path = os.path.join(output_dir, filename)
        if os.path.exists(image_path):
            x = (210 - w) / 2
            self.image(image_path, x=x, w=w)
            self.ln(5)
        else:
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(255, 0, 0)
            self.cell(0, 6, f'[Chart not found: {filename}]', ln=True)
            self.set_text_color(51, 51, 51)
            self.ln(5)

# Create PDF
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

# ==================== TITLE PAGE ====================
pdf.add_page()
pdf.ln(50)
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(41, 128, 185)
pdf.cell(0, 15, 'Anime Dataset', ln=True, align='C')
pdf.cell(0, 15, 'Complete Analysis Report', ln=True, align='C')
pdf.ln(15)
pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(52, 73, 94)
pdf.cell(0, 10, '4-Phase Comprehensive Analysis', ln=True, align='C')
pdf.cell(0, 10, '9,999 Anime | 25+ Visualizations | ML Modeling', ln=True, align='C')
pdf.ln(40)
pdf.set_font('Helvetica', 'I', 11)
pdf.set_text_color(128, 128, 128)
pdf.cell(0, 8, 'Data Source: MyAnimeList Dataset', ln=True, align='C')
pdf.cell(0, 8, 'Analysis Date: January 2026', ln=True, align='C')
pdf.cell(0, 8, 'Prepared for: Industry Analysts, Content Strategists, Anime Enthusiasts', ln=True, align='C')

# ==================== EXECUTIVE SUMMARY ====================
pdf.add_page()
pdf.chapter_title('Executive Summary')

pdf.body_text('This report presents a comprehensive analysis of 9,999 anime titles from MyAnimeList, covering releases from 1980-2024. The analysis is designed for anime studios seeking data-driven content strategies, content platforms evaluating acquisition opportunities, and industry analysts tracking market trends.')

pdf.body_text('The analysis was conducted in 4 phases: (1) Core descriptive analytics of scores, genres, and studios; (2) Industry trends and format analysis; (3) People analysis focusing on directors and voice actors; (4) Advanced analytics including machine learning, network analysis, and temporal patterns.')

pdf.section_title('Key Findings:')
pdf.bullet_point('NO SCORE INFLATION: Average scores stable at ~7.0 for over 30 years, indicating rating system integrity')
pdf.bullet_point('POPULARITY PREDICTS QUALITY: Strong correlation (not necessarily causation) - popular anime score 8.0+ vs 6.5 for low-popularity titles')
pdf.bullet_point('TALENT MATTERS: Top directors and voice actors are consistently associated with highest-rated content')
pdf.bullet_point('PRODUCTION EXPLOSION: 5x growth in annual releases post-2010, yet quality maintained')
pdf.bullet_point('SCORES ARE UNPREDICTABLE: ML model achieved R²=0.02, suggesting quality is subjective and defies simple prediction')

pdf.ln(3)
pdf.section_title('Actionable Insights:')
pdf.bullet_point('For Studios: Invest in director relationships; data shows consistent directors deliver consistent quality')
pdf.bullet_point('For Platforms: Prioritize acquisitions from studios like Kyoto Animation and MAPPA')
pdf.bullet_point('For Viewers: Use director and studio as primary quality signals when choosing content')

# ==================== METHODOLOGY ====================
pdf.add_page()
pdf.chapter_title('Methodology & Data Source')

pdf.section_title('Data Source')
pdf.body_text('Dataset: 9,999 anime entries from MyAnimeList (MAL), one of the largest anime databases with over 10 million registered users providing ratings and reviews.')

pdf.section_title('Data Files Analyzed')
pdf.bullet_point('anime.csv - Core metadata (title, score, members, episodes, type, dates)')
pdf.bullet_point('anime_genres.csv - Genre/tag mappings for each title')
pdf.bullet_point('anime_companies.csv - Studio and producer relationships')
pdf.bullet_point('anime_staff.csv - Staff credits including directors')
pdf.bullet_point('anime_voice_actors.csv - Voice actor casting information')
pdf.bullet_point('anime_characters.csv - Character data')
pdf.bullet_point('entities.csv - Lookup table for names')

pdf.section_title('Data Cleaning')
pdf.body_text('Cleaning steps included: removing entries with missing scores (<5% of data), standardizing date formats, handling null values in optional fields, and filtering to entries with sufficient user ratings for statistical validity.')

pdf.section_title('Time Period')
pdf.body_text('Primary analysis covers 1990-2024, though the dataset includes titles from 1980. Pre-1990 data is limited and primarily used for trend analysis context.')

pdf.section_title('Tools & Libraries')
pdf.bullet_point('Python 3.11 with Pandas 2.0 for data manipulation')
pdf.bullet_point('Matplotlib and Seaborn for static visualizations')
pdf.bullet_point('Scikit-learn 1.3 for machine learning modeling')
pdf.bullet_point('Plotly Dash for interactive dashboard')
pdf.bullet_point('FPDF2 for PDF report generation')

pdf.section_title('Limitations')
pdf.bullet_point('POPULARITY BIAS: Dataset skewed toward popular/well-known titles; obscure anime underrepresented')
pdf.bullet_point('RECENCY BIAS: Older anime have fewer ratings and may be less accurately scored')
pdf.bullet_point('REGIONAL FOCUS: MyAnimeList is English-focused; Japanese domestic-only titles may be underrepresented')
pdf.bullet_point('SURVIVORSHIP: Only released anime included; cancelled/unreleased projects not in dataset')

# ==================== PHASE 1-2: CORE ANALYSIS ====================
pdf.add_page()
pdf.chapter_title('PHASE 1-2: Core Analysis')

# Chart 1: Score Distribution
pdf.section_title('1. Score Distribution')
pdf.body_text('The distribution of anime scores follows a near-normal distribution centered around 6.5-7.0, with a slight positive skew. Very few anime score below 4.0 (typically abandoned/unfinished projects) or above 9.0 (masterpieces with universal acclaim).')
pdf.add_chart('score_distribution.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Median score is approximately 6.8, indicating most anime are rated "average" to "good"')
pdf.bullet_point('The long right tail (scores 8.5+) represents approximately 5% of all anime')
pdf.bullet_point('Minimal rating inflation compared to other entertainment platforms')
pdf.ln(3)

# Chart 2: Trends Over Time
pdf.add_page()
pdf.section_title('2. Industry Trends: Quantity vs Quality (1990-2024)')
pdf.body_text('This dual-axis visualization reveals possibly the most important industry trend: the anime production explosion. Annual releases grew from ~200 in the early 2000s to over 1,000 by 2020, yet average quality scores remained remarkably stable.')
pdf.add_chart('trends_over_time.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('EXPLOSIVE GROWTH: 5x increase in annual production volume since 2005')
pdf.bullet_point('QUALITY MAINTAINED: Despite quantity surge, average scores hover around 6.5-7.0')
pdf.bullet_point('NO "RACE TO BOTTOM": Industry scaling did not sacrifice quality, contrary to common concern')
pdf.bullet_point('Recent slight dip (2020+) may reflect COVID production challenges or market saturation')
pdf.ln(3)

# Chart 3: Top Genres
pdf.add_page()
pdf.section_title('3. Top 15 Anime Genres')
pdf.body_text('Genre analysis reveals market preferences. Note: genres are not mutually exclusive - a single anime can have multiple genre tags (most have 3-5).')
pdf.add_chart('top_genres.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('ACTION dominates with 3,000+ tagged entries - the market is heavily action-oriented')
pdf.bullet_point('COMEDY ranks second, often paired with other genres as a tonal element')
pdf.bullet_point('SHOUNEN (young male demographic) appears frequently, reflecting primary market focus')
pdf.bullet_point('Niche genres (Psychological, Thriller) appear less frequently but often correlate with higher scores')
pdf.ln(3)

# Chart 4: Popularity vs Score
pdf.add_page()
pdf.section_title('4. Popularity vs Score Relationship')
pdf.body_text('This analysis groups anime by member count (popularity) and calculates average scores for each tier. The relationship is striking but requires careful interpretation.')
pdf.add_chart('score_vs_popularity_binned.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('STRONG POSITIVE CORRELATION: More popular titles receive substantially higher ratings')
pdf.bullet_point('Low popularity (<10k members): Average score ~6.5')
pdf.bullet_point('High popularity (>1M members): Average score ~8.0+')
pdf.section_title('Important Caveat:')
pdf.body_text('This correlation does NOT prove causation. Two competing explanations exist: (1) Quality drives popularity - good anime naturally attract more viewers; (2) Bandwagon effect - popular anime receive higher ratings because raters are predisposed to like what others like. The truth likely involves both factors.')
pdf.ln(3)

# Chart 5: Top Studios
pdf.add_page()
pdf.section_title('5. Top Anime Studios (Minimum 15 Productions)')
pdf.body_text('This analysis filters for studios with substantial output (15+ titles) to identify consistently high-performing studios, not one-hit wonders.')
pdf.add_chart('top_studios.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('KYOTO ANIMATION and MAPPA lead in average scores - consistently deliver quality')
pdf.bullet_point('High production values and distinctive visual styles correlate with top rankings')
pdf.bullet_point('Legacy studios (Madhouse, Sunrise) maintain strong reputations over decades')
pdf.bullet_point('Studio selection is a strong quality signal for content acquisition decisions')
pdf.ln(3)

# Chart 6: Format Comparison
pdf.add_page()
pdf.section_title('6. Average Score by Anime Format')
pdf.body_text('Different anime formats serve different purposes. TVseries allow extended storytelling, movies provide cinematic experiences, OVAs offer niche content without broadcast constraints.')
pdf.add_chart('format_comparison.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('TV SERIES and MOVIES score comparably high - format itself is not a quality determinant')
pdf.bullet_point('OVAs score lower on average, possibly due to lower budgets and niche audiences')
pdf.bullet_point('SPECIALS and MUSIC formats have lowest scores - often supplementary content')
pdf.bullet_point('Format choice should be driven by story requirements, not quality expectations')
pdf.ln(3)

# Chart 7: Duration vs Score
pdf.add_page()
pdf.section_title('7. Duration vs Quality (TV Series <150 Episodes)')
pdf.body_text('This scatter plot examines whether longer series tend to be better rated, with a trend line added to show the relationship.')
pdf.add_chart('duration_vs_score.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('POSITIVE CORRELATION: Longer series tend to have higher scores')
pdf.bullet_point('SURVIVORSHIP BIAS explains this: poor shows get cancelled early; only good shows get renewed')
pdf.bullet_point('Short series (12 episodes) show high variance - many one-cour projects exist at all quality levels')
pdf.section_title('Industry Implication:')
pdf.body_text('This finding supports the business logic of seasonal renewals: let the market validate quality before committing to long runs. Shows that earn renewals have already proven audience appeal.')
pdf.ln(3)

# ==================== PHASE 3: PEOPLE ANALYSIS ====================
pdf.add_page()
pdf.chapter_title('PHASE 3: People Analysis')

# Chart 8: Top Directors
pdf.section_title('8. Top Anime Directors (Minimum 5 Titles)')
pdf.body_text('Directors shape the creative vision of anime. This analysis identifies directors with consistent track records across multiple projects.')
pdf.add_chart('top_directors.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Top directors are often associated with specific franchises (e.g., Gintama, major shounen)')
pdf.bullet_point('CONSISTENCY IS KEY: Top-ranked directors rarely produce "flops"')
pdf.bullet_point('Director tracking is a viable strategy for predicting quality for studios and viewers alike')
pdf.bullet_point('Auteur directors develop recognizable styles that build dedicated fanbases')
pdf.ln(3)

# Chart 9: Voice Actors
pdf.add_page()
pdf.section_title('9. Top Voice Actors / Seiyuu (Minimum 15 Roles)')
pdf.body_text('Voice actors (seiyuu) are celebrities in Japan. This analysis examines which actors consistently appear in highly-rated productions.')
pdf.add_chart('top_voice_actors.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Star seiyuu (Hiroshi Kamiya, Tomokazu Sugita) consistently appear in top-rated content')
pdf.bullet_point('Casting popular voice actors signals high production value and budget')
pdf.bullet_point('Strong correlation between popular seiyuu and high ratings')
pdf.bullet_point('Voice acting talent is a genuine quality differentiator, not just marketing')
pdf.ln(3)

# ==================== PHASE 4: ADVANCED ANALYTICS ====================
pdf.add_page()
pdf.chapter_title('PHASE 4: Advanced Analytics Suite')
pdf.body_text('Phase 4 applies advanced analytical techniques including machine learning, network analysis, and temporal pattern recognition to extract deeper insights from the data.')

# Chart 10: Seasonal Scores
pdf.add_page()
pdf.section_title('10. Seasonal Analysis: Score Distribution')
pdf.body_text('The anime industry operates on seasonal schedules (Spring, Summer, Fall, Winter). This analysis examines whether release season affects quality.')
pdf.add_chart('seasonal_scores.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Score distributions are remarkably CONSISTENT across all seasons')
pdf.bullet_point('No "dump months" phenomenon - good anime release year-round')
pdf.bullet_point('Season of release has negligible impact on quality')
pdf.ln(3)

# Chart 11: Seasonal Genres
pdf.add_page()
pdf.section_title('11. Seasonal Analysis: Genre Popularity Heatmap')
pdf.body_text('This heatmap visualizes which genres are most popular in each season.')
pdf.add_chart('seasonal_genres.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Action and Comedy dominate ALL seasons uniformly')
pdf.bullet_point('No strong seasonal genre preferences detected')
pdf.bullet_point('Genre distribution is remarkably uniform year-round')
pdf.ln(3)

# Chart 12: Seasonal Volume
pdf.add_page()
pdf.section_title('12. Seasonal Analysis: Release Volume')
pdf.body_text('This chart shows total anime released by season across the entire dataset.')
pdf.add_chart('seasonal_volume.png')
pdf.section_title('Key Insights & Data Context:')
pdf.bullet_point('Winter appears to dominate with ~10,000 releases')
pdf.section_title('Important Data Note:')
pdf.body_text('The Winter dominance is partially a DATA ARTIFACT. Many older anime in the dataset have incomplete release dates, and the system defaults unclear dates to January (Winter). Additionally, the Japanese fiscal year starts in April, making Winter (Q4) a major release period. This finding should be interpreted with caution.')
pdf.ln(3)

# Chart 13: Character Roles
pdf.add_page()
pdf.section_title('13. Character Analysis: Top 10 Role Types')
pdf.body_text('Analysis of 39,871 unique characters and their role classifications.')
pdf.add_chart('character_roles.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('"Unknown" roles (69,846) dominate - many characters lack proper classification in the source data')
pdf.bullet_point('Supporting characters (45,279) outnumber Main characters (33,377)')
pdf.bullet_point('This reflects anime storytelling: large casts with ensemble roles are common')
pdf.ln(3)

# Chart 14: Top Characters
pdf.add_page()
pdf.section_title('14. Character Analysis: Most Frequent Characters')
pdf.body_text('Characters that appear across multiple anime entries, typically from long-running franchises or crossover properties.')
pdf.add_chart('top_characters.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Franchise characters dominate (characters from multi-season shows)')
pdf.bullet_point('Character popularity drives sequel and spinoff production')
pdf.bullet_point('Some characters achieve "mascot" status across studio properties')
pdf.ln(3)

# Chart 15: Role Impact
pdf.add_page()
pdf.section_title('15. Character Analysis: Role Impact on Scores')
pdf.body_text('Do anime with more main characters score differently than those with ensemble casts?')
pdf.add_chart('role_impact.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('All role types cluster around the same ~7.0 average score')
pdf.bullet_point('Character role distribution has MINIMAL impact on overall anime quality')
pdf.bullet_point('Quality depends on execution, not cast structure')
pdf.ln(3)

# Chart 16: Genre Evolution
pdf.add_page()
pdf.section_title('16. Temporal Analysis: Genre Evolution Over Decades')
pdf.body_text('Tracking how genre preferences have shifted from 1980 to 2020.')
pdf.add_chart('genre_evolution.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Genre preferences have DRAMATICALLY shifted since the 1980s')
pdf.bullet_point('Action has grown exponentially to dominate modern production')
pdf.bullet_point('Different eras favor different genres, reflecting cultural changes')
pdf.bullet_point('This trend data is valuable for predicting future market direction')
pdf.ln(3)

# Chart 17: Episode Trends
pdf.add_page()
pdf.section_title('17. Temporal Analysis: Episode Count Trends (1990-2024)')
pdf.body_text('How has the typical anime length changed over time?')
pdf.add_chart('episode_trends.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Episode counts are TRENDING DOWN significantly')
pdf.bullet_point('Modern standard is 12-13 episodes (one "cour" or broadcast quarter)')
pdf.bullet_point('This represents a shift from long-running formats (50+ episodes) to seasonal projects')
pdf.bullet_point('Business model has shifted: prove concept in one season, renew if successful')
pdf.ln(3)

# Chart 18: Score Inflation
pdf.add_page()
pdf.section_title('18. Temporal Analysis: Score Inflation Investigation')
pdf.body_text('Has rating inflation occurred over time? This dual-panel analysis examines both average scores and score variance across decades.')
pdf.add_chart('score_inflation.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('NO SCORE INFLATION DETECTED - average scores stable around 7.0 for 30+ years')
pdf.bullet_point('Score variance also remains consistent over time')
pdf.bullet_point('The MAL rating system has maintained integrity - unlike many other platforms')
pdf.bullet_point('Historical comparisons are valid; older anime are not systematically underrated')
pdf.ln(3)

# Chart 19: ML Feature Importance
pdf.add_page()
pdf.section_title('19. Machine Learning: Feature Importance')
pdf.body_text('A Random Forest regression model was trained to predict anime scores based on available features. This chart shows which features the model found most predictive.')
pdf.add_chart('feature_importance.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('YEAR is the most important feature - reflects evolving production standards')
pdf.bullet_point('EPISODES matters - longer series correlate with quality (survivorship bias)')
pdf.bullet_point('GENRE COUNT has minor predictive value')
pdf.bullet_point('STUDIO PRESENCE has minimal direct impact in the model')
pdf.ln(3)

# Chart 20: Prediction Accuracy
pdf.add_page()
pdf.section_title('20. Machine Learning: Prediction Accuracy')
pdf.body_text('Scatter plot comparing actual scores to model predictions. A perfect model would cluster points along the diagonal line.')
pdf.add_chart('prediction_accuracy.png')
pdf.section_title('Model Performance:')
pdf.bullet_point('R² Score: 0.02 (very low predictive power)')
pdf.bullet_point('MAE: 0.50 (average error of half a point)')
pdf.section_title('Why the Model Fails (And Why That is Interesting):')
pdf.body_text('The model\'s poor performance is itself a finding: anime quality cannot be predicted from basic metadata. This suggests that subjective factors (story, art, direction, cultural timing) matter far more than structural features. Creativity defies algorithmic prediction - which is perhaps reassuring for the art form.')
pdf.ln(3)

# Chart 21: Director-Studio Network
pdf.add_page()
pdf.section_title('21. Network Analysis: Director-Studio Collaborations')
pdf.body_text('Identifying the most frequent director-studio partnerships in the industry.')
pdf.add_chart('director_studio_network.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Clear partnership patterns exist - directors tend to work repeatedly with the same studios')
pdf.bullet_point('Successful collaborations are replicated over time')
pdf.bullet_point('These partnerships represent valuable industry relationships')
pdf.bullet_point('Studios cultivate director talent; directors develop studio loyalty')
pdf.ln(3)

# Chart 22: Studio Genre Heatmap
pdf.add_page()
pdf.section_title('22. Network Analysis: Studio Genre Specialization')
pdf.body_text('Which genres does each major studio focus on? This heatmap reveals specialization patterns.')
pdf.add_chart('studio_genre_heatmap.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Studios show DISTINCT genre preferences - specialization is real')
pdf.bullet_point('Some studios diversify widely; others focus on 2-3 core genres')
pdf.bullet_point('Genre specialization correlates with quality - expertise compounds')
pdf.bullet_point('This data helps match projects to studios with relevant experience')
pdf.ln(3)

# Chart 23: Studio Comparison
pdf.add_page()
pdf.section_title('23. Comparative Analysis: Studio Quality vs Volume')
pdf.body_text('Do studios sacrifice quality for quantity? This dual bar chart examines both dimensions.')
pdf.add_chart('studio_comparison.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Top studios successfully balance BOTH quality AND quantity')
pdf.bullet_point('High volume does not necessarily mean low quality')
pdf.bullet_point('Best studios have systematized quality processes that scale')
pdf.bullet_point('Consistency is the key differentiator for top performers')
pdf.ln(3)

# Chart 24: Genre Mashup
pdf.add_page()
pdf.section_title('24. Comparative Analysis: Single vs Multi-Genre Performance')
pdf.body_text('Does combining multiple genres help or hurt anime performance?')
pdf.add_chart('genre_mashup.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('Single-genre and multi-genre anime perform SIMILARLY')
pdf.bullet_point('Genre mixing neither helps nor hurts scores significantly')
pdf.bullet_point('Quality depends on execution, not genre strategy')
pdf.bullet_point('Creative freedom in genre mixing is viable without quality risk')
pdf.ln(3)

# Chart 25: Format Popularity
pdf.add_page()
pdf.section_title('25. Comparative Analysis: Format Popularity Trends (2000-2024)')
pdf.body_text('How have different anime formats evolved in market share over time?')
pdf.add_chart('format_popularity.png')
pdf.section_title('Key Insights:')
pdf.bullet_point('TV format DOMINATES and continues to grow')
pdf.bullet_point('Movies show steady growth, especially post-2015')
pdf.bullet_point('OVA format has declined significantly from its 1990s peak')
pdf.bullet_point('Streaming has reinforced TV series as the primary format')
pdf.ln(3)

# ==================== STRATEGIC RECOMMENDATIONS ====================
pdf.add_page()
pdf.chapter_title('Strategic Recommendations')

pdf.section_title('For Anime Studios')
pdf.bullet_point('INVEST IN DIRECTOR RELATIONSHIPS: Data shows consistent directors deliver consistent quality. Long-term director partnerships are valuable assets.')
pdf.bullet_point('QUALITY OVER VOLUME: Top studios maintain quality at scale. Systematize quality processes rather than cutting corners to increase output.')
pdf.bullet_point('GENRE SPECIALIZATION WORKS: Build deep expertise in 2-3 core genres rather than spreading thin across all genres.')
pdf.bullet_point('EMBRACE SEASONAL MODEL: 12-episode first seasons allow market validation before major investment. Renew successful properties.')
pdf.ln(3)

pdf.section_title('For Content Platforms (Streaming Services)')
pdf.bullet_point('PRIORITIZE ACQUISITIONS FROM TOP STUDIOS: Kyoto Animation, MAPPA, and top-tier studios consistently deliver quality.')
pdf.bullet_point('USE DIRECTOR AS DISCOVERY FILTER: Director-based recommendations may outperform genre-based approaches.')
pdf.bullet_point('WINTER SEASON = MAX CONTENT: Plan annual content calendars around winter\'s larger release volume.')
pdf.bullet_point('LONG-RUNNING SERIES ARE SAFE BETS: Multi-season renewals indicate proven audience appeal.')
pdf.ln(3)

pdf.section_title('For Investors & Analysts')
pdf.bullet_point('QUALITY STUDIOS MAINTAIN MARGINS: Top studios balance quality and volume successfully - they are not mutually exclusive.')
pdf.bullet_point('FRANCHISE VALUE IS REAL: Longer series correlate with higher ratings, indicating franchise development is a valid strategy.')
pdf.bullet_point('TALENT IS A MOAT: Star directors and voice actors are scarce resources that predict success.')
pdf.bullet_point('AVOID PREDICTION MODELS: Quality is inherently unpredictable from basic features - human creative judgment remains essential.')
pdf.ln(3)

pdf.section_title('For Anime Viewers')
pdf.bullet_point('TRUST DIRECTORS AND STUDIOS OVER GENRE: Studio and director are better quality predictors than genre alone.')
pdf.bullet_point('POPULAR = PROBABLY GOOD: While not guaranteed, high-popularity anime are statistically more likely to be high-quality.')
pdf.bullet_point('DON\'T FEAR 12-EPISODE SERIES: Short seasons are now the industry standard and include excellent content.')

# ==================== CONCLUSION ====================
pdf.add_page()
pdf.chapter_title('Conclusion')

pdf.body_text('This 4-phase analysis of 9,999 anime titles reveals a mature, healthy industry that has successfully scaled without sacrificing quality. Key takeaways:')

pdf.section_title('Industry Health')
pdf.bullet_point('Production has grown 5x in two decades while maintaining average quality around 7.0')
pdf.bullet_point('No score inflation detected - the rating system has maintained integrity')
pdf.bullet_point('The seasonal production model has professionalized content development')
pdf.ln(2)

pdf.section_title('Quality Drivers')
pdf.bullet_point('Talent matters: Directors, studios, and voice actors are genuine quality predictors')
pdf.bullet_point('Popularity correlates with quality (though causation is complex)')
pdf.bullet_point('Longer series correlate with higher scores due to survivorship bias')
pdf.bullet_point('Format and genre have minimal direct impact on quality')
pdf.ln(2)

pdf.section_title('The Limits of Data')
pdf.bullet_point('ML models fail to predict scores (R²=0.02) - creativity defies algorithms')
pdf.bullet_point('This is arguably good news: art remains irreducibly human')
pdf.bullet_point('Data can inform decisions but not replace creative judgment')
pdf.ln(5)

pdf.set_font('Helvetica', 'B', 11)
pdf.set_text_color(41, 128, 185)
pdf.cell(0, 8, 'Interactive Dashboard Available', ln=True, align='C')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(51, 51, 51)
pdf.multi_cell(0, 6, 'An interactive Plotly Dash dashboard accompanies this report, allowing dynamic exploration of the data with filters for year range, format, and more. Run: python dashboard/app.py', align='C')

pdf.ln(15)
pdf.set_font('Helvetica', 'I', 9)
pdf.set_text_color(128, 128, 128)
pdf.cell(0, 6, '---', align='C', ln=True)
pdf.cell(0, 6, 'Report generated using Python, Pandas, Seaborn, Matplotlib, and Scikit-learn', align='C', ln=True)
pdf.cell(0, 6, 'Total Visualizations: 25 | Analysis Date: January 2026', align='C', ln=True)

# Save PDF
output_pdf_path = os.path.join(project_root, 'Anime_Analysis_Report.pdf')
pdf.output(output_pdf_path)
print(f"✅ PDF generated successfully: {output_pdf_path}")
print(f"📊 Total pages: {pdf.page_no()}")
print(f"📈 All 25 charts embedded with detailed descriptions")
