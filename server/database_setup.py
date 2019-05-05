import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Tracks(Base):
    __tablename__ = 'tracks'

    key = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    image = Column(String, nullable=False)
    percent = Column(String, default=0)
    audio = Column(String, default='/output.mp3')

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

engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/tracks')


Base.metadata.create_all(engine)
