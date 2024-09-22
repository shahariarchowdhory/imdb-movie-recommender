import pickle
import streamlit as st
import requests

# Function to fetch the movie poster from TMDb API
def fetch_poster(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"
    base_url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US"
    response = requests.get(base_url.format(movie_id, api_key))
    
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_poster_url
    return ""

# Function to recommend movies based on the selected movie
def recommend(movie):
    # Get the index of the selected movie
    index = movies[movies['title'] == movie].index[0]
    
    # Compute similarity scores and sort in descending order
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    
    # Fetch the top 5 similar movies and their posters
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id  # Movie ID for poster fetching
        recommended_movie_names.append(movies.iloc[i[0]].title)  # Movie title
        recommended_movie_posters.append(fetch_poster(movie_id))  # Movie poster

    return recommended_movie_names, recommended_movie_posters

# Streamlit App Title
st.header('Movie Recommender System')

# Load pre-processed movie data and similarity matrix from pickle files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown menu for selecting a movie
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Button to display recommendations
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display the recommended movies and their posters in columns
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])
