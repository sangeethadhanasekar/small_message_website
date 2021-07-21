import  requests
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

api_key="59d5ad58b6b388a288ba8ffa5f0c65ca"
gallery={}
cast_name=[]
top_popular_movies ={}
recent_movies={}
genre_movie={}
movie_desc={}
video_link={}
song_link={}
first_gallery=[]
top_five_cast=[]


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

def function_3(genre_name_gn):
    movie_desc = {}
    page=2
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key=59d5ad58b6b388a288ba8ffa5f0c65ca&language=en-US"
    gene_name = requests.get(url).json()

    name = genre_name_gn     #input("enter mvie name:")
    for i in range(len(gene_name['genres'])):
        if name.title() in gene_name['genres'][i]['name']:
            movie_desc = gene_name['genres'][i]

    gen_movie_url = "https://api.themoviedb.org/3/discover/movie?api_key=" + api_key + "&with_genres=" + str(movie_desc['id'])+"&page="+str(page)
    gene_movie_name = requests.get(gen_movie_url).json()

    for i in range(len(gene_movie_name['results'])):
        genre_movie[gene_movie_name['results'][i]['original_title']]=" http://image.tmdb.org/t/p/original" +gene_movie_name['results'][i]['poster_path']
function_3("Action")

def function_4(movie_name):
    page=1
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + str(movie_name) + "&page=1&include_adult=false"
    movie = requests.get(url).json()
    movie_id = movie["results"][0]['id']
    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"

    movie_desc_json = requests.get(movie_url).json()

    '''MOVIE DESC     ******************************************************************************************************'''
    genre = []
    for i in range(len(movie_desc_json['genres'])):
        genre.append(movie_desc_json['genres'][i]['name'])
    s=','
    strings=s.join(genre)


    movie_desc['movie_name']=movie_desc_json['original_title']
    movie_desc['genre'] = strings
    movie_desc['overview'] = movie_desc_json['overview']
   
    movie_desc['poster_path'] = "http://image.tmdb.org/t/p/original" + movie_desc_json['poster_path']
    movie_desc['rating'] = movie_desc_json['vote_average']
    movie_desc['release_date'] = movie_desc_json['release_date']
    production=[]
    for i in range(len(movie_desc_json['production_companies'])):
                    production.append(movie_desc_json['production_companies'][i]['name'])
    prod_name=s.join(production)
    movie_desc['production_company']=prod_name

    sec=movie_desc_json['runtime']
    movie_desc['runtime']=str(datetime.timedelta(minutes=sec))
    person_url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"/credits?api_key="+ str(api_key)+"&language=en-US"
    person_url_json=requests.get(person_url).json()
    director=[]
    for i in range(len(person_url_json['crew'])):
        if person_url_json['crew'][i]['job']=='Director':
            director.append(person_url_json['crew'][i]['name'])
    movie_desc['director']=s.join(director)
    '''trailer link ****************************************************************************************************************'''
    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    movie_descs = requests.get(movie_url).json()
    id = movie_descs["imdb_id"]
    trailer_url="https://api.themoviedb.org/3/movie/"+str(id)+"/videos?api_key="+ api_key
    trailer_descs = requests.get(trailer_url).json()
    trailer_key=trailer_descs['results'][0]['key']
    youtube_link="https://www.youtube.com/watch?v="+str(trailer_key)
    movie_desc['trailer link'] = youtube_link

    '''GALLERY ****************************************************************************************************************'''
    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    movie_descs = requests.get(movie_url).json()
    id = movie_descs["imdb_id"]
    img_url = "https://www.imdb.com/title/" + str(id) + "/mediaindex/?ref_=tt_mi_sm"
    try:
        page = urlopen(img_url)
    except:
        print("Error opening the URL")

    soup = BeautifulSoup(page, 'html.parser')
    img_list=[]
    for a in soup.find_all('a'):
        if a.img:
            img_list.append(a.img['src'])
            gallery['images']=img_list
    first_gallery.append(gallery['images'][10:-10])
    ''' cast name with there image and profile link.*********************************************************************************'''
    cast_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "/credits?api_key=" + api_key + "&language=en-US"
    cast = requests.get(cast_url).json()
    for i in range(len(cast['cast'])):
        casts = {}
        original_name = cast['cast'][i]['original_name']
        casts['original_name']=original_name
        profile_url='https://en.wikipedia.org/wiki/'+str(original_name).replace(' ', '_')
        casts['profile_url'] =profile_url
        if cast['cast'][i]['profile_path'] == None:
            casts['profile_img']="profile id not available"
        else:
            profile_path = "http://image.tmdb.org/t/p/original" + cast['cast'][i]['profile_path']
            casts['profile_img'] = profile_path
        cast_name.append(casts)
    top_five_cast.append(cast_name[0:6] )


    a = (str(movie_name).replace(' ', '%20'))
    b = (a.replace('%20', '+'))

    """ hotstar link"""
    video_link['hotstar link']="https://www.hotstar.com/in/search?q=" + a

    """amazon prime link """
    video_link['amazon prime link']='https://www.primevideo.com/search/ref=atv_nb_sr?phrase=' + a

    """netflix link """
    video_link['netflix'] = 'https://www.netflix.com/search?q=' + a + '%202'

    """ youtube songs link"""
    song_link['youtube songs link']='https://www.youtube.com/results?search_query=' + b + '+songs&sp=EgIQAw%253D%253D'

    """ spotify link"""
    song_link['spotify link']="https://open.spotify.com/search/" + a + "/playlists"

function_4('frozen')
'''print(movie_desc)
print(gallery)
print(cast_name)
print(video_link)
print(song_link)
print(top_popular_movies)
print(recent_movies)
print(genre_movie)'''
#print(len(gallery['images']))
#print(gallery)
#print(cast_name)
print(movie_desc)
#print(top_five_cast[0])
#print(len(first_gallery[0]))