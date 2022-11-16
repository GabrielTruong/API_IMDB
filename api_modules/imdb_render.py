from api_modules.imdb_request import ImdbRequest
from api_modules.imdb_request import Response


class MovieInfo():
    def __init__(self, title, id, description, image):
        self.title = title
        self.id = id
        self.description = description
        self.image = image
        self.rating = self.getMovieRating()

    def getMovieRating(self):
        rating_response = ImdbRequest.search_movie_rating(self.id)

        if rating_response.status_code == 200:
            return rating_response.content["imDb"]
        else:
            return (f"Error {rating_response.status_code}")


class RenderedMovieInfo():
    def get_rendered_movie_info(title=""):
        movie_response = ImdbRequest.search_movie_info(title)
        nb_movie = len(movie_response.content["results"])
        if movie_response.status_code == 200:
            return [MovieInfo(movie_response.content['results'][i]["title"],
                              movie_response.content['results'][i]["id"],
                              movie_response.content['results'][i]["description"],
                              movie_response.content['results'][i]["image"]) for i in range(nb_movie)]
        else:
            return (f"Error {movie_response.status_code}")
