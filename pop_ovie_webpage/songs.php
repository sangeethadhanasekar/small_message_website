

def movie_gallery(movie_name):
    url = "https://api.themoviedb.org/3/search/movie?api_key=" + api_key + "&language=en-US&query=" + str(movie_name) + "&page=1&include_adult=false"
    movie = requests.get(url).json()
    movie_id = movie["results"][0]['id']

    movie_url = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key + "&language=en-US"
    movie_desc = requests.get(movie_url).json()

    id=movie_desc["imdb_id"]
    print(id)
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
#def get_img(movie_name):










function 1:
*it should give top 12 popular movie,12 recent movie with their poster.
*it should also give most visited in this site with their poster.

function 2:
*list of all movies in alphabetical order with there poster.

function 3: input(genre)
it should give all movies name under the gere with there poster.

function 4: input(movie name)
*it should give: genre of the movie, rating, director, writer, running time and summary.
*watch link.
*images for gallery.
*cast name with there image and profile link.
*songs link.














