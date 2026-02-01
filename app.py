import streamlit as st
from recommender import recommend
import pickle

# Load the movie list for the dropdown
movies = pickle.load(open('movies.pkl', 'rb'))

st.title("🎬 My Movie Recommender App")

# This creates a searchable dropdown menu
selected_movie = st.selectbox(
    "Type or select a movie from the list",
    movies['title'].values
)

if st.button('Recommend'):
    results = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for i in results:
        st.write(f"👉 {i}")
