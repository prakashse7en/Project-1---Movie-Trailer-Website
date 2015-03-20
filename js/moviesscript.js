$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
	$(function() {
		var showTotalChar = 30, showChar = "Show more (+)", hideChar = "Show less (-)";
		$('.show').each(function() {
			var content = $(this).text();
			if (content.length > showTotalChar) {
				var con = content.substr(0, showTotalChar);
				var hcon = content.substr(showTotalChar, content.length - showTotalChar);
				var txt= con +  '<span class="dots">...</span><span class="morectnt"><span>' + hcon + '</span>&nbsp;&nbsp;<a href="" class="showmoretxt">' + showChar + '</a></span>';
				$(this).html(txt);
			}
		});
		$(".showmoretxt").click(function() {
			if ($(this).hasClass("sample")) {
				$(this).removeClass("sample");
				$(this).text(showChar);
			} else {
				$(this).addClass("sample");
				$(this).text(hideChar);
			}
			$(this).parent().prev().toggle();
			$(this).prev().toggle();
			return false;
		});
	});
        // Animate in the movies when the page loads
       /* $(document).ready(function () {
            //added for hiding more content starts
           
            //added for hiding more content ends
        
            var textArr = []; 
            $('h2').each(function() {
                 textArr.push($(this).text());
            }); 
            alert(textArr.join(','));

        
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });*/