import os
import sys
from sqlalchemy import Column, ForeignKey, Numeric, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

class Tracks(Base):
    '''
    Store track information including text
    '''
    __tablename__ = 'tracks'


    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    image = Column(String, nullable=False)
    audio = Column(String, default='None')
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    
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
        session.add(self)

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

    def storeAudioPath(self, track, key, session):
        '''Takes in the audio path and DB session as input, stores
        the audio path and outputs a confirmation'''

        track.audio = 'file://server/audio_file/' + key + '.mp3'
        session.commit()
        status = f'{track.audio} is the new path.'
        return (status)

engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/tracks')


Base.metadata.create_all(engine)
