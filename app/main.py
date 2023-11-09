from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    index = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    overview = Column(Text)
    tagline = Column(Text)
    popularity = Column(Float)
    vote_average = Column(Float)
    vote_count = Column(Float)
    year = Column(String(4))
    weighted_rating = Column(Float)
    description = Column(Text)

    def __init__(self, index, id, title, genres, overview, tagline, popularity,
                 vote_average, vote_count, year, weighted_rating, description):
        self.index = index
        self.id = id
        self.title = title
        self.genres = genres
        self.overview = overview
        self.tagline = tagline
        self.popularity = popularity
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.year = year
        self.weighted_rating = weighted_rating
        self.description = description


class TopMovie(Base):
    __tablename__ = 'top_movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    genres = Column(String(100))
    weighted_rating = Column(Float)
    popularity = Column(Float)
    year = Column(String(4))

    def __init__(self, id, title, genres, weighted_rating, popularity, year):

        self.id = id
        self.title = title
        self.genres = genres
        self.weighted_rating = weighted_rating
        self.popularity = popularity
        self.year = year


engine = create_engine('sqlite:///moviemood.db')
Base.metadata.create_all(engine)
