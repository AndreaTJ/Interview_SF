from unittest.mock import patch
from flask import url_for, request, jsonify
from flask_testing import TestCase


from app import app, Duo, db

class TestBase (TestCase):
    def create_app (self): 
        
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
        TESTING = True)

        return app
    
    def setUp (self): 
        db.create_all()
 
    def tearDown (self):
        db.drop_all()
    

class TestResponse(TestBase):

    def test_req(self):
        with patch('requests.get') as g:
            country = "Paris"
            money2 = "15"
            result_2 = country, money2
            g.return_value.json.return_value = result_2

            response = self.client.get(url_for('hello_internet'))
            self.assertIn(b"Paris", response.data)
            self.assertIn(b"15", response.data)







        
        

