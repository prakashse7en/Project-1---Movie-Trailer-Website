"""This module is used to provide the values of
title,video id,director,music director and actors info """

__license__ = "Prakash"

import Cinema
import fresh_tomatoes
import urllib
try: import simplejson as json
except ImportError: import json


class AccessMovies:
    
    '''below video id,actor ,music director etc are sent as parameter
    to Movies constructor'''
    
    
   
    okkanmani = Cinema.Movies("OK Kanmani","https://www.youtube.com/watch?v=2mBG4vlhcCc","http://goo.gl/tAVp3x","2mBG4vlhcCc",json,"Dulquer salmaan","Nithya Menen","Mani Ratnam","A. R. Rahman")
    aayirathilOruvan = Cinema.Movies("Aayirathil Oruvan","https://www.youtube.com/watch?v=twbmCjTEx5g","http://goo.gl/1Y3yrH","rFG1Ak49agk",json,"Reemma sen","Karthi","Selvaraghavan","G. V. Prakash Kumar")
    aaythaezhuthu = Cinema.Movies("Aaytha Ezhuthu","https://www.youtube.com/watch?v=kiuOvdYBCzI","http://goo.gl/8xRx5g","P6glPdQB_7E",json,"Suriya","R. Madhavan","Mani Ratnam","A. R. Rahman")
    rangDeBasanthi = Cinema.Movies("Rang De Basanthi","https://www.youtube.com/watch?v=l-BTOTtcGmk","http://goo.gl/FslbqI","l-BTOTtcGmk",json,"Aamir Khan","R. Madhavan","Rakeysh Omprakash Mehra","A. R. Rahman")
    unnaleUnnale = Cinema.Movies("Unnale Unnale","https://www.youtube.com/watch?v=5zjVNdcQY5Q","http://goo.gl/6TTE7X","5zjVNdcQY5Q",json,"Vinay Rai","Tanisha Mukherjee","Jeeva","Harris Jayaraj")
    swades = Cinema.Movies("Swdaes","https://www.youtube.com/watch?v=NC7GuohSdWA","http://goo.gl/E5g2rx","NC7GuohSdWA",json,"Shah Rukh Khan","Gayatri Joshi","Ashutosh Gowariker","A. R. Rahman")
    jigarthanda = Cinema.Movies("Jigarthanda","https://www.youtube.com/watch?v=_T8n-EHr4ZE","http://goo.gl/ReRbxl","_T8n-EHr4ZE",json,"Siddharth","Simhaa","Karthik Subbaraj","Santhosh Narayanan")

    ''' movieList now contains all the information for the movies to
    be displayed'''
    movieList = [rangDeBasanthi,swades,jigarthanda,unnaleUnnale,aayirathilOruvan,aaythaezhuthu,okkanmani]

    fresh_tomatoes.open_movies_page(movieList)

        
