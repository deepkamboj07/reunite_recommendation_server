import pandas as pd
from flask import *  
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, render_template, jsonify
from music.randomSerach import send_results, generate_recoms, sendSongofGivenId


def createSimilarity():
    data = pd.read_csv('main_data.csv') # reading the dataset
    cv = CountVectorizer()
    countMatrix = cv.fit_transform(data['comb'])
    similarity = cosine_similarity(countMatrix) # creating the similarity matrix
    return (data, similarity)


def getAllMovies():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())

def Recommend(movie):
    movie = movie.lower()
    try:
        data.head()
        similarity.shape
    except:
        (data, similarity) = createSimilarity()
    if movie not in data['movie_title'].unique():
        return 'Sorry! The movie you requested is not present in our database.'
    else:
        movieIndex = data.loc[data['movie_title'] == movie].index[0]
        lst = list(enumerate(similarity[movieIndex]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:20]  # excluding first item since it is the requested movie itself and taking the top20 movies
        movieList = []
        for i in range(len(lst)):
            a = lst[i][0]
            movieList.append(data['movie_title'][a])
        return movieList


app = Flask(__name__, static_folder='movie-recommender-app/build',
            static_url_path='/')
cors = CORS(app, resources={r"*": {"origins": "https://reunite.onrender.com"}})


@app.route('/api/movies', methods=['GET'])
@cross_origin()
def movies():
    # returns all the movies in the dataset
    movies = getAllMovies()
    result = {'arr': movies}
    return jsonify(result)


@app.route('/')
@cross_origin()
def serve():
    return jsonify(status=200, message='Welcom to Recommendation',statubar='hellllllo')


#movies recomendation
@app.route('/api/similarity/<name>')
@cross_origin()
def sendMovieRecomendation(name):
    print(name)
    movie = name
    recommendations = Recommend(movie)
    
    return jsonify(result='yes working', movie=name)

@app.route('/api/randomMusic')
@cross_origin()
def sendRandomMusic():
    songlist=send_results()
    return jsonify(result=songlist)

@app.route('/api/music-recomendation-based-on-select/<id>')
@cross_origin()
def sendData(id):
    songList=generate_recoms(id)
    return jsonify(result=songList)

@app.route('/api/song-by-id/<id>')
@cross_origin()
def sendMusicData(id):
    song=sendSongofGivenId(id)
    print(song)
    return jsonify(result=song)

@app.errorhandler(404)
def not_found(e):
    return jsonify(status=404, message='NOT FOUND')