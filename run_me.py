# %% [markdown]
# ## DataFrame Creation

# %%
print("Hello")

# %%
import numpy
import pandas as pd

# %%
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# %%
credits.head(1)['cast'].values

# %%
movies.head()

# %%
# genre
# id
# keywords
# original lamguage 
# title
# overview
# popularity
# profuction_companies
# release_date
# runtime
# cast
# crew

movies = movies[['genres', 'id', 'keywords','original_language','title','overview','popularity','production_companies','release_date','runtime']]

# %%
movies.isnull().sum()

# %%
movies.dropna(inplace=True)

# %%
movies.duplicated().sum()

# %%
movies.head(1)

# %%
movies.iloc[0].genres

# %%
import ast
def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        i['name']
        L.append(i['name'])
    return L

# %%
movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)

# %%
def convert3(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter != 3:
            L.append(i['name'])
            counter+=1
        else:
            break
    return L

# %%
#movies['cast']=movies['cast'].apply(convert3)

# %%
#movies['cast'].head()

# %%
#movies['crew'][0]

# %%
def convert2(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director' :
            L.append(i['name'])
            break
    return L

# %%
#movies['crew']=movies['crew'].apply(convert2)

# %%
movies['overview'][0]

# %%
movies['overview']=movies['overview'].apply(lambda x:x.split())

# %%
movies.isnull().sum()

# %%
def convert4(obj):
    L=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter < 2:
            L.append(i['name'])
            counter +=1 
    return L

# %%
movies['production_companies'].apply(convert4)

# %%
movies['production_companies'] = movies['production_companies'].apply(convert4)

# %%
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
#movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
#movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies['production_companies']=movies['production_companies'].apply(lambda x:[i.replace(" ","") for i in x])

# %%
movies.head()

# %%
movies['tag'] = movies['overview'] + movies['genres'] + movies['production_companies']

# %%
new_df = movies[['id', 'title', 'tag']]

# %%
new_df['tag']=new_df['tag'].apply(lambda x:" ".join(x)) 

# %%
new_df['tag'][0]

# %%
new_df['tag'] =new_df['tag'].apply(lambda x:x.lower())

# %% [markdown]
# ## Text Vectorization

# %%
new_df['tag'][1]

# %%
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

# %%
vectors = cv.fit_transform(new_df['tag']).toarray()

# %%
vectors[0]

# %%
len(cv.get_feature_names_out())

# %%
cv.get_feature_names_out()[20:1000]

# %%
import nltk

# %%
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

# %%
ps.stem('loving')

# %%
def stem(text):

    y=[]
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

# %%
new_df['tag']=new_df['tag'].apply(stem)

# %%
from sklearn.metrics.pairwise import cosine_similarity

# %%
similarity = cosine_similarity(vectors)

# %%
similarity

# %%
def recommend(movie, how_many = 5):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:how_many+1]

    for i in movie_list:
       print(new_df.iloc[i[0]].title)

# %%
recommend('American Pie',10)

# %%
new_df.iloc[2248].title

# %%
import pickle

# %% [markdown]
# 

# %%
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# %%


# %%
pickle.dump(new_df, open("movies.pkl", "wb"))

# %%



