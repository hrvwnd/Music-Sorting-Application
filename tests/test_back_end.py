import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Tracks, Artists, Genres
from application.py.remake_db import remake_db
from application.routes import delete

class UnitBase(TestCase):

    def create_app(self):
        #pass in test configurations
        config_name = "testing"
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('MYSQL_USER'))+':' \
                +str(getenv('MYSQL_PASSWORD'))+'@'+str(getenv('MYSQL_HOST'))+'/'+str(getenv('MYSQL_DB_TEST')))
        return app 
        

    def setup(self):
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
        track3 = Tracks(title = "deletetest", filename = "musicfileexample1.mp3", album = "album_test", artist_id = "1", genre_id = "1")
        #saves users to database

        db.session.add(artist1)
        db.session.add(artist2)
        db.session.add(genre1)
        db.session.add(genre2)
        db.session.add(track1)
        db.session.add(track2)
        db.session.add(track3)

        db.session.commit()

    def TearDown(self):
        # drops all created databases 

        db.session.remove()

        db.drop_all()

class UnitTest(UnitBase):
    # testing accessability of webpages 

    def test_sort_with_url(self):
        # is testing page reachable 
        response = self.client.get(url_for('sort'))
        self.assertEqual(response.status_code, 200)

    def test_amend_directory_url(self):
        response = self.client.get(url_for('amend_directory'))
        self.assertEqual(response.status_code, 200)

    def test_update_artist_genre_url(self):
        response = self.client.get(url_for('update_artist_genre'))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_url(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 200)

    def test_amend_directory_post(self):
        # create test post
        genretest = Genres(name="testgenre", folder_path = "/opt/flask-app/music/genretest")
        # save post to database
        db.session.add(genretest)
        db.session.commit()
        self.assertEqual(Genres.query.count(), 3)
    """
    def test_delete_delete(self):
        #tests the delete functionality of the app
        Tracks.query.filter_by(title = "deletetest").delete()
        self.assertEqual(Tracks.query.count(),2)
    """


    

    

