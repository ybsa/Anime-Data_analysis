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
    characters = pd.read_csv(os.path.join(input_dir, "anime_characters_cleaned.csv"))
    entities = pd.read_csv(os.path.join(input_dir, "entities_cleaned.csv"))
    return anime, characters, entities

def plot_character_roles(characters):
    """Distribution of character roles - Top 10 only"""
    role_counts = characters['role'].value_counts().head(10)
    
    plt.figure(figsize=(12, 8))
    plt.barh(range(len(role_counts)), role_counts.values, color='#4ECDC4')
    plt.yticks(range(len(role_counts)), role_counts.index)
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Role', fontsize=12)
    plt.title('Top 10 Character Roles', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()  # Highest at top
    
    # Add value labels
    for i, v in enumerate(role_counts.values):
        plt.text(v + 1000, i, f'{v:,}', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'character_roles.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated character_roles.png")

def plot_top_characters(characters, entities):
    """Top characters by appearance count"""
    char_counts = characters['character_id'].value_counts().head(15)
    
    # Merge with entities to get names
    char_df = pd.DataFrame({'character_id': char_counts.index, 'count': char_counts.values})
    char_named = char_df.merge(entities[['entity_id', 'name']], left_on='character_id', right_on='entity_id')
    
    plt.figure(figsize=(12, 8))
    sns.barplot(data=char_named, x='count', y='name', palette='viridis')
    plt.title('Top 15 Characters by Appearance Count')
    plt.xlabel('Number of Anime Appearances')
    plt.ylabel('Character')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_characters.png'))
    plt.close()
    print("Generated top_characters.png")

def plot_role_impact(anime, characters):
    """Impact of character roles on anime scores - Main roles only"""
    # Merge anime with characters
    anime_char = anime.merge(characters, on='anime_id')
    
    # Filter to main character role types only (not staff roles)
    main_roles = ['Main', 'Supporting', 'Unknown']
    anime_char_filtered = anime_char[anime_char['role'].isin(main_roles)]
    
    # Group by role and calculate mean score
    role_scores = anime_char_filtered.groupby('role')['score'].mean().sort_values(ascending=True)
    
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(role_scores)), role_scores.values, color=['#95E1D3', '#4ECDC4', '#FF6B6B'])
    plt.yticks(range(len(role_scores)), role_scores.index, fontsize=12)
    plt.xlabel('Average Score', fontsize=12)
    plt.ylabel('Character Role', fontsize=12)
    plt.title('Average Anime Score by Character Role Type', fontsize=14, fontweight='bold')
    plt.xlim(6.5, 7.5)
    
    # Add value labels
    for i, v in enumerate(role_scores.values):
        plt.text(v + 0.02, i, f'{v:.2f}', va='center', fontsize=11)
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'role_impact.png'), dpi=150, bbox_inches='tight')
    plt.close()
    print("Generated role_impact.png")

def main():
    print("Loading data for character analysis...")
    anime, characters, entities = load_data()
    
    print("Generating character plots...")
    plot_character_roles(characters)
    plot_top_characters(characters, entities)
    plot_role_impact(anime, characters)
    
    print("\nCharacter Analysis Statistics:")
    print(f"Total unique characters: {characters['character_id'].nunique()}")
    print(f"Total character-anime relationships: {len(characters)}")
    print(f"\nRole distribution:\n{characters['role'].value_counts()}")
    
    print("\nCharacter analysis complete!")

if __name__ == "__main__":
    main()
