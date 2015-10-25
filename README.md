# My_Music_Choice
The script aims to analyze my youtube playlist and find the genre of the songs/videos in it. By finding the count of each genre it then creates the word cloud of my choice of the music ( in accordance with the playlist). The Machine Learning algorithms can be applied for finding out patterns and generate a more appropriate word cloud.

**Requirements -:**
 - Python 3/2.7
 - Scikit-learn, if using Python
 - Modules like urllib, request, Beautiful Soup, json
 - Alternative is to use Anaconda
 
**Setup -:**
 - Install Anaconda or Python.
 - Create your youtube channel and then a playlist. Add songs to that playlist of your choice and get its ID.
 - Create a project in the Google Developers Console and obtain authorization credentials so your application can submit API requests.
 - After creating your project, make sure the YouTube Data API is one of the services that your application is registered to use:
	- Go to the Developers Console and select the project that you just registered.
	- Open the API Library in the Google Developers Console. If prompted, select a project or create a new one. In the list of APIs, make sure the status is ON for the YouTube Data API v3.
	- The FreeBase API will also be needed for the script to run. Enable that also.
	
 - Replace the parameters 'MY_KEY' and 'Playlistid' . You can also take a different value for the parameter MAX_LIMIT. Though one'll not be able to go beyond 50 as the youtube data API has that as its maximum limit. Hoever, the problem can be solved by using nextPage and PreviousPage token.
 - Run the script.
 - Currently the code only displays the dictionary having the genre name as its key and value as the key's count. We can generate word cloud using any online wordcloud generator.
 
*Further Code to be done -:**
 - A wordCloud generator
 - Implementation of various ML algorithms on the genre data collected and draw an optimal wordcloud.
 
*References -:**

- https://docs.python.org/2.7/
- https://developers.google.com/youtube/v3/guides/searching_by_topic#Topics_in_the_API
- https://developers.google.com/freebase/mql/ch02
- https://developers.google.com/freebase/mql/ch03
- https://en.wikipedia.org/wiki/Template:Infobox_album