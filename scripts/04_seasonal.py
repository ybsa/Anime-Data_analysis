import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
input_dir = "cleaned"
output_dir = "analysis_output"
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

def get_season(month):
    """Convert month to season"""
    if pd.isna(month):
        return 'Unknown'
    if month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    elif month in [9, 10, 11]:
        return 'Fall'
    else:  # 12, 1, 2
        return 'Winter'

def load_data():
    anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
    genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))
    
    # Ensure dates are datetime
    anime['start_date'] = pd.to_datetime(anime['start_date'])
    anime['month'] = anime['start_date'].dt.month
    anime['season'] = anime['month'].apply(get_season)
    
    return anime, genres

def plot_seasonal_scores(anime):
    # Filter out Unknown
    seasonal_data = anime[anime['season'] != 'Unknown']
    
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=seasonal_data, x='season', y='score', 
                order=season_order,
                palette='Set2')
    plt.title('Anime Score Distribution by Season')
    plt.xlabel('Season')
    plt.ylabel('Score')
    plt.ylim(0, 10)
    
    # Add mean markers
    means = seasonal_data.groupby('season')['score'].mean().reindex(season_order)
    for i, season in enumerate(season_order):
        if season in means.index and pd.notna(means[season]):
            plt.plot(i, means[season], 'r*', markersize=15, label='Mean' if i == 0 else '')
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'seasonal_scores.png'))
    plt.close()
    print("Generated seasonal_scores.png")

def plot_seasonal_genres(anime, genres):
    # Merge anime with genres
    anime_genres = anime.merge(genres, on='anime_id')
    
    # Filter out Unknown season
    seasonal_genres = anime_genres[anime_genres['season'] != 'Unknown']
    
    # Get top 10 genres overall
    top_genres = genres['genre'].value_counts().head(10).index.tolist()
    
    # Filter to top genres
    seasonal_genres = seasonal_genres[seasonal_genres['genre'].isin(top_genres)]
    
    # Count by season and genre
    season_genre_counts = seasonal_genres.groupby(['season', 'genre']).size().reset_index(name='count')
    
    # Pivot for heatmap
    pivot_data = season_genre_counts.pivot(index='genre', columns='season', values='count').fillna(0)
    
    # Reindex to ensure all seasons are present
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    pivot_data = pivot_data.reindex(columns=season_order, fill_value=0)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(pivot_data, annot=True, fmt='g', cmap='YlOrRd', cbar_kws={'label': 'Count'})
    plt.title('Top 10 Genres by Season')
    plt.xlabel('Season')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'seasonal_genres.png'))
    plt.close()
    print("Generated seasonal_genres.png")

def plot_seasonal_volume(anime):
    # Count anime per season
    seasonal_data = anime[anime['season'] != 'Unknown']
    season_counts = seasonal_data['season'].value_counts()
    
    # Reindex to ensure order
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    season_counts = season_counts.reindex(season_order, fill_value=0)
    
    plt.figure(figsize=(10, 6))
    season_counts.plot(kind='bar', color=['#90EE90', '#FFD700', '#FF8C00', '#87CEEB'])
    plt.title('Total Anime Released by Season')
    plt.xlabel('Season')
    plt.ylabel('Number of Anime')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'seasonal_volume.png'))
    plt.close()
    print("Generated seasonal_volume.png")

def main():
    print("Loading data for seasonal analysis...")
    anime, genres = load_data()
    
    print("Generating seasonal plots...")
    plot_seasonal_scores(anime)
    plot_seasonal_genres(anime, genres)
    plot_seasonal_volume(anime)
    
    # Print summary stats
    seasonal_stats = anime[anime['season'] != 'Unknown'].groupby('season')['score'].agg(['mean', 'count'])
    season_order = ['Spring', 'Summer', 'Fall', 'Winter']
    seasonal_stats = seasonal_stats.reindex(season_order)
    print("\nSeasonal Statistics:")
    print(seasonal_stats)
    
    print("\nSeasonal analysis complete!")

if __name__ == "__main__":
    main()
