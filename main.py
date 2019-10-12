# import flask modules
from flask import Flask, request, redirect, jsonify, url_for

# import for database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Tracks

# import helper functions
from load_articles import loadArticlesAPI, loadArticlesDB, findNewTracks
from tts import createAudioFile
from db_helpers import storeNewTracks, storeAudioPath

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

@app.route('/tracks', methods=['GET'])
def getTracks():
    try:
        tracks = session.query(Tracks).all()
        track_list = loadArticlesDB(tracks)
    except:
        session.rollback()
        raise
    return (track_list)

@app.route('/newtracks', methods=['GET'])
def newTracks():
    '''Calls Pocket API, stores tracks in DB, and
    outputs tracks that are brand new'''
    # grabbing latest 15 articles from Pocket
    tracks_api = loadArticlesAPI()
    try:
        track_db_keys = session.query(Tracks.key).all()
    except:
        session.rollback()
        raise

    # outputs new tracks as full objects with all track information
    new_tracks = findNewTracks(track_db_keys, tracks_api)

    # store new tracks within DB
    if len(new_tracks) > 0:
        storeNewTracks(new_tracks, session)
        return (jsonify(True))
    else:
        return (jsonify(False))

@app.route('/init')
def initDBWithTracks():
    ''' currently just doing a straight upload into database.
    need to change this to actually only update with new entries'''
    session.rollback()
    session.query(Tracks).delete()
    tracks = loadArticlesAPI()
    status = storeNewTracks(tracks, session)
    return ('Check database, tracks should be initialized')


@app.route('/audio/<string:audio_key>/mp3')
def getAudio(audio_key):
    '''get track text, convert and store audio, output audio file'''
    track = session.query(Tracks).filter_by(key=audio_key).one()
    audio_file_path = createAudioFile(track.text, audio_key)

    confirmation = storeAudioPath(track, audio_key, session)
    return (confirmation)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
