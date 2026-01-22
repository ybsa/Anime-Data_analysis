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
    staff = pd.read_csv(os.path.join(input_dir, "anime_staff_cleaned.csv"))
    voice_actors = pd.read_csv(os.path.join(input_dir, "anime_voice_actors_cleaned.csv"))
    characters = pd.read_csv(os.path.join(input_dir, "anime_characters_cleaned.csv"))
    
    # Ensure dates are datetime
    anime['start_date'] = pd.to_datetime(anime['start_date'])
    return anime, genres, companies, entities, staff, voice_actors, characters

def plot_score_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['score'].dropna(), bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Anime Scores')
    plt.xlabel('Score')
    plt.ylabel('Count')
    plt.savefig(os.path.join(output_dir, 'score_distribution.png'))
    plt.close()
    print("Generated score_distribution.png")

def plot_top_genres(genres_df):
    # Determine frequencies
    top_genres = genres_df['genre'].value_counts().head(15)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
    plt.title('Top 15 Anime Genres/Tags')
    plt.xlabel('Count')
    plt.ylabel('Genre')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_genres.png'))
    plt.close()
    print("Generated top_genres.png")

def plot_score_vs_popularity(df):
    # Bin popularity (members) into categories to make it understandable
    bins = [0, 10000, 100000, 500000, 1000000, float('inf')]
    labels = ['<10k', '10k-100k', '100k-500k', '500k-1M', '>1M']
    
    df['popularity_group'] = pd.cut(df['members'], bins=bins, labels=labels)
    
    # Calculate average score per group
    avg_scores = df.groupby('popularity_group')['score'].mean().reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=avg_scores, x='popularity_group', y='score', palette='coolwarm')
    plt.title('Average Score by Popularity (Member Count)')
    plt.xlabel('Popularity Group (Members)')
    plt.ylabel('Average Score')
    plt.ylim(5, 9) # Focus the y-axis to show differences clearly
    plt.savefig(os.path.join(output_dir, 'score_vs_popularity_binned.png'))
    plt.close()
    print("Generated score_vs_popularity_binned.png")

def plot_top_studios(anime, companies, entities):
    # 1. Filter companies for "Studio" role
    studios_rel = companies[companies['role'] == 'Studio']
    
    # 2. Merge with Entities to get Name
    studios_named = studios_rel.merge(entities[['entity_id', 'name']], left_on='company_id', right_on='entity_id')
    
    # 3. Merge with Anime to get Score
    studios_full = studios_named.merge(anime[['anime_id', 'score']], on='anime_id')
    
    # 4. Group by Studio
    # Count movies/shows and Avg Score
    studio_stats = studios_full.groupby('name').agg(
        count=('anime_id', 'count'),
        mean_score=('score', 'mean')
    ).reset_index()
    
    # 5. Filter: Only studios with > 15 animes (to find consistent quality, not 1-hit wonders)
    top_studios = studio_stats[studio_stats['count'] > 15].sort_values('mean_score', ascending=False).head(15)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_studios, x='mean_score', y='name', palette='magma')
    plt.title('Top 15 Anime Studios (Avg Score, >15 Productions)')
    plt.xlabel('Average Score')
    plt.ylabel('Studio')
    plt.xlim(6, 9) # Zoom in
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_studios.png'))
    plt.close()
    print("Generated top_studios.png")

def plot_trends_over_time(df):
    df['year'] = df['start_date'].dt.year
    # Filter valid years (e.g., 1980+)
    df = df[(df['year'] >= 1990) & (df['year'] <= 2024)]
    
    yearly_stats = df.groupby('year').agg(
        count=('anime_id', 'count'),
        mean_score=('score', 'mean')
    ).sort_index()
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Bar plot for Volume
    color = 'tab:blue'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Number of Anime Released', color=color)
    ax1.bar(yearly_stats.index, yearly_stats['count'], color=color, alpha=0.6, label='Release Count')
    ax1.tick_params(axis='y', labelcolor=color)
    
    # Line plot for Quality
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('Average Score', color=color)  # we already handled the x-label with ax1
    ax2.plot(yearly_stats.index, yearly_stats['mean_score'], color=color, linewidth=3, marker='o', label='Avg Score')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(6, 8.5)
    
    plt.title('Anime Industry Trends: Quantity vs. Quality (1990-2024)')
    fig.tight_layout()
    plt.savefig(os.path.join(output_dir, 'trends_over_time.png'))
    plt.close()
    print("Generated trends_over_time.png")

def plot_format_comparison(df):
    # Group by Type
    type_stats = df.groupby('type')['score'].mean().sort_values(ascending=False).reset_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=type_stats, x='type', y='score', palette='Pastel1')
    plt.title('Average Score by Anime Format')
    plt.xlabel('Format')
    plt.ylabel('Average Score')
    plt.ylim(6, 8)
    plt.savefig(os.path.join(output_dir, 'format_comparison.png'))
    plt.close()
    print("Generated format_comparison.png")

def plot_duration_vs_score(df):
    # Filter for standard TV series range (e.g. < 200 eps) to see the trend clearer
    # and exclude movies (1 ep)
    tv_anime = df[(df['type'] == 'TV') & (df['episodes'] > 1) & (df['episodes'] < 150)]
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tv_anime, x='episodes', y='score', alpha=0.5, color='purple')
    
    # Add a trendline
    sns.regplot(data=tv_anime, x='episodes', y='score', scatter=False, color='black')
    
    plt.title('Do Longer Series Get Better Scores? (TV Anime < 150 Eps)')
    plt.xlabel('Number of Episodes')
    plt.ylabel('Score')
    plt.savefig(os.path.join(output_dir, 'duration_vs_score.png'))
    plt.close()
    print("Generated duration_vs_score.png")

def plot_top_directors(anime, staff, entities):
    # 1. Filter for Directors
    # Role often contains multiple roles like "Director, Storyboard", so we use string contains
    directors = staff[staff['role'].str.contains('Director', case=False, na=False)]
    
    # 2. Join with Entities to get Name
    directors_named = directors.merge(entities[['entity_id', 'name']], left_on='person_id', right_on='entity_id')
    
    # 3. Join with Anime to get Score
    directors_full = directors_named.merge(anime[['anime_id', 'score']], on='anime_id')
    
    # 4. Group by Director
    director_stats = directors_full.groupby('name').agg(
        count=('anime_id', 'count'),
        mean_score=('score', 'mean')
    ).reset_index()
    
    # 5. Filter: Min 5 animes to filter out one-hit wonders
    top_directors = director_stats[director_stats['count'] >= 5].sort_values('mean_score', ascending=False).head(15)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_directors, x='mean_score', y='name', palette='rocket')
    plt.title('Top 15 Anime Directors (Avg Score, >5 Titles)')
    plt.xlabel('Average Score')
    plt.ylabel('Director')
    plt.xlim(7, 9.5) # Zoom in to see differences
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_directors.png'))
    plt.close()
    print("Generated top_directors.png")

def plot_top_voice_actors(anime, voice_actors, characters, entities):
    # 1. Filter for Japanese (Original) cast if column exists
    if 'language' in voice_actors.columns:
        voice_actors = voice_actors[voice_actors['language'] == 'Japanese']
        
    # 2. Link VA -> Character -> Anime
    # VA (person_id) -> VA Table (character_id) -> Characters Table (anime_id) -> Anime Table (score)
    
    # Merge VA with Characters on character_id
    va_char = voice_actors.merge(characters[['character_id', 'anime_id']], on='character_id')
    
    # Merge with Anime to get Score
    va_full = va_char.merge(anime[['anime_id', 'score']], on='anime_id')
    
    # Merge with Entities to get VA Name
    va_named = va_full.merge(entities[['entity_id', 'name']], left_on='person_id', right_on='entity_id')
    
    # 3. Group by Voice Actor
    va_stats = va_named.groupby('name').agg(
        count=('anime_id', 'nunique'), # Count distinct anime
        mean_score=('score', 'mean')
    ).reset_index()
    
    # 4. Filter: Min 15 roles for consistency
    top_vas = va_stats[va_stats['count'] > 15].sort_values('mean_score', ascending=False).head(15)
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=top_vas, x='mean_score', y='name', palette='mako')
    plt.title('Top 15 Voice Actors (Avg Score of Anime, >15 Roles)')
    plt.xlabel('Average Score')
    plt.ylabel('Voice Actor')
    plt.xlim(7, 9)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_voice_actors.png'))
    plt.close()
    print("Generated top_voice_actors.png")

def main():
    print("Loading data...")
    try:
        data = load_data()
        anime, genres, companies, entities, staff, voice_actors, characters = data
    except FileNotFoundError as e:
        print(f"Error: {e}. Run the cleaning script first.")
        return

    print("Generating Phase 2 & 3 plots...")
    plot_score_distribution(anime)
    plot_top_genres(genres)
    plot_score_vs_popularity(anime)
    plot_top_studios(anime, companies, entities)
    plot_trends_over_time(anime)
    plot_format_comparison(anime)
    plot_duration_vs_score(anime)
    
    # Phase 3 Plots
    plot_top_directors(anime, staff, entities)
    plot_top_voice_actors(anime, voice_actors, characters, entities)
    
    # Save a summary text
    with open(os.path.join(output_dir, "summary_stats.txt"), "w") as f:
        f.write(f"Total Anime Analyzed: {len(anime)}\n")
        f.write(f"Average Score: {anime['score'].mean():.2f}\n")
        f.write(f"Most Popular Anime: {anime.sort_values('members', ascending=False).iloc[0]['title']}\n")
        f.write(f"Highest Rated Anime: {anime.sort_values('score', ascending=False).iloc[0]['title']}\n")
    print("Saved summary_stats.txt")
    print("All Analysis complete!")

if __name__ == "__main__":
    main()
