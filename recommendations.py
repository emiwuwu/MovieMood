# Import necessary libraries
import pickle
from sklearn.metrics.pairwise import linear_kernel

# Load the pre-trained TF-IDF model from a pickle file
with open('models/tfidf_vectorizer.pickle', 'rb') as handle:
    tf = pickle.load(handle)


# Define a function to build a movie recommender system
def build_movie_recommender(data):
    # Transform the data using the pre-trained TF-IDF vectorizer
    tfidf_matrix = tf.transform([movie.description for movie in data])

    # Compute the cosine similarity matrix using linear_kernel
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Define a dictionary that maps movie titles to their indices in the data
    indices = {movie.title: index for index, movie in enumerate(data)}

    # Define the recommendation function
    def improved_recommendations(title):
        # Get the index of the input movie title
        idx = indices[title]

        # Calculate the cosine similarity scores for the input movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movie indices based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Exclude the input movie and take the top 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the indices of the recommended movies
        movie_indices = [i[0] for i in sim_scores]

        # Retrieve the recommended movies from the data
        recommended_movies = [data[index] for index in movie_indices]

        # Sort the recommended movies by weighted rating in descending order
        recommended_movies = sorted(
            recommended_movies, key=lambda x: x.weighted_rating, reverse=True)

        # Create dictionaries containing recommended movie information
        recommendations = {
            "title": [movie.title for movie in recommended_movies],
            "year": [movie.year for movie in recommended_movies],
            "popularity": [movie.popularity for movie in recommended_movies],
            "weighted_rating": [movie.weighted_rating for movie in recommended_movies],
        }

        return recommendations

    # Return the recommendation function
    return improved_recommendations
