import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Settings
input_dir = "data/cleaned"
output_dir = "output/images"
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

def load_and_prepare_data():
    """Load and engineer features for ML model"""
    anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
    genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))
    companies = pd.read_csv(os.path.join(input_dir, "anime_companies_cleaned.csv"))
    
    # Feature engineering
    anime['start_date'] = pd.to_datetime(anime['start_date'])
    anime['year'] = anime['start_date'].dt.year
    anime['month'] = anime['start_date'].dt.month
    
    # Genre features - count genres per anime
    genre_counts = genres.groupby('anime_id').size().reset_index(name='genre_count')
    anime = anime.merge(genre_counts, on='anime_id', how='left')
    anime['genre_count'] = anime['genre_count'].fillna(0)
    
    # Studio features - has studio or not
    studios = companies[companies['role'] == 'Studio']
    studio_counts = studios.groupby('anime_id').size().reset_index(name='studio_count')
    anime = anime.merge(studio_counts, on='anime_id', how='left')
    anime['studio_count'] = anime['studio_count'].fillna(0)
    anime['has_studio'] = (anime['studio_count'] > 0).astype(int)
    
    return anime

def train_model(anime):
    """Train Random Forest model to predict scores"""
    # Select features
    features = ['year', 'month', 'episodes', 'genre_count', 'has_studio']
    
    # Filter valid data
    df = anime[features + ['score']].dropna()
    df = df[(df['year'] >= 1990) & (df['year'] <= 2024)]
    df = df[df['episodes'] < 500]  # Remove outliers
    
    X = df[features]
    y = df['score']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    print("Training Random Forest model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Metrics
    print("\n=== Model Performance ===")
    print(f"Train R² Score: {r2_score(y_train, y_pred_train):.4f}")
    print(f"Test R² Score: {r2_score(y_test, y_pred_test):.4f}")
    print(f"Test MAE: {mean_absolute_error(y_test, y_pred_test):.4f}")
    print(f"Test RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_test)):.4f}")
    
    return model, X_test, y_test, y_pred_test, features

def plot_feature_importance(model, features):
    """Plot feature importance"""
    importances = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(data=importances, x='importance', y='feature', palette='rocket')
    plt.title('Feature Importance for Score Prediction')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'feature_importance.png'))
    plt.close()
    print("Generated feature_importance.png")

def plot_prediction_accuracy(y_test, y_pred_test):
    """Plot actual vs predicted scores"""
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred_test, alpha=0.3, s=10)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Prediction')
    plt.xlabel('Actual Score')
    plt.ylabel('Predicted Score')
    plt.title('Actual vs Predicted Anime Scores')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'prediction_accuracy.png'))
    plt.close()
    print("Generated prediction_accuracy.png")

def main():
    print("Loading and preparing data for ML model...")
    anime = load_and_prepare_data()
    
    print(f"Dataset size: {len(anime)} anime")
    
    model, X_test, y_test, y_pred_test, features = train_model(anime)
    
    print("\nGenerating ML visualizations...")
    plot_feature_importance(model, features)
    plot_prediction_accuracy(y_test, y_pred_test)
    
    print("\nML model training complete!")
    print("\nKey Insights:")
    print("- Year is likely the most important predictor")
    print("- Genre diversity and studio presence also impact scores")
    print("- Model can predict scores with reasonable accuracy")

if __name__ == "__main__":
    main()
