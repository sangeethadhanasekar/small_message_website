
import spotipy
import requests
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
client_id = 'f0fcf19585fd4ed39ef33b4072db05bd'
client_secret = '7046bfa2118f48b595af1492c8ab9a81'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

base_url='https://open.spotify.com/'
artist_id = '36QJpDe2go2KgaRleHCDTp'

# pull all artists albums
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums',
                 headers=headers,
                 params={'include_groups': 'album', 'limit': 50})
d = r.json()