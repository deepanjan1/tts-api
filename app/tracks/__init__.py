from flask import Blueprint

bp = Blueprint('tracks', __name__)

from app.tracks import routes