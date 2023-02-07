import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def createSimilarity():
    data = pd.read_csv('movies/main_data.csv') # reading the dataset
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(data['comb'])
    similarity = cosine_similarity(countMatrix) # creating the similarity matrix
    return (data, similarity)


def getAllMovies():
    data = pd.read_csv('movies/main_data.csv')
    return list(data['movie_title'].str.capitalize())

def Recommend(movie):
    movie = movie.lower()
    data = pd.read_csv('movies/main_data.csv')
    try:
        data.head()
        similarity.shape
    except EOFError:
     return "no data provided to input function"
    except:
        (data, similarity) = createSimilarity()
    if movie not in data['movie_title'].unique():
        return 'Sorry! The movie you requested is not present in our database.'
    # else:
    #     movieIndex = data.loc[data['movie_title'] == movie].index[0]
    #     lst = list(enumerate(similarity[movieIndex]))
    #     lst = sorted(lst, key=lambda x: x[1], reverse=True)
    #     lst = lst[1:20]  # excluding first item since it is the requested movie itself and taking the top20 movies
    #     movieList = []
    #     for i in range(len(lst)):
    #         a = lst[i][0]
    #         movieList.append(data['movie_title'][a])
    return 'working hai bhai'

