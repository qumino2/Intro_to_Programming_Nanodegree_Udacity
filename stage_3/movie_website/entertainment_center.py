import media
import fresh_tomatoes

the_shawshank_redemption = media.Movie(
	"The Shawshank Redemption",
	"http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg", # noqa
	"https://www.youtube.com/watch?v=6hB3S9bIaco")

up = media.Movie(
	"Up",
	"http://vignette1.wikia.nocookie.net/pixar/images/e/e1/Up_ver3_xlg.jpg/revision/latest?cb=20110414093844", # noqa
	"https://www.youtube.com/watch?v=pkqzFUhGPJg")

the_pursuit_of_happiness = media.Movie(
	"The Pursuit of Happiness",
	"https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
	"https://www.youtube.com/watch?v=89Kq8SDyvfg")

bridge_to_terabithia = media.Movie(
	"Bridge To Terabithia",
	"http://img.lum.dolimg.com/v1/images/open-uri20150422-12561-1kj1nqt_76e5c5bb.jpeg?region=0%2C0%2C500%2C747", # noqa
	"https://www.youtube.com/watch?v=T2TDSEG57hI")

movies = [the_shawshank_redemption, up, the_pursuit_of_happiness,
bridge_to_terabithia]

# function open_movies_page takes a list of movie names as input,
# and open an html file with contents in the browser
# input: a list of movie names
# output: an html file with movie contents
fresh_tomatoes.open_movies_page(movies)