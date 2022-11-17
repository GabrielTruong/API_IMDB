from api_modules.imdb_request import ImdbRequest
from api_modules.imdb_request import Response
import unittest
from unittest.mock import Mock


class TestMyTestClass(unittest.TestCase):

    def test_mock_request(self):
        class_request = Response(200,{})
        #class_request.status_code = Mock(return_value=200)
        self.assertEqual(class_request.status_code,200)

