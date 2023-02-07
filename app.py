from flask import *  
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from flask import Flask, request, render_template, jsonify
from music.randomSerach import send_results, generate_recoms, sendSongofGivenId
from movies.moviesApi import getAllMovies,Recommend

app = Flask(__name__)
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
    # if type(recommendations) == type('string'):
    #     resultArray = recommendations.split('---')
    #     apiResult = {'movies': resultArray}
    #     return jsonify(apiResult)
    # else:
    #     movieString = '---'.join(recommendations)
    #     resultArray = movieString.split('---')
    #     apiResult = {'movies': resultArray}
    return jsonify(recommendations)

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

if __name__ == '__main__':
    app.run(debug=False)
