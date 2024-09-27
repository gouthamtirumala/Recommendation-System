import os
import streamlit as st
import pandas as pd
import pickle

# Check if the similarity_of_vectors.pkl file exists
if not os.path.exists('similarity_of_vectors.pkl'):
    st.error("The file 'similarity_of_vectors.pkl' was not found.")
else:
    similarity_of_vectors = pickle.load(open('similarity_of_vectors.pkl', 'rb'))

# Load the movie data
if not os.path.exists('movies_dictform.pkl'):
    st.error("The file 'movies_dictform.pkl' was not found.")
else:
    movies_dictform = pickle.load(open('movies_dictform.pkl', 'rb'))
    movies = pd.DataFrame(movies_dictform)

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity_of_vectors[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie Recommender Engine")

Select_a_moviename = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(Select_a_moviename)
    for i in recommendations:
        st.write(i)
