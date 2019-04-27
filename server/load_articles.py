from flask import jsonify

# Account information
from config import POCKET_KEY, ACCESS_TOKEN

# to read APIs
import requests
import json

# function that loads articles
def loadArticles():
    '''function calls all articles from Pocket'''
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
    for article in articles_json_raw['list']:
        article_json = {
        'title': articles_json_raw['list'][article]['resolved_title'],
        'percent': 0.2,
        # 'image': articles_json_raw['list'][article]['top_image_url'] if articles_json_raw['list'][article]['top_image_url'] is not None else False,
        }
        articles_json.append(article_json)

    print (articles_json)
    return (jsonify(articles_json))
