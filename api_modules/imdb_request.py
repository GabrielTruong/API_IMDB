import requests
from dotenv import load_dotenv
import os
#import streamlit as st

load_dotenv()
#API_KEY = os.environ.get('API_KEY')
#st.secrets["api_key"]

class ImdbRequest:

    _base_url = "https://imdb-api.com/en/API/"
    def __init__(self,key):
        self.API_KEY = key

    @classmethod
    def search_movie_info(cls,self,title=""):

        search_type = "SearchMovie/"
        print(self.API_KEY)
        response = requests.get(cls._base_url+search_type+self.API_KEY+"/"+title)
        return Response(status_code=response.status_code, content=response.json())

    @classmethod
    def search_movie_rating(cls,id=""):
        search_type = "Ratings/"
        response = requests.get(cls._base_url+search_type+API_KEY+"/"+id)
        return Response(status_code=response.status_code, content=response.json())

    @classmethod
    def search_movie_trailer(cls,id=""):
        search_type = "YouTubeTrailer/"
        response = requests.get(cls._base_url+search_type+API_KEY+"/"+id)
        print(response)
        return Response(status_code=response.status_code, content=response.json())


class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content
    
    
