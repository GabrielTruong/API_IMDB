from api_modules.imdb_render import RenderedMovieInfo
from api_modules.imdb_render import MovieInfo
import unittest
from unittest.mock import Mock

class TestRenderedMovies(unittest.TestCase):
    def test_movie_info(self):
        rendered_movie_test = MovieInfo("Inception", "tt1234567", "201O, Leonardo Di Caprio", "test.png")

        assert isinstance(rendered_movie_test.title, str)
    

