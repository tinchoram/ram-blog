from flask_testing import TestCase
from flask import current_app, url_for
from blog import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    # TEST BASE
    # APP EXIST
    def test_app_exists(self):
        """ param app
        """
        self.assertIsNotNone(current_app)

    # TEST MODE
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # TEST INDEX
    def test_index_get(self):
        response = self.client.get(url_for('index'))

        self.assert200(response)
