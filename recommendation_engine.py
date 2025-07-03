import pandas as pd

def load_movie_data(csv_path="movies.csv"):
    return pd.read_csv(csv_path)

def filter_movies_by_genre(df, genre):
    return df[df['genre'].str.contains(genre, case=False)]

def ask_user_preferences(df):
    sorted_by_rating = df.sort_values(by="rating", ascending=False)
    return sorted_by_rating.head(5)[["title", "genre", "rating", "description"]]

def get_recommendations(df, top_n=10):
    return df.sort_values(by="rating", ascending=False).head(top_n)