from unittest.mock import patch
from flask import url_for, Response, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_random_destination(self):
        destinations = [b'Brazil', b'Mexico', b'Bahamas', b'San Francisco', b'Miami', b'Madrid', b'Pekin', b'Dubai', b'Paris', b'Rome']
        response = self.client.get(url_for("hello_internet"))
        self.assertIn(response.data, destinations)
