
                          SEVEN TRAILERS

  What is it?
  -----------
	
  Seven trailers is a movie trailers website where you can watch the trailer of my favourite movies
  Through this site you can view
  
  1) youtube video of the my favourite movie in a modal dialog
  2) Cast ,Director and Music director information are shown
  3) Likes and dislikes of the video are shown. This info is fetched from youtube via json 
  4) small description of the video is shown - This info is also fetched from youtube via json 
  

  Files included
  ------------------
  css    			 - This folder contains moviestyles.css that used to style movie trailer website
  images 			 - This folder contains images to be shown in  movie trailer website
  js    			 - This folder contains moviestyles.js which does the scripting work
  sample_screenshots - This folder contains sample screenshots of movie trailer website
  AccessMov.py		 - This python file is used to generate fresh_tomatoes.html file
  Cinema.py 		 - This python file is used to intialize values like film title,actors etc given in AccessMov.py
  fresh_tomatoes.py	 - This python file is used to show title,starring,director info which is fetched from movie list ,sent from AccessMov.py
  

  Installation 
  ------------
 
 1) Install Idle
	for Windows users -	https://www.udacity.com/course/viewer#!/c-ud036-nd/l-990110642/m-3669178657
	for MAC users     - https://www.udacity.com/course/viewer#!/c-ud036-nd/l-990110642/m-3625658739
 2)Open IDLE and run AccessMov.py
 3) Hooray ! Movie trailers website is launched
 
 
  Working
  ---------
  1) Attributes required to be intialized is created in Cinema.py for eg) starring,director,title are attributes required for each movies
  2) The values for each attributes are sent via AccessMov.py 
  3) once the attributes for each movie is intialized it is added into array list "movieList"
  4) open_movies_page() in fresh_tomatoes.py is called by passing "movieList" which then generates the final html.
  5) In fresh_tomatoes.py each attributes(title,actors,director etc) of the movie is fetched from the list "movieList" and shown
  6) Likes , Dislikes  and youtube video description is fectched from youtube via JSON(Javascript object notation) 
     i)How JSON response is read via Python
		"try: import simplejson as json
		except ImportError: import json " this  way we can use the json library provided by Python.
		url used - 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % video_id  where video Id refers to youtube video id
		--------
		Sample json response is placed in folder "Sample_JSON_Response" . Note - this json response is only for movie Swades
		
  7) Onclick of any movie image in the movie trailer website ,the trailer of the corresponding movie is played in modal dialog.
  8) Each movie related information are placed in table for which boostrap css/js frond end framework is used.
		

  Contacts
  --------

     o please send your queries regarding this project to prakash.dec20@gmail.com 
