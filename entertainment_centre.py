import media
import fresh_tomatoes

"""Instantiate Movie objects with the titles, synopsis, and urls for the
   corresponding poster images and YouTube trailers."""
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

finding_nemo = media.Movie(
    "Finding Nemo",
    """A clown fish named Marlin who lives in the Great Barrier Reef loses his
    son, Nemo, after he ventures into the open sea.""",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=2zLkasScy7A")

matrix = media.Movie(
    "The Matrix",
    "What is The Matrix?",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=tGgCqGm_6Hs")

avengers_age_of_ultron = media.Movie(
    "Avengers: Age of Ultron",
    """When Tony Stark jump-starts a dormant peacekeeping program, things go
    terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk and
    the rest of the Avengers to reassemble.""",
    "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
    "https://www.youtube.com/watch?v=tmeOjFno6Do")

"""List of movies used to generate the html page."""
movies = [toy_story, finding_nemo, matrix, avengers_age_of_ultron]
fresh_tomatoes.open_movies_page(movies)
