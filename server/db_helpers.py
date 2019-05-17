from database_setup import Tracks

def storeNewTracks(tracks, session):
    '''Takes in input of tracks formatted as a list and the DB session.
    Outputs a boolean 'True' once a session is committed with the new
    tracks to DB'''

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
    status = f'{len(tracks)} new tracks added to DB.'
    return (status)
