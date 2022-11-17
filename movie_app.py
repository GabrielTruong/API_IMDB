import streamlit as st
import urllib.request
from api_modules.imdb_render import RenderedMovieInfo


st.header("Welcome to Friday Movie !")
st.write("You were about to watch a movie but you want to make sure it is good ? Convince yourself it is the right one by watching the trailer !")

title = st.text_input('Enter the title of the movie', 'Inception')
movie_list = RenderedMovieInfo.get_rendered_movie_info(title)
movie_chosen = movie_list[0]

st.write(f'The movie is rated {movie_chosen.rating}/10')
st.write('The trailer will appear below: ')
st.video(movie_chosen.trailer)





