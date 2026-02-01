import pickle
import bz2
import os
import gdown 

# 1. Data Loading
file_id = '1-gmcKrv_9FYmu7P9NxnXEla1GWwGF3m1'
url = f'https://drive.google.com/uc?id=1-gmcKrv_9FYmu7P9NxnXEla1GWwGF3m1'
output = 'similarity.pbz2'

if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

movies = pickle.load(open('movies.pkl', 'rb'))

def load_similarity():
    with bz2.BZ2File(output, 'rb') as f:
        return pickle.load(f)

similarity = load_similarity()

# 2. THE MISSING FUNCTION (Add this now!)
def recommend(movie):
    # This line makes the search case-insensitive and handles errors
    try:
        # We lowercase both the user input and the database titles to find a match
        index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    except IndexError:
        return ["Movie not found. Please check your spelling!"]

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


