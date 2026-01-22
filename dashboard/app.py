"""
Interactive Anime Data Dashboard
Run with: python dashboard/app.py
Then open http://localhost:8050 in your browser
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

# Load data - go up one directory to find cleaned folder
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
input_dir = os.path.join(parent_dir, "cleaned")

anime = pd.read_csv(os.path.join(input_dir, "anime_cleaned.csv"))
genres = pd.read_csv(os.path.join(input_dir, "anime_genres_cleaned.csv"))

# Prepare data
anime['start_date'] = pd.to_datetime(anime['start_date'])
anime['year'] = anime['start_date'].dt.year
anime_genres = anime.merge(genres, on='anime_id')

# Initialize app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("🎌 Anime Data Explorer", style={'textAlign': 'center', 'color': '#2c3e50'}),
    
    html.Div([
        html.Div([
            html.Label("Select Year Range:"),
            dcc.RangeSlider(
                id='year-slider',
                min=1990,
                max=2024,
                value=[2010, 2024],
                marks={i: str(i) for i in range(1990, 2025, 5)},
                tooltip={"placement": "bottom", "always_visible": True}
            ),
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '20px'}),
        
        html.Div([
            html.Label("Select Format:"),
            dcc.Dropdown(
                id='format-dropdown',
                options=[{'label': 'All', 'value': 'All'}] + 
                        [{'label': t, 'value': t} for t in anime['type'].unique() if pd.notna(t)],
                value='All',
                clearable=False
            ),
        ], style={'width': '48%', 'display': 'inline-block', 'padding': '20px'}),
    ]),
    
    html.Div([
        dcc.Graph(id='score-distribution'),
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='genre-popularity'),
    ], style={'width': '48%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='yearly-trend'),
    ], style={'width': '100%'}),
    
    html.Footer([
        html.P("📊 Interactive Anime Analytics Dashboard | Data from MyAnimeList", 
               style={'textAlign': 'center', 'color': '#7f8c8d', 'marginTop': '40px'})
    ])
], style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'})

# Callbacks
@app.callback(
    [Output('score-distribution', 'figure'),
     Output('genre-popularity', 'figure'),
     Output('yearly-trend', 'figure')],
    [Input('year-slider', 'value'),
     Input('format-dropdown', 'value')]
)
def update_graphs(year_range, format_type):
    # Filter data
    filtered = anime[(anime['year'] >= year_range[0]) & (anime['year'] <= year_range[1])]
    if format_type != 'All':
        filtered = filtered[filtered['type'] == format_type]
    
    filtered_genres = anime_genres[(anime_genres['year'] >= year_range[0]) & (anime_genres['year'] <= year_range[1])]
    if format_type != 'All':
        filtered_genres = filtered_genres[filtered_genres['type'] == format_type]
    
    # Score distribution
    fig1 = px.histogram(filtered, x='score', nbins=30, 
                        title=f'Score Distribution ({year_range[0]}-{year_range[1]})',
                        labels={'score': 'Score', 'count': 'Count'},
                        color_discrete_sequence=['#3498db'])
    fig1.update_layout(showlegend=False)
    
    # Genre popularity
    genre_counts = filtered_genres['genre'].value_counts().head(10)
    fig2 = px.bar(x=genre_counts.values, y=genre_counts.index, orientation='h',
                  title='Top 10 Genres',
                  labels={'x': 'Count', 'y': 'Genre'},
                  color=genre_counts.values,
                  color_continuous_scale='Viridis')
    fig2.update_layout(showlegend=False)
    
    # Yearly trend
    yearly = filtered.groupby('year').agg({'anime_id': 'count', 'score': 'mean'}).reset_index()
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=yearly['year'], y=yearly['anime_id'], 
                              name='Count', mode='lines+markers',
                              line=dict(color='#e74c3c', width=3)))
    fig3.add_trace(go.Scatter(x=yearly['year'], y=yearly['score']*100, 
                              name='Avg Score (×100)', mode='lines+markers',
                              line=dict(color='#2ecc71', width=3)))
    fig3.update_layout(title='Yearly Trends', xaxis_title='Year', yaxis_title='Value',
                       hovermode='x unified')
    
    return fig1, fig2, fig3

if __name__ == '__main__':
    print("🚀 Starting Anime Dashboard...")
    print("📊 Open http://localhost:8050 in your browser")
    app.run(debug=True, port=8050)
