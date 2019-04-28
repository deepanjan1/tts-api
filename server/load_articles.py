from flask import jsonify

# Account information
from config import POCKET_KEY, ACCESS_TOKEN

# to read APIs
import requests
import json

# function that loads articles
def loadArticles():
    '''function calls all articles from Pocket; this function is exported'''
    parameters = {
    'access_token': ACCESS_TOKEN,
    'consumer_key': POCKET_KEY,
    'count': 10,
    }
    url = 'https://getpocket.com/v3/get'

    response = requests.post(url, data = parameters)
    # response_escape = response.text.replace('\ ', '')
    articles_json_raw = json.loads(response.text)

    articles_json = []
    for key in articles_json_raw['list']:
        articleObject = articles_json_raw['list'][key]
        # print (articleObject)
        if readableArticleValidator(articleObject):
            # article_json = {
            # 'title': articleObject['resolved_title'],
            # 'percent': 0.2,
            # 'key': key,
            # 'image': articles_json_raw['list'][key]['top_image_url'],
            # }
            article_json = articleObjectCreator(articleObject, key)
            articles_json.append(article_json)

    # print (articles_json)
    # print (articles_json_raw['list'])
    return (jsonify(articles_json))

## Helper functions to not be exported ##

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

    article_json = {
    'title': title,
    'percent': 0.2,
    'key': key,
    'image': image,
    }

    return article_json
