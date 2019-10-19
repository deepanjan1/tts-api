# actual imports
from flask import (
    make_response,
    redirect,
    url_for,
    flash,
    request
    )

# internal imports
from app.tracks import bp
from app import db
from app.models import Tracks

@bp.route('/tracks', methods=['GET'])
def getTracks():
    try:
        tracks = session.query(Tracks).all()
        track_list = loadArticlesDB(tracks)
    except:
        session.rollback()
        raise
    return (track_list)


@bp.route('/newtracks', methods=['GET'])
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


@bp.route('/init')
def initDBWithTracks():
    ''' currently just doing a straight upload into database.
    need to change this to actually only update with new entries'''
    session.rollback()
    session.query(Tracks).delete()
    tracks = loadArticlesAPI()
    status = storeNewTracks(tracks, session)
    return ('Check database, tracks should be initialized')


@bp.route('/audio/<string:audio_key>/mp3')
def getAudio(audio_key):
    '''get track text, convert and store audio, output audio file'''
    track = session.query(Tracks).filter_by(key=audio_key).one()
    audio_file_path = createAudioFile(track.text, audio_key)

    confirmation = storeAudioPath(track, audio_key, session)
    return (confirmation)
