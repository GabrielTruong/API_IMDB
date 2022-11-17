import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY_ENV = os.environ.get('API_KEY')


class ImdbRequest:
    def __init__(self):
        self.API_KEY = ""
        self._base_url = "https://imdb-api.com/en/API/"

    def set_API_KEY(self,key):
        self.API_KEY = key


    def search_movie_info(self, title=""):
        search_type = "SearchMovie/"
        response = requests.get(self._base_url+search_type+self.API_KEY+"/"+title)
        return Response(status_code=response.status_code, content=response.json())

    
    def search_movie_rating(self, id=""):
        search_type = "Ratings/"
        response = requests.get(self._base_url+search_type+self.API_KEY+"/"+id)
        return Response(status_code=response.status_code, content=response.json())

    
    def search_movie_trailer(self, id=""):
        search_type = "YouTubeTrailer/"
        response = requests.get(self._base_url+search_type+self.API_KEY+"/"+id)
        return Response(status_code=response.status_code, content=response.json())


class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
    
    
