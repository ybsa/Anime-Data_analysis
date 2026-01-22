"""
IEEE-Style Anime Research Report PDF Generator
Generates a professional academic-style PDF report with proper formatting and figures.
"""

from fpdf import FPDF
import os

# Get the script directory and project root
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
images_dir = os.path.join(project_root, "output", "images")
reports_dir = os.path.join(project_root, "output", "reports")

class IEEEReportPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.figure_count = 0
    
    def header(self):
        if self.page_no() > 1:  # Skip header on title page
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, 'A Comprehensive Data-Driven Analysis of the Anime Industry (1980-2024)', border=False, align='C')
            self.ln(12)  # Increased gap after header
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def title_page(self):
        self.add_page()
        self.ln(40)
        
        # Main title
        self.set_font('Helvetica', 'B', 22)
        self.set_text_color(0, 51, 102)  # Dark blue
        self.multi_cell(0, 12, 'A Comprehensive Data-Driven Analysis\nof the Anime Industry (1980-2024)', align='C')
        
        self.ln(20)
        
        # Author
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(51, 51, 51)
        self.cell(0, 10, 'Samir Rana', ln=True, align='C')
        
        self.set_font('Helvetica', 'I', 11)
        self.set_text_color(102, 102, 102)
        self.cell(0, 8, 'Portfolio Research Paper (IEEE-style)', ln=True, align='C')
        
        self.ln(15)
        
        # Dataset info
        self.set_font('Helvetica', '', 11)
        self.set_text_color(51, 51, 51)
        self.cell(0, 8, 'Dataset: MyAnimeList Anime Dataset', ln=True, align='C')
        self.cell(0, 8, '9,999 Titles | 25+ Visualizations | ML Modeling', ln=True, align='C')
        
        self.ln(30)
        
        # Date and source
        self.set_font('Helvetica', 'I', 10)
        self.set_text_color(128, 128, 128)
        self.cell(0, 8, 'Data Source: MyAnimeList (https://myanimelist.net)', ln=True, align='C')
        self.cell(0, 8, 'Analysis Date: January 2026', ln=True, align='C')

    def section_heading(self, number, title):
        """IEEE-style section heading (e.g., I. INTRODUCTION)"""
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, f'{number}. {title.upper()}')
        self.ln(12)

    def subsection_heading(self, label, title):
        """IEEE-style subsection (e.g., A. Score Distribution)"""
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(51, 51, 51)
        self.cell(0, 8, f'{label}. {title}')
        self.ln(9)

    def body_text(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(51, 51, 51)
        # Sanitize text
        safe_text = text.replace("'", "'").replace('"', '"').replace('"', '"').replace('—', '-').replace('–', '-')
        self.multi_cell(0, 5.5, safe_text)
        self.ln(3)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(51, 51, 51)
        safe_text = text.replace("'", "'").replace('"', '"').replace('"', '"')
        self.set_x(15)
        self.multi_cell(180, 5, '  * ' + safe_text)

    def add_figure(self, filename, caption, w=150):
        """Add a figure with IEEE-style caption"""
        self.figure_count += 1
        image_path = os.path.join(images_dir, filename)
        
        if os.path.exists(image_path):
            x = (210 - w) / 2
            self.image(image_path, x=x, w=w)
            self.ln(3)
            # Caption
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(51, 51, 51)
            self.multi_cell(0, 5, f'Fig. {self.figure_count}. {caption}', align='C')
            self.ln(5)
        else:
            print(f"  [MISSING] {filename}")
            self.set_font('Helvetica', 'I', 9)
            self.set_text_color(255, 0, 0)
            self.cell(0, 6, f'[Figure not found: {filename}]', align='C')
            self.ln(6)

    def add_table(self, headers, rows):
        """Add a simple table"""
        self.set_font('Helvetica', 'B', 9)
        self.set_fill_color(240, 240, 240)
        col_width = 190 / len(headers)
        
        for header in headers:
            self.cell(col_width, 7, header, 1, 0, 'C', True)
        self.ln()
        
        self.set_font('Helvetica', '', 9)
        for row in rows:
            for cell in row:
                self.cell(col_width, 6, str(cell), 1, 0, 'C')
            self.ln()
        self.ln(5)


def generate_ieee_report():
    print("=" * 60)
    print("IEEE-Style Anime Research Report Generator")
    print("=" * 60)
    
    pdf = IEEEReportPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # ==================== TITLE PAGE ====================
    pdf.title_page()
    
    # ==================== ABSTRACT ====================
    pdf.add_page()
    pdf.section_heading('', 'Abstract')
    pdf.body_text(
        'The global anime industry has experienced rapid expansion over the past two decades, '
        'driven by streaming platforms, international audiences, and evolving production models. '
        'This study presents a comprehensive data-driven analysis of 9,999 anime titles sourced from MyAnimeList, '
        'covering releases from 1980 to 2024. Using descriptive analytics, temporal trend analysis, '
        'people-centric evaluation, and machine learning techniques, this research examines whether '
        'large-scale growth has impacted content quality and identifies the factors most strongly associated '
        'with highly rated anime.'
    )
    pdf.body_text(
        'Results show that average user scores have remained stable at approximately 7.0 for over thirty years, '
        'indicating no observable score inflation despite a nearly fivefold increase in production volume. '
        'Popularity exhibits a strong positive correlation with ratings, while directors and voice actors '
        'emerge as consistent quality signals. Machine learning models demonstrate very low predictive power '
        '(R-squared = 0.02), highlighting the inherently subjective and creative nature of anime quality. '
        'These findings suggest that while data can guide strategic decisions, creative success in anime '
        'remains fundamentally resistant to algorithmic prediction.'
    )
    
    pdf.ln(3)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(0, 6, 'Keywords')
    pdf.ln(6)
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 6, 'Anime Industry, Data Analysis, Machine Learning, MyAnimeList, Content Strategy')
    pdf.ln(10)
    
    # ==================== I. INTRODUCTION ====================
    pdf.section_heading('I', 'Introduction')
    pdf.body_text(
        'Anime has evolved from a niche entertainment medium into a global cultural and economic force. '
        'Over the past two decades, annual anime production has increased dramatically, raising concerns '
        'about market saturation and potential quality degradation. At the same time, large-scale user-driven '
        'platforms such as MyAnimeList have generated extensive data that enables quantitative evaluation of industry trends.'
    )
    pdf.body_text(
        'This research aims to assess the long-term health of the anime industry by examining production growth, '
        'audience ratings, genre evolution, and the influence of creative talent. The primary objectives are:'
    )
    pdf.bullet_point('Determine whether quality has declined as production output increased')
    pdf.bullet_point('Identify reliable indicators of high-quality productions')
    pdf.bullet_point('Evaluate the extent to which anime success can be predicted using machine learning methods')
    pdf.ln(3)
    
    # ==================== II. RELATED WORK ====================
    pdf.add_page()
    pdf.section_heading('II', 'Related Work')
    pdf.body_text(
        'Prior research on media analytics has explored popularity bias in user ratings, survivorship effects '
        'in episodic content, and the challenges of predicting creative success using metadata alone. '
        'Studies on film and television industries suggest that audience ratings often correlate with visibility '
        'rather than intrinsic quality, while creative leadership plays a central role in long-term success.'
    )
    pdf.body_text(
        'However, comprehensive large-scale analyses focused specifically on anime remain limited. '
        'This study contributes to the literature by combining industry-scale descriptive analysis '
        'with advanced analytics applied exclusively to anime content.'
    )
    
    # ==================== III. DATASET AND METHODOLOGY ====================
    pdf.section_heading('III', 'Dataset and Methodology')
    
    pdf.subsection_heading('A', 'Data Source')
    pdf.body_text(
        'The dataset consists of 9,999 anime entries obtained from MyAnimeList (MAL), one of the largest '
        'anime databases, supported by millions of user ratings and reviews. The data includes titles released between 1980 and 2024.'
    )
    
    pdf.subsection_heading('B', 'Data Components')
    pdf.body_text('The analysis integrates multiple structured files:')
    pdf.add_table(
        ['File', 'Description'],
        [
            ['anime.csv', 'Core metadata (title, score, members, episodes, type, dates)'],
            ['anime_genres.csv', 'Genre/tag mappings for each title'],
            ['anime_companies.csv', 'Studio and producer relationships'],
            ['anime_staff.csv', 'Staff credits including directors'],
            ['anime_voice_actors.csv', 'Voice actor casting information'],
            ['anime_characters.csv', 'Character data (39,871 unique characters)'],
        ]
    )
    
    pdf.subsection_heading('C', 'Data Cleaning')
    pdf.body_text(
        'Entries with missing or unreliable scores were removed, accounting for less than five percent of the dataset. '
        'Date formats were standardized, null values in optional fields were handled appropriately, '
        'and titles with insufficient user engagement were excluded to maintain statistical validity.'
    )
    
    pdf.subsection_heading('D', 'Analytical Approach')
    pdf.body_text('The study follows a four-phase analytical framework:')
    pdf.bullet_point('Phase 1-2: Core descriptive analysis of scores, genres, studios, and formats')
    pdf.bullet_point('Phase 3: People-focused analysis of directors and voice actors')
    pdf.bullet_point('Phase 4: Advanced analytics including ML, network analysis, and temporal patterns')
    pdf.ln(3)
    
    # ==================== IV. RESULTS AND VISUAL ANALYSIS ====================
    pdf.add_page()
    pdf.section_heading('IV', 'Results and Visual Analysis')
    
    pdf.subsection_heading('A', 'Score Distribution and Rating Stability')
    pdf.body_text(
        'The distribution of anime scores follows a near-normal pattern centered between 6.5 and 7.0. '
        'Extremely low and extremely high scores are rare, indicating a balanced and credible rating system.'
    )
    pdf.add_figure('score_distribution.png', 
                   'Distribution of anime scores across 9,999 titles. The distribution is centered around 6.8-7.0 with a slight positive skew.')
    
    pdf.body_text(
        'Longitudinal analysis confirms that average scores have remained stable for more than three decades, '
        'providing no evidence of systemic score inflation.'
    )
    pdf.add_figure('score_inflation.png',
                   'Dual-panel analysis showing average scores and score variance across decades (1990-2024). No significant inflation detected.')
    
    # Production Growth
    pdf.add_page()
    pdf.subsection_heading('B', 'Production Growth Versus Quality')
    pdf.body_text(
        'Annual anime production increased nearly fivefold after 2005, surpassing 1,000 releases per year by 2020. '
        'Despite this growth, average user scores remained consistent, demonstrating that increased output did not lead to a decline in overall quality.'
    )
    pdf.add_figure('trends_over_time.png',
                   'Dual-axis visualization comparing production volume (bars) and average scores (line) over time. Quality remains stable despite 5x growth.')
    
    pdf.bullet_point('EXPLOSIVE GROWTH: 5x increase in annual production volume since 2005')
    pdf.bullet_point('QUALITY MAINTAINED: Average scores hover around 6.5-7.0 throughout')
    pdf.bullet_point('NO RACE TO BOTTOM: Industry scaling did not sacrifice quality')
    pdf.ln(3)
    
    # Genre and Format
    pdf.add_page()
    pdf.subsection_heading('C', 'Genre and Format Trends')
    pdf.body_text(
        'Action and Comedy dominate the genre landscape, while niche genres such as Psychological and Thriller '
        'appear less frequently but often achieve higher average ratings.'
    )
    pdf.add_figure('top_genres.png',
                   'Top 15 anime genres by frequency. Action leads with 3,000+ entries.')
    
    pdf.add_figure('format_comparison.png',
                   'Comparison of average scores across different anime formats (TV, Movie, OVA, Special, etc.).')
    
    # Popularity
    pdf.add_page()
    pdf.subsection_heading('D', 'Popularity and Audience Ratings')
    pdf.body_text(
        'Popularity, measured by user membership counts, exhibits a strong positive correlation with average scores. '
        'Highly popular anime consistently achieve higher ratings than low-visibility titles.'
    )
    pdf.add_figure('score_vs_popularity_binned.png',
                   'Anime grouped by member count showing clear positive correlation between popularity and ratings.')
    
    pdf.add_table(
        ['Popularity Group', 'Average Score'],
        [
            ['<10k members', '~6.5'],
            ['10k-100k members', '~6.8'],
            ['100k-1M members', '~7.5'],
            ['>1M members', '~8.0+'],
        ]
    )
    
    # ==================== V. PEOPLE AND TALENT ANALYSIS ====================
    pdf.add_page()
    pdf.section_heading('V', 'People and Talent Analysis')
    
    pdf.subsection_heading('A', 'Directors')
    pdf.body_text(
        'Directors with multiple projects demonstrate high consistency in producing well-rated anime. '
        'Repeated collaboration between directors and studios is common, suggesting the presence of stable creative partnerships.'
    )
    pdf.add_figure('top_directors.png',
                   'Directors with highest average scores across their filmographies (minimum 5 titles). Consistency is key.')
    
    pdf.add_page()
    pdf.subsection_heading('B', 'Voice Actors')
    pdf.body_text(
        'Prominent voice actors (seiyuu) frequently appear in top-rated anime, indicating that casting decisions '
        'serve as both quality indicators and signals of production investment.'
    )
    pdf.add_figure('top_voice_actors.png',
                   'Voice actors with highest average scores across their roles (minimum 15 roles).')
    
    pdf.bullet_point('Star seiyuu consistently appear in top-rated content')
    pdf.bullet_point('Casting popular voice actors signals high production value and budget')
    pdf.bullet_point('Voice acting talent is a genuine quality differentiator')
    pdf.ln(3)
    
    # ==================== VI. ADVANCED ANALYTICS ====================
    pdf.add_page()
    pdf.section_heading('VI', 'Advanced Analytics')
    
    pdf.subsection_heading('A', 'Temporal Trends')
    pdf.body_text(
        'Genre preferences have shifted significantly since the 1980s, with Action becoming increasingly dominant in modern production.'
    )
    pdf.add_figure('genre_evolution.png',
                   'Stacked area chart showing how genre popularity has evolved from 1980 to 2020.')
    
    pdf.body_text(
        'Episode counts have trended downward, with 12 to 13 episode seasons now representing the industry standard.'
    )
    pdf.add_figure('episode_trends.png',
                   'Average episode counts for TV anime over time, showing shift toward seasonal (12-13 episode) formats.')
    
    # ML Evaluation
    pdf.add_page()
    pdf.subsection_heading('B', 'Machine Learning Evaluation')
    pdf.body_text(
        'A Random Forest regression model was trained to predict anime scores using available metadata.'
    )
    pdf.add_figure('feature_importance.png',
                   'Feature importance from Random Forest model trained to predict anime scores.')
    
    pdf.add_table(
        ['Metric', 'Value'],
        [
            ['Train R-squared Score', '0.12'],
            ['Test R-squared Score', '0.02'],
            ['Test MAE', '0.50'],
            ['Test RMSE', '0.61'],
        ]
    )
    
    pdf.add_figure('prediction_accuracy.png',
                   'Scatter plot comparing actual scores to model predictions. Poor clustering indicates low predictive power.')
    
    pdf.body_text(
        'The model\'s poor performance is itself a significant finding: anime quality cannot be predicted from basic metadata. '
        'This suggests that subjective factors (story, art, direction, cultural timing) matter far more than structural features. '
        'Creativity defies algorithmic prediction - which is perhaps reassuring for the art form.'
    )
    
    # Network Analysis
    pdf.add_page()
    pdf.subsection_heading('C', 'Network and Studio Analysis')
    pdf.body_text(
        'Network analysis reveals strong director-studio partnerships and clear genre specialization among major studios.'
    )
    pdf.add_figure('director_studio_network.png',
                   'Top 15 director-studio collaboration pairs showing established creative partnerships.')
    pdf.add_figure('studio_genre_heatmap.png',
                   'Heatmap showing genre specialization patterns across major anime studios.')
    
    # ==================== VII. DISCUSSION ====================
    pdf.add_page()
    pdf.section_heading('VII', 'Discussion')
    pdf.body_text(
        'The findings indicate that the anime industry has matured into a scalable production ecosystem '
        'capable of maintaining quality despite rapid growth. Creative leadership, rather than format or genre, '
        'plays a central role in determining success. The failure of predictive models underscores the limitations '
        'of algorithmic approaches in creative domains and reinforces the importance of human judgment.'
    )
    
    pdf.subsection_heading('', 'Strategic Implications')
    pdf.bullet_point('For Studios: Invest in director relationships; data shows consistent directors deliver consistent quality')
    pdf.bullet_point('For Platforms: Prioritize acquisitions from studios like Kyoto Animation and MAPPA')
    pdf.bullet_point('For Viewers: Use director and studio as primary quality signals when choosing content')
    pdf.ln(3)
    
    # ==================== VIII. CONCLUSION ====================
    pdf.add_page()
    pdf.section_heading('VIII', 'Conclusion and Future Work')
    pdf.body_text(
        'This research demonstrates that large-scale data analysis can provide valuable insights into the structure '
        'and evolution of the anime industry. Production growth has not resulted in declining quality, and no evidence '
        'of rating inflation is observed. While popularity, directors, and voice actors correlate strongly with success, '
        'machine learning models fail to accurately predict quality, highlighting the subjective nature of creative evaluation.'
    )
    
    pdf.subsection_heading('', 'Future Work')
    pdf.body_text('Potential directions for future research include:')
    pdf.bullet_point('Narrative Analysis: Incorporating story structure and thematic elements')
    pdf.bullet_point('Visual Style Metrics: Quantifying animation quality and artistic direction')
    pdf.bullet_point('Audience Sentiment Modeling: Using NLP on user reviews for deeper insights')
    pdf.bullet_point('International Markets: Comparing reception across different regions')
    pdf.ln(5)
    
    # ==================== REFERENCES ====================
    pdf.section_heading('', 'References')
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(51, 51, 51)
    refs = [
        '[1] MyAnimeList, "Anime Database," https://myanimelist.net',
        '[2] T. Hastie, R. Tibshirani, and J. Friedman, The Elements of Statistical Learning. Springer, 2009.',
        '[3] Scikit-learn Developers, "Machine Learning in Python," 2023.',
        '[4] F. Pedregosa et al., "Scikit-learn: Machine Learning in Python," JMLR, vol. 12, pp. 2825-2830, 2011.',
        '[5] J.D. Hunter, "Matplotlib: A 2D Graphics Environment," Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.',
        '[6] W. McKinney, "Data Structures for Statistical Computing in Python," Proc. 9th Python in Science Conf., pp. 51-56, 2010.',
    ]
    for ref in refs:
        pdf.multi_cell(0, 5, ref)
        pdf.ln(1)
    
    pdf.ln(10)
    pdf.set_font('Helvetica', 'I', 9)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 6, '---', align='C', ln=True)
    pdf.cell(0, 6, 'Report generated using Python, Pandas, Seaborn, Matplotlib, and Scikit-learn', align='C', ln=True)
    pdf.cell(0, 6, 'Total Visualizations: 15 | Analysis Date: January 2026', align='C', ln=True)
    
    # Save PDF
    output_pdf_path = os.path.join(reports_dir, 'IEEE_Anime_Research_Report.pdf')
    pdf.output(output_pdf_path)
    
    print(f"\n{'=' * 60}")
    print(f"PDF generated successfully!")
    print(f"{'=' * 60}")
    print(f"Output: {output_pdf_path}")
    print(f"Total pages: {pdf.page_no()}")
    print(f"Total figures: {pdf.figure_count}")
    print("=" * 60)


if __name__ == "__main__":
    generate_ieee_report()
