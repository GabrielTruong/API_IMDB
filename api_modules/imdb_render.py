from api_modules.imdb_request import ImdbRequest
from api_modules.imdb_request import Response


class MovieInfo():
    def __init__(self, title, id, description, image):
        self.title = title
        self.id = id
        self.description = description
        self.image = image
        self.rating = 0
        self.trailer = ""

    def get_movie_rating(self):
        rating_response = ImdbRequest.search_movie_rating(self.id)

        if rating_response.status_code == 200:
            self.rating = rating_response.content["imDb"]

            return self.rating
        else:
            return (f"Error {rating_response.status_code}")
    
    def get_movie_trailer(self):
        trailer_response = ImdbRequest.search_movie_trailer(self.id)

        if trailer_response.status_code == 200:
            self.trailer = trailer_response.content["videoUrl"]
            return self.trailer
        else:
            return (f"Error {trailer_response.status_code}")


class RenderedMovieInfo():
    def get_rendered_movie_info(title=""):
        movie_request = ImdbRequest().search_movie_info(title)
        movie_result = movie_request.content["results"][0]
        print(movie_result)
        if movie_request.status_code == 200:
            return MovieInfo(movie_result["title"],
                              movie_result["id"],
                              movie_result["description"],
                              movie_result["image"])
        else:
            return (f"Error {movie_result.status_code}")
