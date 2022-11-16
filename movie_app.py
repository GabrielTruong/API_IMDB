import streamlit as st 
from PIL import Image
import urllib.request
from api_modules.imdb_render import RenderedMovieInfo



st.header("Welcome to Friday Movie !")

title = st.text_input('Are you searching for a movie ?', 'Inception')
movie_list = RenderedMovieInfo.get_rendered_movie_info(title)
movie_test = movie_list[0]
st.write('The closest movie title is', movie_test.title)
st.write('The cover is below: ')

urllib.request.urlretrieve(
  movie_test.image,
   "movie_cover.png")

img = Image.open("movie_cover.png")
st.image(img, caption='Cover of the movie')


