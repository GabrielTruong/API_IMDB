from api_modules.imdb_request import ImdbRequest
from api_modules.imdb_request import Response


class TestMyTestClass:

    def test_request(self):
        assert isinstance(ImdbRequest.search_movie_info(
            title="inception"), Response)
        assert ImdbRequest.search_movie_info(
            title="inception").status_code == 200
