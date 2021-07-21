from tmdbv3api import TMDb
from tmdbv3api import Movie
import imdb
ia = imdb.IMDb()
top250 = ia.get_top250_movies()

tmdb = TMDb()
tmdb.api_key = '59d5ad58b6b388a288ba8ffa5f0c65ca'
tmdb.language = 'en'
tmdb.debug = True
movie = Movie()

recommendations = movie.recommendations(movie_id=111)

#for recommendation in recommendations:
 #   print(recommendation.title)





# Iterate through the first 20 movies in the top 250
for movie_count in range(0, 20):
    # First, retrieve the movie object using its ID
    movie = ia.get_movie(top250[movie_count].movieID)
    # Print movie title and genres
    print(movie_count)
    print(*movie['genres'], sep=", ")