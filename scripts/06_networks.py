import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Settings
input_dir = "data/cleaned"
output_dir = "output/images"
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

def load_data():
    companies = pd.read_csv(os.path.join(input_dir, "anime_companies_cleaned.csv"))
    entities = pd.read_csv(os.path.join(input_dir, "entities_cleaned.csv"))
    staff = pd.read_csv(os.path.join(input_dir, "anime_staff_cleaned.csv"))
    anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
    genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))
    return companies, entities, staff, anime, genres

def plot_director_studio_network(companies, entities, staff, anime):
    """Analyze director-studio collaboration patterns"""
    # Get directors
    directors = staff[staff['role'].str.contains('Director', case=False, na=False)]
    directors_named = directors.merge(entities[['entity_id', 'name']], left_on='person_id', right_on='entity_id')
    directors_named = directors_named.rename(columns={'name': 'director_name'})
    
    # Get studios
    studios = companies[companies['role'] == 'Studio']
    studios_named = studios.merge(entities[['entity_id', 'name']], left_on='company_id', right_on='entity_id')
    studios_named = studios_named.rename(columns={'name': 'studio_name'})
    
    # Merge to find director-studio collaborations
    collab = directors_named.merge(studios_named, on='anime_id')
    
    # Count collaborations
    collab_counts = collab.groupby(['director_name', 'studio_name']).size().reset_index(name='collaborations')
    
    # Get top collaborations
    top_collabs = collab_counts.nlargest(15, 'collaborations')
    
    # Create visualization
    plt.figure(figsize=(12, 8))
    
    # Create a simple bar chart showing top collaborations
    top_collabs['pair'] = top_collabs['director_name'] + ' × ' + top_collabs['studio_name']
    top_collabs = top_collabs.sort_values('collaborations')
    
    plt.barh(range(len(top_collabs)), top_collabs['collaborations'], color='steelblue')
    plt.yticks(range(len(top_collabs)), top_collabs['pair'], fontsize=9)
    plt.xlabel('Number of Collaborations')
    plt.title('Top 15 Director-Studio Collaborations')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'director_studio_network.png'))
    plt.close()
    print("Generated director_studio_network.png")

def plot_studio_genre_heatmap(companies, entities, anime, genres):
    """Studio genre specialization heatmap"""
    # Get studios
    studios = companies[companies['role'] == 'Studio']
    studios_named = studios.merge(entities[['entity_id', 'name']], left_on='company_id', right_on='entity_id')
    
    # Merge with anime and genres
    studio_anime = studios_named.merge(anime[['anime_id']], on='anime_id')
    studio_genres = studio_anime.merge(genres, on='anime_id')
    
    # Get top 10 studios and top 10 genres
    top_studios = studios_named['name'].value_counts().head(10).index.tolist()
    top_genres = genres['genre'].value_counts().head(10).index.tolist()
    
    # Filter
    studio_genres_filtered = studio_genres[
        (studio_genres['name'].isin(top_studios)) & 
        (studio_genres['genre'].isin(top_genres))
    ]
    
    # Create pivot table
    heatmap_data = studio_genres_filtered.groupby(['name', 'genre']).size().reset_index(name='count')
    pivot = heatmap_data.pivot(index='name', columns='genre', values='count').fillna(0)
    
    plt.figure(figsize=(14, 8))
    sns.heatmap(pivot, annot=True, fmt='g', cmap='YlGnBu', cbar_kws={'label': 'Count'})
    plt.title('Studio Genre Specialization (Top 10 Studios × Top 10 Genres)')
    plt.xlabel('Genre')
    plt.ylabel('Studio')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'studio_genre_heatmap.png'))
    plt.close()
    print("Generated studio_genre_heatmap.png")

def main():
    print("Loading data for network analysis...")
    companies, entities, staff, anime, genres = load_data()
    
    print("Generating network visualizations...")
    plot_director_studio_network(companies, entities, staff, anime)
    plot_studio_genre_heatmap(companies, entities, anime, genres)
    
    print("\nNetwork analysis complete!")

if __name__ == "__main__":
    main()
