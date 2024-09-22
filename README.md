# IMDb Movie Recommender System

This is a simple **IMDb Movie Recommender System** built using Python, Streamlit, and scikit-learn. The system recommends movies based on the plot similarity of selected movies. It fetches additional movie information, including posters, from the TMDb API.

## Features
- Recommends similar movies based on the selected movie's plot.
- Displays movie posters fetched from the TMDb API.
- User-friendly interface built using Streamlit.

## Dataset
The recommender system uses two datasets sourced from The Movie Database (TMDb):
1. **tmdb_5000_movies.csv** - Contains metadata of movies including movie titles, plot summaries, genres, and more.
2. **tmdb_5000_credits.csv** - Contains information about the cast and crew of the movies.

These datasets are used to build the recommendation model, which calculates the similarity between movies based on their plot summaries.

## Installation

### Prerequisites
Make sure you have the following installed:
- **Python 3.x**
- The required Python libraries, which you can install using the `requirements.txt` file.

### Steps

1. **Clone the repository** or download the source code:
   ```bash
   git clone https://github.com/shahariarchowdhory/imdb-movie-recommender.git
   cd imdb-movie-recommender

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
3. **Model File Creation**
    Due to file size limitations of Github, I failed to upload the .pkl files. However, I have attached the script that creates those files. You can explore the dataset via the pre-made "movie_recom.ipynb" or you can create the ".pkl" in instant via running
    ```bash
    python run_me.py
3. **For Deployment** 
    ```bash
    streamlit run app.py
    ```

    Alternatively, you can use the provided scripts for easier access:
    For Windows: Run WINDOWS_RUN.cmd
    For Linux: Run LINUX_RUN.sh

For model and dataset exploration, you can access them in the Model_Creation folder. 
