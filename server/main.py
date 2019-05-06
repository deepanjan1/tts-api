# import flask modules
from flask import Flask, request, redirect, jsonify, url_for

# import for database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Tracks

# import helper functions
from load_articles import loadArticles
from tts import createAudioFile

# import config modules
from config import POCKET_KEY, ACCESS_TOKEN

# to read APIs
import requests
import json

app = Flask(__name__)

# connect to a postgres database
engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/tracks')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/tracks')
def getTracks():
    tracks = loadArticles()
    return (jsonify(tracks))

@app.route('/init')
def initDBWithTracks():
    ''' currently just doing a straight upload into database.
    need to change this to actually only update with new entries'''

    tracks = loadArticles()
    for track in tracks:
        new_track = Tracks(
        key = track['key'],
        title = track['title'],
        text = track['text'],
        image = track['image'],
        percent = track['percent']
        )
        session.add(new_track)
    session.commit()
    return ('Check database, tracks should be initialized')


@app.route('/audio/<int:audio_key>/mp3')
def getAudio(audio_key):
    '''get track text, convert and store audio, output audio file'''

    return (str(audio_key))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
