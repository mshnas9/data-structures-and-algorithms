import pytest
from movie_sort import sort_by_title, sort_by_year

movies = [
    {
        "title": "The Godfather",
        "year": 1972,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Pulp Fiction",
        "year": 1994,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "The Dark Knight",
        "year": 2008,
        "genres": ["Action", "Crime", "Drama"],
    },
    {
        "title": "Fight Club",
        "year": 1999,
        "genres": ["Drama"],
    },
    {
        "title": "Inception",
        "year": 2010,
        "genres": ["Action", "Adventure", "Sci-Fi"],
    },
    {
        "title": "The Matrix",
        "year": 1999,
        "genres": ["Action", "Sci-Fi"],
    },
    {
        "title": "Forrest Gump",
        "year": 1994,
        "genres": ["Drama", "Romance"],
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama"],
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "year": 2001,
        "genres": ["Action", "Adventure", "Drama"],
    },
    {
        "title": "Back to the Future",
        "year": 1985,
        "genres": ["Adventure", "Comedy", "Sci-Fi"],
    },
]


def test_sort_by_year():
    sorted_movies = sort_by_year(movies)
    assert sorted_movies[0]['title'] == 'The Godfather'

def test_sort_by_title():
    sorted_movies = sort_by_title(movies)
    assert sorted_movies[0]['title'] == 'Back to the Future'
