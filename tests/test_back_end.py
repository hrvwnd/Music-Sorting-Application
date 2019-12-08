import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Tracks, Artists, Genres

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

        remake_db()

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
    


    

    

