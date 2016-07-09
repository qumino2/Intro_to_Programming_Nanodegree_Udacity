import webbrowser


class Movie():
     """This class provides a way to store movie related information"""

    def __init__(self, movie_title, poster_image,
                 trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # open the url of a movie trailer in a browser
        webbrowser.open(self.trailer_youtube_url)
