
import os
import sys
import datetime

# local imports 
from app import db, login


class Tracks(db.Model):
    '''
    Store track information including text
    '''
    __tablename__ = 'tracks'


    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    audio = db.Column(db.String, default='None')
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    
    def __init__(self, data):
        """
        Class constructor
        """
        self.key = data['key']
        self.title = data['title'],
        self.text = data['text'],
        self.image = data['image'],
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
    
    def save(self):
        db.session.add(self)

    def update(self, data):
      for key, item in data.items():

        # handle certain google user attributes separately
        if key in ['google_refresh_token', 'slack_access_token']:
          if item and type(item) is str:
            self.set_token(key, item)
          continue
        if key == 'id':
          setattr(self, 'google_id', item)
          continue
        if key in ['given_name', 'family_name', 'verified_email']:
          continue
        setattr(self, key, item)
      self.modified_at = datetime.datetime.utcnow()

    def delete(self):
      db.session.delete(self)
      @property
      def serialize(self):
          """Return object data in easily serializeable format"""
          return {
              'key': self.key,
              'title': self.title,
              'text': self.text,
              'image': self.image,
              'percent': self.percent,
              'audio': self.audio,
          }
    
    @staticmethod
    def get_all_tracks():
      return Tracks.query.all()

    def storeAudioPath(self, track, key):
        '''Takes in the audio path and DB session as input, stores
        the audio path and outputs a confirmation'''

        track.audio = 'file://server/audio_file/' + key + '.mp3'
        db.session.commit()
        status = f'{track.audio} is the new path.'
        return (status)
