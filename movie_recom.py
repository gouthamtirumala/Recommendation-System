import streamlit as st
import pandas as pd
import pickle

# Display the image at the top
st.image(r"inoopng.png")
st.image(r"movie_png.png", width=500)


def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity_of_vectors[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        # fetch poster from id
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies    

movies_dictform = pickle.load(open('movies_dictform.pkl','rb'))
movies=pd.DataFrame(movies_dictform)

similarity_of_vectors=pickle.load(open('similarity_of_vectors.pkl','rb'))

st.title("Movie Recommender Engine")
 
Select_a_moviename = st.selectbox('how would like to be contacted',
movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(Select_a_moviename)
    for i in recommendations:
        st.write(i)


