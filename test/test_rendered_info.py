from api_modules.imdb_render import RenderedMovieInfo
from api_modules.imdb_render import MovieInfo
from api_modules.imdb_request import Response
import unittest
from unittest.mock import patch,MagicMock

class TestRenderedMovies(unittest.TestCase):
    
    @patch('api_modules.imdb_request.ImdbRequest.search_movie_rating')
    def test_movie_info(self,mock_get_info):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = {"imDb":8.1}

        mock_get_info.return_value = mock_response

        self.assertEqual(MovieInfo.get_movie_rating(self,API_KEY="test_key"),8.1)