import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Tracks, Artists, Genres

class UnitBase(TestCase):

    def create_app(self):
        #creates and drops database
        # Will be called for every test 

        db.session.commit()
        db.drop_all()
        db.create_all()

        #creates test artists

        artist1 = Artists(name = "dilated peoples", default_genre = "hiphop")
        artist2 = Artists(name = "keeno", default_genre = "liquid")

        #saves users to database

        db.session.add(artist1)
        db.session.add(artist2)
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
        self.assrtEqual(response.status_code, 200)

    def test_sort_without_url(self):
        # tests whether the default redirect is sort
        response = self.client.get(url_for(''))
        self.assrtEqual(response.status_code, 200)

    def test_amend_directory_url(self):
        response = self.client.get(url_for('amend_directory'))
        self.assrtEqual(response.status_code, 200)

    def test_update_artist_genre_url(self):
        response = self.client.get(url_for('update_artist_genre'))
        self.assrtEqual(response.status_code, 200)
    
    def test_delete_url(self):
        response = self.client.get(url_for('delete'))
        self.assrtEqual(response.status_code, 200)
    
    def test_unreachable_url(self):
        response = self.client.get(url_for('not-real'))
        self.assrtEqual(response.status_code, 400)

    

    

