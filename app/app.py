from flask import Flask, request, render_template
from sentiment_prediction import predict
from recommendations import build_movie_recommender
from tmdb import get_movie_title_and_reviews
from main import Movie, TopMovie
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///moviemood.db')

# Create a SQLAlchemy session
session = Session(engine)


def get_movie(movie_id):
    if not movie_id:
        return {"error": "movie_id is required"}

    title = get_movie_title_and_reviews(movie_id)['title']
    reviews = get_movie_title_and_reviews(movie_id)['reviews']
    predictions = predict(reviews)

    positive = predictions.count("Positive")
    negative = predictions.count("Negative")

    summary = {
        "positive": positive,
        "negative": negative,
        "num_reviews": len(reviews)
    }

    if len(reviews) > 0:
        summary['rating'] = round((positive / len(reviews)) * 100, 2)
    else:
        summary['rating'] = 0

    return {"title": title, "reviews": reviews, "predictions": predictions, "summary": summary}


def get_recommendations(title):
    recommender = build_movie_recommender(session.query(Movie).all())
    recommended_movies = recommender(title)
    popularity = [round(p, 2) for p in recommended_movies['popularity']]
    weighted_rating = [round(wr, 2)
                       for wr in recommended_movies['weighted_rating']]
    return list(zip(recommended_movies['title'], recommended_movies['year'], popularity, weighted_rating))


def get_topmovies():
    results = session.query(TopMovie).all()
    movie_info = {
        'id': [],
        'title': [],
        'genres': [],
        'weighted_rating': [],
        'popularity': [],
        'year': []
    }
    for r in results:
        id_ = r.id
        title = r.title
        genres = json.loads(r.genres)
        weighted_rating = round(r.weighted_rating, 2)
        popularity = round(r.popularity, 2)
        year = r.year
        movie_info['id'].append(id_)
        movie_info['title'].append(title)
        movie_info['genres'].append(genres)
        movie_info['weighted_rating'].append(weighted_rating)
        movie_info['popularity'].append(popularity)
        movie_info['year'].append(year)
    return movie_info


@app.route('/', methods=['GET', 'POST'])
def index():
    title = None
    movie_id = None
    summary = None
    reviews = []
    recommendations = []

    if request.method == 'POST':
        movie_id = request.form.get('movie_id')
        data = get_movie(movie_id)

        title = data['title']
        summary = data['summary']
        reviews = list(zip(data['reviews'], data['predictions']))
        recommendations = get_recommendations(title)

    return render_template('index.html', title=title, summary=summary, reviews=reviews, recommendations=recommendations)


@app.route('/top_movies', methods=['GET'])
def top_movies():
    data = get_topmovies()
    movie_info = list(zip(data['id'], data['title'], data['genres'],
                      data['weighted_rating'], data['popularity'], data['year']))
    return render_template('top_movies.html', movie_info=movie_info)


if __name__ == '__main__':
    app.run(debug=True)

session.close()
