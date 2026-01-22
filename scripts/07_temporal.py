import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
input_dir = "data/cleaned"
output_dir = "output/images"
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

def load_data():
    anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
    genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))
    anime['start_date'] = pd.to_datetime(anime['start_date'])
    anime['year'] = anime['start_date'].dt.year
    anime['decade'] = (anime['year'] // 10) * 10
    return anime, genres

def plot_genre_evolution(anime, genres):
    """Decade-by-decade genre evolution"""
    anime_genres = anime.merge(genres, on='anime_id')
    anime_genres = anime_genres[(anime_genres['decade'] >= 1980) & (anime_genres['decade'] <= 2020)]
    
    # Get top 5 genres
    top_genres = genres['genre'].value_counts().head(5).index.tolist()
    anime_genres = anime_genres[anime_genres['genre'].isin(top_genres)]
    
    # Count by decade and genre
    decade_genre = anime_genres.groupby(['decade', 'genre']).size().reset_index(name='count')
    
    plt.figure(figsize=(14, 8))
    for genre in top_genres:
        data = decade_genre[decade_genre['genre'] == genre]
        plt.plot(data['decade'], data['count'], marker='o', label=genre, linewidth=2)
    
    plt.title('Genre Evolution Over Decades')
    plt.xlabel('Decade')
    plt.ylabel('Number of Anime')
    plt.legend(title='Genre')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'genre_evolution.png'))
    plt.close()
    print("Generated genre_evolution.png")

def plot_episode_trends(anime):
    """Episode count trends over time"""
    anime_filtered = anime[(anime['year'] >= 1990) & (anime['year'] <= 2024) & (anime['type'] == 'TV')]
    anime_filtered = anime_filtered[anime_filtered['episodes'] < 200]  # Filter outliers
    
    yearly_eps = anime_filtered.groupby('year')['episodes'].agg(['mean', 'median']).reset_index()
    
    plt.figure(figsize=(14, 6))
    plt.plot(yearly_eps['year'], yearly_eps['mean'], label='Mean Episodes', linewidth=2, marker='o')
    plt.plot(yearly_eps['year'], yearly_eps['median'], label='Median Episodes', linewidth=2, marker='s')
    plt.title('TV Anime Episode Count Trends (1990-2024)')
    plt.xlabel('Year')
    plt.ylabel('Number of Episodes')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'episode_trends.png'))
    plt.close()
    print("Generated episode_trends.png")

def plot_score_inflation(anime):
    """Score inflation/deflation analysis"""
    anime_filtered = anime[(anime['year'] >= 1990) & (anime['year'] <= 2024)]
    
    yearly_scores = anime_filtered.groupby('year')['score'].agg(['mean', 'std']).reset_index()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Mean score over time
    ax1.plot(yearly_scores['year'], yearly_scores['mean'], linewidth=2, color='blue', marker='o')
    ax1.set_title('Average Anime Score Over Time')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Average Score')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=yearly_scores['mean'].mean(), color='r', linestyle='--', label='Overall Mean')
    ax1.legend()
    
    # Score variance over time
    ax2.plot(yearly_scores['year'], yearly_scores['std'], linewidth=2, color='green', marker='s')
    ax2.set_title('Score Variance Over Time')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Standard Deviation')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'score_inflation.png'))
    plt.close()
    print("Generated score_inflation.png")

def main():
    print("Loading data for temporal analysis...")
    anime, genres = load_data()
    
    print("Generating temporal plots...")
    plot_genre_evolution(anime, genres)
    plot_episode_trends(anime)
    plot_score_inflation(anime)
    
    print("\nTemporal analysis complete!")

if __name__ == "__main__":
    main()
