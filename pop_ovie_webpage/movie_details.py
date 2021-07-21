
import imdb
import  requests




api_key="59d5ad58b6b388a288ba8ffa5f0c65ca"
ia = imdb.IMDb()
# give similar mcvie names hera in name variable
#name = "3 idiots"
"""
def movie_description(movie_name):
    url="https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=en-US&query="+str(movie_name)+"&page=1&include_adult=false"
    movie=requests.get(url).json()

    try:
       for i,j in movie["results"][0].items():
           print(i,j)
    except:
       print("error,invalid syntax")
#print(movie_description("Our Idiot Brother"))
search = ia.search_movie(name)
i=1
for movie in search:
    print(movie)
    print(movie_description(movie))
    print(i)
    print("***************************************************************************")
    i=i+1

"""
def movie_description(movie_name):
    url="https://api.themoviedb.org/3/search/movie?api_key="+api_key+"&language=en-US&query="+str(movie_name)+"&page=1&include_adult=false"
    movie=requests.get(url).json()
    movie_id=movie["results"][0]['id']
    print(movie_id)

    movie_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+api_key+"&language=en-US"
    movie_desc=requests.get(movie_url).json()
    #print(movie_desc)
    for i,j in movie_desc.items():
       print("'"+i+"'"+":",j)
    genre=[]
    for i in range(len(movie_desc['genres'])):
         genre.append(movie_desc['genres'][i]['name'])
    print("geners:", genre)
    review=movie_desc['overview']
    print("\nreview:",review)
    popular=movie_desc['popularity']
    print("popularity:",popular)
    rating=movie_desc['vote_average']
    print("rating:",rating)
    poster_path="http://image.tmdb.org/t/p/original"+movie_desc['poster_path']
    print("poster_path:",poster_path)

    trailer_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"/videos?api_key="+api_key+"&language=en-US"
    trailer_desc = requests.get(trailer_url).json()
    #print(trailer_desc)
    key=trailer_desc['results'][1]['key']
    youtube_link='https://www.youtube.com/watch?v='+str(key)
    print(youtube_link)


def movie_gallery(movie_name):
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + str(movie_name) + "&page=1&include_adult=false"
    movie = requests.get(url).json()
    movie_id = movie["results"][0]['id']

    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    movie_desc = requests.get(movie_url).json()
    # print(movie_desc)
    for i, j in movie_desc.items():
        print("'" + i + "'" + ":", j)
    id=movie_desc["imdb_id"]
    img_url="https://www.imdb.com/title/"+str(id)+"/?ref_=fn_al_tt_1"
    print(img_url)

    req = session.get(img_url)
    bs = BeautifulSoup(req.text, 'html.parser')

    link_box = bs.find_all('div', attrs={'class': ''})

    for links in link_box:
        print(links['href'])


movie_gallery("three idiots")







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

#print(movie_description("three idiots"))
#cast("three idiots")
