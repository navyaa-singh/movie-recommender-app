import streamlit as st
from recommender import recommend

st.title("🎬 My Movie Recommender App")

movie_name = st.text_input("Enter a movie name")

if st.button("Recommend"):
    results = recommend(movie_name)

    if results:
        st.subheader("Recommended Movies:")
        for movie in results:
            st.write("👉", movie)
    else:
        st.write("Please enter a movie name.")
