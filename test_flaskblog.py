import unittest
import flaskblog

# Template Render and Route Tests


class TestContainerOnHome(unittest.TestCase):
    def setUp(self):
        self.app = flaskblog.app.test_client()

    def test_container(self):
        rv = self.app.get('/')
        self.assertIn('Home', rv.data.decode())

    def test_about(self):
        rv = self.app.get('/about')
        self.assertIn('About Page', rv.data.decode())
