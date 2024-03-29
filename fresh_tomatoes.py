
'''This module is used to override and generate fresh_tomatoes.html
   file with the movie contents appended
in html form '''

__license__ = "Prakash"

import webbrowser
import os
import re
try: import simplejson as json
except ImportError: import json

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Seven Trailers!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	<link rel="stylesheet" type="text/css" href="css/moviestyles.css">
	<script src="js/moviesscript.js"></script>
 
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
	<!-- Header content starts -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container-fluid ">
        <div class="navbar-header">
          <a class="navbar-brand" href="#"><img alt="Trailers" src="images/seven.jpg" style="width:25px;height:23px"> <font face="verdana" color="green">MOVIE TRAILERS</font></a>
        </div>
      </div>
    </nav>
	<!-- Header content ends -->
	
    
    
    
    <div class="container">
      {movie_tiles}
    </div>
	
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="row">

	<div class="col-sm-5 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
		<img src="{poster_image_url}" width="220" height="342">
	</div>
	<div class ="col-sm-7">
		<h2 >{movie_title}</h2>
		<!-- movie info table starts -->
		<table class="table table-hover">
			<tbody>
				<tr>
					<td>
						<h5><B>Starring</B></h5>
					</td>
					<td><h5>{actor1}, {actor2}</h5></td>
				</tr>
				<tr>
					<td>
						<h5><B>Director</B></h5>
					</td>
					<td><h5>{director}</h5></td>
				</tr>	
				<tr>
					<td>
						<h5><B>Music Director</B></h5>
					</td>
					<td><h5>{musicdirector}</h5></td>
				</tr>
				<tr>
					<td>
						<img src="images/like.jpg" alt="Like" style="width:20px;height:20px"/>
					</td>
					<td><h5>{likes_count} <B>Likes</B></h5></td>
				</tr>
				<tr>
					<td>
						<img src="images/dislike.jpg" alt="Dislike" style="width:20px;height:20px"/>
					</td>
					<td><h5>{dislikes_count} <B>Dislikes</B></h5></td>
				</tr>				
			</tbody>
		</table>
		<!-- movie info table ends -->

		<!-- read more/ less starts -->
		<B>Youtube Video Description</B> 
		<div class="main_ctnt">
			<div class="show">

			 <h6 class="extra_content">{more_content}</h6>
			 </div>
		</div>
 
		<!-- read more / less ends -->
		<!--add the title ,info here using the youtube api in acces movies -->
		
	</div>
</div>
<hr class="break-line" style="height:5px;background-color: lightgreen">
'''

def create_movie_tiles_content(movies):

    '''generates the movie content from movies list and places in separate
variables which is later used to display the information in HTML form	'''

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url4
        
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            #likes count fetched from json response using numLikes parameter
            likes_count = movie.json['entry']['yt$rating']['numLikes'],
			#dislikes count fetched from json response using numDislikes parameter
            dislikes_count = movie.json['entry']['yt$rating']['numDislikes'],
			#video description count fetched from json response using media$description parameter
            more_content = unicode(movie.json['entry']['media$group']['media$description']['$t']).encode("utf-8"),
	        actor1 = movie.actor1,
	        actor2 = movie.actor2,
	        director = movie.director,
	        musicdirector = movie.musicdirector
            
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
