import pandas as pd
import os

# Define file paths
data_dir = "."
files = [
    "anime.csv",
    "anime_characters.csv",
    "anime_companies.csv",
    "anime_genres.csv",
    "anime_staff.csv",
    "anime_voice_actors.csv",
    "entities.csv"
]

def inspect_data():
    for file in files:
        file_path = os.path.join(data_dir, file)
        if os.path.exists(file_path):
            print(f"--- Loading {file} ---")
            try:
                df = pd.read_csv(file_path)
                print(f"Shape: {df.shape}")
                print("\nColumns:")
                print(df.columns.tolist())
                print("\nMissing Values:")
                print(df.isnull().sum())
                print("\nHead:")
                print(df.head())
                print("-" * 30 + "\n")
            except Exception as e:
                print(f"Error loading {file}: {e}")
        else:
            print(f"File not found: {file}")

if __name__ == "__main__":
    inspect_data()
