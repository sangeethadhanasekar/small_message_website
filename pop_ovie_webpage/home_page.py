import  requests
api_key="59d5ad58b6b388a288ba8ffa5f0c65ca"
top_popular_movies ={}
recent_movies={}
home_page={}

def function_1():
    page=1
    url="https://api.themoviedb.org/3/movie/popular?api_key="+api_key+"&language=en-US&page="+str(page)
    toprated_details=requests.get(url).json()

    for i in range(len(toprated_details['results'])):
          top_popular_movies[toprated_details['results'][i]['title']]="http://image.tmdb.org/t/p/original"+toprated_details['results'][i]['poster_path']


    url="https://api.themoviedb.org/3/movie/now_playing?api_key="+api_key+"&language=en-US&page="+str(page)
    recent_details=requests.get(url).json()
    for i in range(len(recent_details['results'])):
        recent_movies[recent_details['results'][i]['original_title']]="http://image.tmdb.org/t/p/original"+recent_details['results'][i]['poster_path']

function_1()
home_page['recent']=recent_movies
home_page['popular']=top_popular_movies

print(home_page)