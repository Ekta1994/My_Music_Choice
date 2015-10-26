"""
Created on Tue Oct 6 23:30:25 2015

@author: Ekta
Email-id: ektagoel04@gmail.com

"""

from bs4 import BeautifulSoup
import urllib,re
import requests
import json


MY_KEY  = "Your_key_here"
YOUTUBE_SERVICE_BASE_URL = "https://www.googleapis.com/youtube/v3/"
FREEBASE_SERVICE_URL = "https://www.googleapis.com/freebase/v1/topic"
PLAYLIST_ID = "your_id_here"
MAX_LIMIT = "Your_desired_limit"


def fetch_my_playlist (playlistid) :
    
     api_call_url = YOUTUBE_SERVICE_BASE_URL + "playlistItems?part=snippet"
     api_call_url = api_call_url + "&maxResults=" + str(MAX_LIMIT) +"&playlistId=" + playlistid + "&key=" + MY_KEY
    
     songs_json = urllib.request.urlopen(api_call_url)
     r = requests.get(api_call_url)
     playlist_obj = json.loads(r.text) 
     
     #the JSON object here corresponds to image JSONresponse1.png
    
     videos = []
     
     song_wrappers = playlist_obj['items']
     for song_wrapper in song_wrappers:
        video_id = song_wrapper['snippet']['resourceId']['videoId']
        videos.append(video_id)
       
     return videos  
     
     
     
#Services -> YouTube Data API v3 -> youtube.videos.list
def get_song_topics(playlist_video_id) :
    
    #These URLs can be generated by entering the required fields in the API explorer
    api_call_url = YOUTUBE_SERVICE_BASE_URL + "videos?part=topicDetails&id=" + playlist_video_id + "&key=" + MY_KEY
    
    #print("ApI call for getting topics for the song " + api_call)
    
    topics = None
    
    songs_json = urllib.request.urlopen(api_call_url)
    r = requests.get(api_call_url)
    
    #See JSONresponse2.png to see the object corresponding to the above line
    playlist = json.loads(r.text)    
    
    topics = playlist['items'][0]['topicDetails']['topicIds']
    
    return topics

def get_genres_for_song_from_wiki(url):
    
    genres = []
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    #Refer Infobox_inspect.png for understanding the below code.
    infobox = soup.find('table', {'class' : re.compile(r".*infobox.*")})
    rows = infobox.findAll('tr')
    for row in rows:
        key = ""
        try:
            th = row.find('th', {'scope' : 'row'})
               
            key = th.text.strip()
        except (Exception) :
           continue;
            
        if "Genre" in key:
            td = row.find('td')
            links = td.findAll('a')

            for link in links:                
                if ( str(link.string) != 'None') :
                    genres.append(str(link.string)) 
    
    genres = list(set(genres))
    return genres
    

def do_freebase_call(topic) :
    
    url = FREEBASE_SERVICE_URL + topic + "?key=" + MY_KEY
    r = requests.get(url)
    topic = json.loads(r.text)
    gen = []
    
    #Using TOPIC API here
    #Look at JSON_response3.png for checking out the JSON object fetched in above code
    #The below things will be easy to understand then
    notable_for_obj = topic['property']['/common/topic/notable_for']
    notable_for = notable_for_obj['values'][0]['id'].lower()
        
    notable_types_obj = topic['property']['/common/topic/notable_types']
    notable_types = notable_types_obj['values'][0]['id'].lower()   
    
    category = None
    if "/music/genre" in notable_for or "/music/genre" in notable_types:
        category = "music genre"
    elif "celebrity" in notable_types or "celebrity" in notable_for:
        category = "artist"  
    elif "music" in notable_types or "music" in notable_for:
        category = "music single"
            
    if category == "music genre":
            raw_genres = topic['property']['/type/object/name']['values']
         
            #Refer JSON_response4.png for this
            for g in raw_genres :
                gen.append(str(g['text']))
            
    elif category == "music single" or category == "artist" :
            #Retrievng genres via Wikipedia's link ( InfoBox )
    
            if '/common/topic/description' in topic['property']:
                wiki_link = str(topic['property']['/common/topic/description']['values'][0])

                if 'citation' in wiki_link:                
                
                    wiki_link = topic['property']['/common/topic/description']['values'][0]['citation']['uri'].strip()
                    gen = get_genres_for_song_from_wiki(wiki_link)
                 
    return gen
    
def get_genres_from_topics(topic_list):

    g = []    
    
    for topic in topic_list:
        this_topic_list = do_freebase_call(topic)
        
        if len(this_topic_list) != 0 : 
            g.append(this_topic_list)
        
    return g

def get_my_choice(playlistId) :
    
    videos = fetch_my_playlist(playlistId)
    
    #Uncommenting the below line prints the video-id(as on You-Tube) of all the songs in the playlist
    #print(videos)
        
    list_of_genres = []
    
    for video_id in videos:
        
        #We now wil extract the topics for each video-id
        topic_list = get_song_topics(video_id)
        
        #Uncommenting the below line will print the topic list of the song/video under consideration
        #print(topic_list)
        
        genres= get_genres_from_topics(topic_list)
        #print(genres)

        if len(genres) != 0 :        
            list_of_genres.append(genres)
    
    #print("The list of genres")
    #print(list_of_genres)
    
    #Creating a dictionary with the key as teh Genre and value as the occurrences of it in my playlist
    gen_stats = {}
    
    for i in range(0,len(list_of_genres)) :
        for j in range(0,len(list_of_genres[i])) :
            for k in range(0,len(list_of_genres[i][j])):
                h = list_of_genres[i][j][k]
                
                gen_cnt = 1
                
                if h in gen_stats:
                    gen_cnt = 1+ gen_stats[h]
            
                gen_stats[h]= gen_cnt
            
    print(gen_stats.items())
            
            
if __name__ == '__main__':
    
    #Your playlist as an argument here
    get_my_choice(PLAYLIST_ID)