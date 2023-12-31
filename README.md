# MovieMood

> Exploring Sentiment Analysis and Movie Recommendations

---

## Table of Contents

- [About MovieMood](#about-moviemood)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Movie Recommendation System](#movie-recommendation-system)
- [Usage](#usage)
- [Datasets](#datasets)
- [Contributing](#contributing)

---

## About MovieMood

### Project Description

MovieMood is a comprehensive project that combines two essential components: Sentiment Analysis and a Movie Recommendation System. These components are thoughtfully designed to provide insights into movie reviews and offer movie suggestions to users based on movie descriptions.

### Sentiment Analysis

**Sentiment analysis**, also referred to as opinion mining, is a powerful technique for extracting emotional tone or sentiment from text. It involves interpreting and categorizing emotions (positive, negative, or neutral) within text data, allowing organizations to gauge public sentiment towards specific words or topics. In this repository, sentiment analysis is applied to assess movie reviews and classify them as either positive or negative based on their content.

#### Key Features:

- Utilization of natural language processing (NLP) techniques.
- Sentiment classification is achieved through the implementation of deep neural network algorithms, including Convolutional Neural Networks (CNNs).

#### Model Performance:

**Basic Model:**
- Utilizes average pooling operations AND concludes with a final fully-connected layer.
- Achieved an accuracy of **80.05%**. 

**Complex Model**
- Utilizes Convolutional Neural Networks (CNN).
- Employs max pooling operations and concludes with a final fully-connected layer.
- Applies L2 regularization to prevent overfitting.
- Performance enhanced through callback mechanisms.
- Attained an accuracy of **83.96%**.
- Classification report highlights balanced precision, recall, and F1-scores around 0.84 for positive and negative sentiments.

### Movie Recommendation System

The **Movie Recommendation System** is created to assist users in discovering new movies that align with their preferences. It employs content-based approaches to generate movie recommendations.

#### Key Features:

- Visual representation of movie popularity and ratings.
- Utilization of natural language processing (NLP) techniques.
- Content-based recommender system: Movies are suggested based on their descriptions.

## Usage

Here's how you can benefit from the project:

- Perform sentiment analysis on movie reviews to gain valuable insights into user sentiments.
- Evaluate the recommendation system in MovieMood using various metrics to ensure it meets your needs.

## Datasets

- [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/data): The IMDB dataset contains 50,000 movie reviews, divided into 25,000 for training and 25,000 for testing, making it a valuable resource for binary sentiment classification in the field of natural language processing or text analytics.
- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata): Containing metadata for approximately 5,000 movies from TMDb, this dataset provides details like titles, release dates, genres, popularity, and ratings. It serves as a valuable resource for both movie recommendations and analyzing the factors that impact a movie's success.

## Contributing

- Pei-Ju Wu (Emily)
