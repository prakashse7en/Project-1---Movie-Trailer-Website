"""This module is used to intialize movie
attributes(actor,director,title etc) and
get the json response from you tube   """

__license__ = "Prakash"

import webbrowser
import urllib
try: import simplejson as json
except ImportError: import json


class Movies():
    
    def __init__(self,title,trailer_youtube_url,poster_image_url,video_id,json,actor1,actor2,director,musicdirector):
        '''Constructor used to intialize movie attributes(actor,director etc) and get json response from
           youtube by sending video id '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.video_id = video_id
        #construct json response starts
        url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % video_id
        json = json.load(urllib.urlopen(url))
        self.json = json
        
        #construct json response ends
        
        self.json = json    
        self.actor1 = actor1
        self.actor2 = actor2
        self.director = director
        self.musicdirector = musicdirector

    

    
        
