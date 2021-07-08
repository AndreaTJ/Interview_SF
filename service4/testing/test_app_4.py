from unittest.mock import patch
from flask import url_for, request
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class Test_Response(TestBase):
    def test_request(self):
        with patch("requests.get") as g:
            g.return_value.text = "5000"

            response = self.client.get(url_for("hello_internet"))
            self.assertIn(b'5000', response.data)

class Test_Response_2(TestBase):
    def test_request_2(self):
        with patch("requests.get") as g:
            g.return_value.text = "1"

            response = self.client.get(url_for("hello_internet"))
            self.assertIn(b'1.04', response.data)