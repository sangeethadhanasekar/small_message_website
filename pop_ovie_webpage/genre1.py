from flask import Flask, render_template,request
import  requests
import imdb
from urllib.request import urlopen
from bs4 import BeautifulSoup
api_key="59d5ad58b6b388a288ba8ffa5f0c65ca"
ia = imdb.IMDb()
app=Flask(
    __name__,
    template_folder="client/templates",
    static_folder="client/static",

)
page=1
def get_genre():
    url="https://api.themoviedb.org/3/genre/movie/list?api_key="+api_key+"&language=en-US"
    genre_details=requests.get(url).json()
    #print(genre_details)
    for names,value in genre_details.items():
        for i in range (len(value)):
           movie=value[i]
           genre=movie['name']
           print(genre)

#get_genre()


def get_popular(page):
    url="https://api.themoviedb.org/3/movie/popular?api_key="+api_key+"&language=en-US&page="+str(page)
    popular_details=requests.get(url).json()
   # print(popular_details)
    #print(len(popular_details['results']))
    for i in range(len(popular_details['results'])):
          print(popular_details['results'][i]['title'])
          print("http://image.tmdb.org/t/p/original"+popular_details['results'][i]['poster_path'])
#get_popular(page)


def get_toprated(page):
    url="https://api.themoviedb.org/3/movie/popular?api_key="+api_key+"&language=en-US&page="+str(page)
    toprated_details=requests.get(url).json()
   # print(popular_details)
    #print(len(popular_details['results']))
    for i in range(len(toprated_details['results'])):
          print(toprated_details['results'][i]['title'])
          print("http://image.tmdb.org/t/p/original"+toprated_details['results'][i]['poster_path'])
#get_toprated(page)





def get_recent(page):
    url="https://api.themoviedb.org/3/movie/now_playing?api_key="+api_key+"&language=en-US&page="+str(page)
    recent_details=requests.get(url).json()
    #print(recent_details)
    for i in range(len(recent_details['results'])):
        print(recent_details['results'][i]['original_title'])
        print("http://image.tmdb.org/t/p/original"+recent_details['results'][i]['poster_path'])

#get_recent(page)


def movie_description(movie_name):
    url="https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=en-US&query="+str(movie_name)+"&page=1&include_adult=false"
    movie=requests.get(url).json()

    try:
       for i,j in movie["results"][0].items():
           print(i,j)
    except:
       print("error,invalid syntax")
#print(movie_description("three idiots"))

def cast(movie_name):
    url="https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=en-US&query="+str(movie_name)+"&page=1&include_adult=false"
    movie=requests.get(url).json()
    movie_id=movie["results"][0]['id']
    cast_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"/credits?api_key="+api_key+"&language=en-US"
    cast=requests.get(cast_url).json()
    for i in range(len(cast['cast'])):
            originalname=cast['cast'][i]['original_name']
            print(originalname)
            role=cast['cast'][i]['character']
            print(role)
            if cast['cast'][i]['profile_path'] == None:
                print("profile id not available")
            else:
                profilepath = "http://image.tmdb.org/t/p/original" + cast['cast'][i]['profile_path']
                print(profilepath)

#cast("three idiots")


def movie_description2(movie_name):
    url="https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=en-US&query="+str(movie_name)+"&page=1&include_adult=false"
    movie=requests.get(url).json()
    movie_id=movie["results"][0]['id']
    #print(movie_id)
    movie_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+api_key+"&language=en-US"
    movie_desc=requests.get(movie_url).json()
    #print(movie_desc)
    #for i,j in movie_desc.items():
     #   print("'"+i+"'"+":",j)
    genre=[]
    for i in range(len(movie_desc['genres'])):
         genre.append(movie_desc['genres'][i]['name'])
    print("geners:", genre)
    review=movie_desc['overview']
    print("\nreview:",review)
    popular=movie_desc['popularity']
    print("popularity:",popular)
    poster_path="http://image.tmdb.org/t/p/original"+movie_desc['poster_path']
    print("poster_path:",poster_path)
#print(movie_description2("three idiots"))


def movie_gallery(movie_name):
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + str(movie_name) + "&page=1&include_adult=false"
    movie = requests.get(url).json()
    movie_id = movie["results"][0]['id']

    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    movie_desc = requests.get(movie_url).json()

    id=movie_desc["imdb_id"]
    img_url="https://www.imdb.com/title/"+str(id)+"/mediaindex/?ref_=tt_mi_sm"

    print(img_url)
    try:
        page = urlopen(img_url)
       # print(page)
    except:
        print("Error opening the URL")


    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)

    for a in soup.find_all('a'):
        if a.img:
            print(a.img['src'])

#movie_gallery("frozen")

def get_generee():
    movie_desc={}
    url="https://api.themoviedb.org/3/genre/movie/list?api_key=59d5ad58b6b388a288ba8ffa5f0c65ca&language=en-US"
    gene_name = requests.get(url).json()
    print(gene_name)
    name=input("enter mvie name:")
    for i in range(len(gene_name['genres'])):
       if name.title() in gene_name['genres'][i]['name']:
           movie_desc=gene_name['genres'][i]

    gen_movie_url="https://api.themoviedb.org/3/discover/movie?api_key="+ api_key +"&with_genres="+str(movie_desc['id'])
    gene_movie_name = requests.get(gen_movie_url).json()
    print(gene_movie_name)
    for i in range(len(gene_movie_name['results'])):
          genre_movie[gene_movie_name['results'][i]['original_title'])]="http://image.tmdb.org/t/p/original"+gene_movie_name['results'][i]['poster_path']
   # for i in range(len(gene_movie_name['results'])):
    #    print(i)
get_generee()