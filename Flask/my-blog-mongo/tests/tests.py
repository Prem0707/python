import unittest
from app import app
from app.models import demo
import logging

class TodoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # def tearDown(self):
    #      pass

    def test_index(self):
        rv = self.app.get('/')
        logging.info(rv)
        # assert "awesome-flask-todo" in rv.data.encode('utf-8')

    # def test_add_todo(self):
    #     self.app.post('/add', data=dict(content="test add todo"))
    #     todo = demo.objects.get_or_404(content="test add todo")
    #     assert todo is not None

    def test_404(self):
        rv = self.app.get('/404test')
        logging.info(rv.data)
        assert "Not Found" in rv.data
