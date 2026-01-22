import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
input_dir = "cleaned"
output_dir = "analysis_output"
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

def load_data():
    anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
    genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))
    companies = pd.read_csv(os.path.join(input_dir, "anime_companies_cleaned.csv"))
    entities = pd.read_csv(os.path.join(input_dir, "entities_cleaned.csv"))
    return anime, genres, companies, entities

def plot_studio_comparison(anime, companies, entities):
    """Head-to-head studio comparison"""
    # Get top 10 studios
    studios = companies[companies['role'] == 'Studio']
    studios_named = studios.merge(entities[['entity_id', 'name']], left_on='company_id', right_on='entity_id')
    studios_full = studios_named.merge(anime[['anime_id', 'score']], on='anime_id')
    
    studio_stats = studios_full.groupby('name').agg(
        count=('anime_id', 'count'),
        mean_score=('score', 'mean')
    ).reset_index()
    
    top_studios = studio_stats[studio_stats['count'] > 20].sort_values('mean_score', ascending=False).head(10)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Score comparison
    sns.barplot(data=top_studios, x='mean_score', y='name', palette='magma', ax=ax1)
    ax1.set_title('Top 10 Studios by Average Score')
    ax1.set_xlabel('Average Score')
    ax1.set_ylabel('Studio')
    
    # Volume comparison
    sns.barplot(data=top_studios, x='count', y='name', palette='viridis', ax=ax2)
    ax2.set_title('Production Volume')
    ax2.set_xlabel('Number of Anime')
    ax2.set_ylabel('')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'studio_comparison.png'))
    plt.close()
    print("Generated studio_comparison.png")

def plot_genre_mashup(anime, genres):
    """Genre combination analysis"""
    # Get anime with multiple genres
    anime_genre_count = genres.groupby('anime_id').size().reset_index(name='genre_count')
    anime_multi = anime.merge(anime_genre_count, on='anime_id')
    anime_multi = anime_multi[anime_multi['genre_count'] > 1]
    
    # Compare single vs multi-genre
    anime['is_multi_genre'] = anime['anime_id'].isin(anime_multi['anime_id'])
    
    comparison = anime.groupby('is_multi_genre')['score'].agg(['mean', 'count']).reset_index()
    comparison['is_multi_genre'] = comparison['is_multi_genre'].map({True: 'Multi-Genre', False: 'Single Genre'})
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=comparison, x='is_multi_genre', y='mean', palette='Set2')
    plt.title('Single Genre vs Multi-Genre Anime Performance')
    plt.xlabel('Genre Type')
    plt.ylabel('Average Score')
    plt.ylim(6, 8)
    
    # Add count annotations
    for i, row in comparison.iterrows():
        plt.text(i, row['mean'] + 0.05, f"n={int(row['count'])}", ha='center')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'genre_mashup.png'))
    plt.close()
    print("Generated genre_mashup.png")

def plot_format_popularity(anime):
    """Format popularity over time"""
    anime['start_date'] = pd.to_datetime(anime['start_date'])
    anime['year'] = anime['start_date'].dt.year
    anime_filtered = anime[(anime['year'] >= 2000) & (anime['year'] <= 2024)]
    
    format_year = anime_filtered.groupby(['year', 'type']).size().reset_index(name='count')
    
    # Get top 4 formats
    top_formats = anime_filtered['type'].value_counts().head(4).index.tolist()
    format_year = format_year[format_year['type'].isin(top_formats)]
    
    plt.figure(figsize=(14, 6))
    for fmt in top_formats:
        data = format_year[format_year['type'] == fmt]
        plt.plot(data['year'], data['count'], marker='o', label=fmt, linewidth=2)
    
    plt.title('Anime Format Popularity Trends (2000-2024)')
    plt.xlabel('Year')
    plt.ylabel('Number of Releases')
    plt.legend(title='Format')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'format_popularity.png'))
    plt.close()
    print("Generated format_popularity.png")

def main():
    print("Loading data for comparative analysis...")
    anime, genres, companies, entities = load_data()
    
    print("Generating comparative plots...")
    plot_studio_comparison(anime, companies, entities)
    plot_genre_mashup(anime, genres)
    plot_format_popularity(anime)
    
    print("\nComparative analysis complete!")

if __name__ == "__main__":
    main()
