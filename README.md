# Create an API based project

Link to the project host on streamlit cloud: https://movietrailer.streamlit.app/

## Objectives

The goal of this mini project is to get used to Web API by manipulate one. The API we play with is the [IMDB-API](https://imdb-api.com/). The goal is to encapsulate the API to develop our own product. I chose to create a very simple app that from the name of the movie gives you the trailer associated.

Beside manipulating Web API and creating a web app using `streamlit`, I wanted to explore Test Driven Development and quality of code. That is why I didn't spend much time developping a complex app but instead a robust one. 

## Demo


https://user-images.githubusercontent.com/98752095/202849176-e504fb65-b5e8-4767-b38e-c212842afa0d.mp4


## Get Started

Start by creating a environment for this project.
```
conda create -n ENVNAME --file requirements.txt
```
Simply launch the application using the following command:
```bash
python -m streamlit run app.py
```

The app should automatically launch in your localhost.

## Tests

As mentionned earlier, this project aims to help me discover tests and Test Driven Development. I chose to use the `unittest` python package. I used the `patch` & `MagicMock` modules to 'mock' the behavior of certain function and API call to test the robustness of my web application.
To run them all together, go to the root of the project and use the following command:
```bash
python -m unittest discover test/
``` 

Or if you want to run a single test: 

```bash
python -m unittest test/TEST_FILE_NAME
```

Thank you [Antoine](https://github.com/antoinergr)for helping me in this project and support me during those late nights coding sessions.

Credits to EPF & [Clément Roque](https://github.com/Clement-Roque) for teaching us this API course.
