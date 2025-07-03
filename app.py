import streamlit as st
from recommendation_engine import load_movie_data, filter_movies_by_genre, ask_user_preferences, get_recommendations

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎥 Movie Recommendation System")

df = load_movie_data()

genre = st.selectbox("Choose a movie genre", df['genre'].str.split(', ').explode().unique())

if genre:
    filtered_df = filter_movies_by_genre(df, genre)

    if filtered_df.empty:
        st.warning("No movies found for this genre.")
    else:
        st.subheader("Top Picks Based on Your Genre")
        top_movies = ask_user_preferences(filtered_df)
        st.dataframe(top_movies)

        st.subheader("🎯 Final Recommendations")
        recommended = get_recommendations(filtered_df)
        for idx, row in recommended.iterrows():
            st.markdown(f"**{row['title']}** ({row['year']}) - ⭐ {row['rating']}")
            st.markdown(f"*{row['description']}*")
            st.markdown("---")