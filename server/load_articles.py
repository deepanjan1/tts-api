from flask import jsonify

# Account information
from config import POCKET_KEY, ACCESS_TOKEN

# to read APIs
import requests
import json

# URL encoding
import urllib.parse

# for parsing HTML
from bs4 import BeautifulSoup
import lxml
import re

# function that loads articles from database
def loadArticlesDB(tracks):
    '''takes a DB query object called tracks, and outputs
    a jsonified version for javascript to loop through'''
    track_list = []
    for track in tracks:
        track_list.append(
            {
                'key': track.key,
                'title': track.title,
                'text': track.text,
                'image': track.image,
                'percent': track.percent,
                'audio': track.audio,
            }
        )
    return (jsonify(track_list))

# function that loads articles from API
def loadArticlesAPI():
    '''function calls all articles from Pocket; this function is exported'''
    parameters = {
    'access_token': ACCESS_TOKEN,
    'consumer_key': POCKET_KEY,
    'count': 2,
    }
    url = 'https://getpocket.com/v3/get'

    response = requests.post(url, data = parameters)

    articles_json_raw = json.loads(response.text)

    articles_json = []
    for key in articles_json_raw['list']:
        articleObject = articles_json_raw['list'][key]

        if readableArticleValidator(articleObject):
            article_json = articleObjectCreator(articleObject, key)
            articles_json.append(article_json)

    return (articles_json)

# find new tracks based on what's in the DB vs. what's the latest 15 in Pocket
def findNewTracks(tracks_db_keys_collection, tracks_api):
    '''input tracks from DB and tracks from Pocket,
    output only the new entries in json format'''
    tracks_api_keys = []
    tracks_db_keys = []

    # create a list of keys from Pocket API
    for track in tracks_api:
        tracks_api_keys.append(track['key'])

    for key in tracks_db_keys_collection:
        tracks_db_keys.append(key[0])

    # convert to sets
    tracks_db_keys = set(tracks_db_keys)
    tracks_api_keys = set(tracks_api_keys)

    new_tracks_keys = list(tracks_api_keys - tracks_db_keys)

    # pull out the full track objects for new tracks
    new_tracks = []
    for new_track_key in new_tracks_keys:
        for track_api in tracks_api:
            if track_api['key'] == new_track_key:
                new_tracks.append(track_api)
    return (new_tracks)

####### Helper functions to not be exported #######

def readableArticleValidator(articleObject):
    '''ensures the article has content to read'''
    if articleObject['word_count'] != '0':
        return True
    else:
        return False

def articleObjectCreator(articleObject, key):
    '''checks for whether the article has an
    image and title and creates object'''
    if articleObject['resolved_title'] != '':
        title = articleObject['resolved_title']
    else:
        title = articleObject['given_title']

    # if image is not present, it pulls an image from ui-avatars API
    if 'top_image_url' in articleObject:
        image = articleObject['top_image_url']
    else:
        image = requests.get('https://ui-avatars.com/api/', {'name': title}).url

    articleText = retrieveText(articleObject['resolved_url'])
    article_json = {
    'title': title,
    'percent': 0,
    'key': key,
    'image': image,
    'text': articleText,
    }

    return article_json

def retrieveText(url):
    '''Retrieves text using Pocket's text parser API.
    Inputs: URL, Outputs: object that includes the HTML text'''

    apiURL = 'https://text.getpocket.com/v3/text'

    # build data object with no images or videos
    data = {
    'consumer_key': POCKET_KEY,
    'url': url,
    'images': 0,
    'videos': 0,
    'output': 'json',
    }

    response = requests.post(apiURL, data=data)
    response_json = json.loads(response.text)

    # parse out text only from HTML
    soup = BeautifulSoup(response_json['article'], 'lxml')
    text_ascii = re.sub('(\n|\r)', ' ', soup.get_text())\
    .replace('\u2019', "'")\
    .replace('\"', '"')
    return text_ascii
