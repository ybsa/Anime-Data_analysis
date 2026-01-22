import pandas as pd
import os
import numpy as np

# Define file paths
data_dir = "."
output_dir = "cleaned"
os.makedirs(output_dir, exist_ok=True)

files = [
    "anime.csv",
    "anime_characters.csv",
    "anime_companies.csv",
    "anime_genres.csv",
    "anime_staff.csv",
    "anime_voice_actors.csv",
    "entities.csv"
]

def load_data():
    dfs = {}
    for file in files:
        file_path = os.path.join(data_dir, file)
        if os.path.exists(file_path):
            dfs[file.split(".")[0]] = pd.read_csv(file_path)
    return dfs

def clean_anime_df(df):
    print("Cleaning anime.csv...")
    initial_shape = df.shape
    
    # 1. Date Conversions
    # Coerce errors to NaT (Not a Time) for invalid dates
    df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
    df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')
    
    # 2. Score
    # Check if 'score' is numeric, force it
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    
    # 3. Episodes
    # 'episodes' might have "Unknown" or similar
    df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
    
    # 4. Handle Missing Values
    # For now, we will NOT drop rows with missing scores, but we can fill them or leave them as NaN
    # Let's clean up synopses (fill NaN with empty string)
    df['synopsis'] = df['synopsis'].fillna("")
    
    # Drop duplicates if any
    df = df.drop_duplicates(subset=['anime_id'])
    
    final_shape = df.shape
    print(f"  Shape changed from {initial_shape} to {final_shape}")
    print(f"  Converted dates and numeric columns.")
    return df

def clean_entities(df):
    print("Cleaning entities.csv...")
    # Drop entities with no name, as they are useless
    initial_shape = df.shape
    df = df.dropna(subset=['name'])
    final_shape = df.shape
    print(f"  Dropped {initial_shape[0] - final_shape[0]} entities with missing names.")
    return df

def main():
    dfs = load_data()
    
    if 'anime' in dfs:
        dfs['anime'] = clean_anime_df(dfs['anime'])
        
    if 'entities' in dfs:
        dfs['entities'] = clean_entities(dfs['entities'])
        
    # Save cleaned files
    print("\nSaving cleaned files to /cleaned/ ...")
    for name, df in dfs.items():
        output_path = os.path.join(output_dir, f"{name}_cleaned.csv")
        df.to_csv(output_path, index=False)
        print(f"  Saved {output_path}")

if __name__ == "__main__":
    main()
