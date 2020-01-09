from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Tracks, Artists, Genres


def remake_db():
    #creates and drops database
    # Will be called for every test 

    db.session.commit()
    db.drop_all()
    db.create_all()

    #creates test artists
    artist1 = Artists(name = "keeno", default_genre = "liquid")
    artist2 = Artists(name = "dilated peoples", default_genre = "hiphop")

    
    genre1 = Genres(name="liquid", folder_path = "/opt/flask-app/music/liquid")
    genre2 = Genres(name = "hiphop", folder_path = "/opt/flask-app/music/hiphop")
    
    track1 = Tracks(title = "You Can't Hide, You Can't Run (prod. by Evidence)", filename = "test.mp3", album = "20/20", artist_id = "2",genre_id = "2")
    track2 = Tracks(title = "Guesswork", filename = "test2.mp3", album = "All The Shimmering Things", artist_id = "1", genre_id = "1")
    track3 = Tracks(title = "deletetest", filename = "musicfileexample1.mp3", album = "", artist_id = "1", genre_id = "1")
    #saves users to database

    db.session.add(artist1)
    db.session.add(artist2)
    db.session.add(genre1)
    db.session.add(genre2)
    db.session.add(track1)
    db.session.add(track2)
    db.session.add(track3)

    db.session.commit()