# My_Music_Choice
The project aims to analyse the choice of our music by extracting the genre of each song/video and generate an optimal wordcloud. The Machine Learning algorithm applied, takes as features the genre choice of the user's playlist and various parameters of the song like its popularity, number of viewers etc. For the training data, youtube playlist are taken and video-id(and thus topic-id)  etc extraction is done using Youtube Data API(v3). The genre of every song are extracted from FreeBase which is a Creative Commons Licensed repository containing information about millions of topic-id available on youtube. Since it's closed now, they are fetched via Infobox with the use of TOPIC API.

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