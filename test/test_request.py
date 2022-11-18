from api_modules.imdb_request import ImdbRequest
from api_modules.imdb_request import Response
import unittest
from unittest.mock import patch,MagicMock


class TestMyTestClass(unittest.TestCase):

    @patch('api_modules.imdb_request.requests')
    def test_mock_request(self,mock_requests):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"imDb":8.1}

        mock_requests.get.return_value = mock_response 


        self.assertIsInstance(ImdbRequest.search_movie_rating("test_api"),Response)
        

