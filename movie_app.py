import streamlit as st
from api_modules.imdb_render import RenderedMovieInfo
import os

st.header("Welcome to Friday Movie !")
st.write("You were about to watch a movie but you want to make sure it is good ? Convince yourself it is the right one by watching the trailer !")

movie_name = ""
try:
    title = st.text_input('Enter the title of the movie', movie_name)

#st.write(f'API KEY is {st.secrets["api_key"]}')
    movie_chosen = RenderedMovieInfo.get_rendered_movie_info(title)
    movie_chosen.get_movie_rating()
    movie_chosen.get_movie_trailer()
    st.write(f'The movie is rated {movie_chosen.rating}/10')
    st.write('The trailer will appear below: ')
    st.video(movie_chosen.trailer)
except IndexError:
    st.write("This movie doesn't exist")
    print("No return in results API Call")
except TypeError:
    print("Empty string")







