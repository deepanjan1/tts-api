from flask import Flask, request, redirect, jsonify, url_for
from load_articles import loadArticles
from tts import createAudioFile
from config import POCKET_KEY, ACCESS_TOKEN

# to read APIs
import requests
import json

app = Flask(__name__)

@app.route('/tracks')
def getTracks():
    tracks = loadArticles()
    return (tracks)

@app.route('/audio/mp3')
def getAudio():
    '''get track text, convert and store audio, output audio file'''
    return (createAudioFile())

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
