# Import necessary libraries
import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the value of the DEBUG environment variable
debug = os.getenv("DEBUG")


# Define a function to get movie title and reviews based on a movie ID
def get_movie_title_and_reviews(movie_id):
    # Set up the TMDB API endpoint for movie details
    title_endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}'

    # Set up the TMDB API endpoint for movie reviews
    reviews_endpoint = f'https://api.themoviedb.org/3/movie/{movie_id}/reviews'

    # Define query parameters including the API key
    params = {
        'api_key': os.getenv("API_KEY")
    }

    try:
        # Make the API request for movie details
        details_response = requests.get(title_endpoint, params=params)
        details_response.raise_for_status()
        details_data = details_response.json()
        title = details_data["original_title"]

        # Make the API request for movie reviews
        reviews_response = requests.get(reviews_endpoint, params=params)
        reviews_response.raise_for_status()
        reviews_data = reviews_response.json()
        results = reviews_data.get('results', [])

        # Extract review content from the results
        reviews = [r['content'] for r in results]

        # Return a dictionary with movie title and reviews
        return {
            'title': title,
            'reviews': reviews
        }

    except requests.exceptions.RequestException as e:
        # Handle any request exceptions and return empty data
        print(f"Error: {e}")
        return {
            'title': None,
            'reviews': []
        }
