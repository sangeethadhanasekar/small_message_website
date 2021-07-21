import random

from urllib.request import urlopen
from bs4 import BeautifulSoup

import urllib.request
import urllib.parse
import re
import webbrowser as wb
import  requests
api_key="59d5ad58b6b388a288ba8ffa5f0c65ca"



def movie_link(movie_name):


#movie_link("3 idiots




        a = (movie_name.replace(' ', '%20'))
        print("https://www.hotstar.com/in/search?q=" + a)
        songplaylist = (movie_name.replace(' ', '+'))
        playlist = "https://www.youtube.com/results?search_query=" + songplaylist + "+soundtrack+playlist+"
        print(playlist)



        html = urllib.request.urlopen(playlist)
        #video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode()
        video_id = re.findall(r"list=(\S{34})", html.read().decode())
        print("https://www.youtube.com/playlist?list=" + video_id[0])

        # for i in range(len(video_ids)):
          #print("https://www.youtube.com/watch?v=" + video_ids[i])
        '''from youtubesearchpython import ChannelsSearch

        channelsSearch = ChannelsSearch(movie_name+'movie+all+song+playlist+', limit = 10, region = 'US')

        print(channelsSearch.result())'''


movie_link("to story")



