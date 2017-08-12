import webbrowser


class Movie():
    """This class provides a way to store movie-related information.

    Attributes:
        title (str): title of the movie.
        storyline (str): brief synopsis of the movie.
        poster_image_url (str): URL of the image thumbnail to be displayed with
                                each movie.
        trailer_youtube_url (str): URL of video to be played when movie
                                   thumbnail is clicked.
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Play the movie trailer in the browser."""
        webbrowser.open(self.trailer_youtube_url)
