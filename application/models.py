from application import db,login_manager
from flask_login import UserMixin
from datetime import datetime

#project tables

class Artists(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String(100), nullable=False, unique= True)
    default_genre = db.Column(db.String(100),nullable = False, unique= True)
    tracks = db.relationship('Tracks', backref = 'artist', lazy = True)

class Genres(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    folder_path = db.Column(db.String(100), nullable = False, unique = True)
    tracks = db.relationship('Tracks', backref = 'genre', lazy = True)

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique = True)
    title = db.Column(db.String(100), nullable = False)
    filename = db.Column(db.String(100), nullable = False, unique = True)
    album = db.Column(db.String(100), nullable = False)
    artist_id = db.Column(db.Integer,db.ForeignKey('artists.id'))
    genre_id = db.Column(db.Integer,db.ForeignKey('genres.id'))



