from api_modules.imdb_render import RenderedMovieInfo
from api_modules.imdb_render import MovieInfo


class TestRenderedMovies:

    def test_rendered_info(self):
        rendered_movies = RenderedMovieInfo.get_rendered_movie_info("Inception")
        assert isinstance(rendered_movies[0],MovieInfo)

    def test_movie_rating(self):
        rendered_movies = RenderedMovieInfo.get_rendered_movie_info("Inception")
        assert isinstance(rendered_movies[0].rating,float)


