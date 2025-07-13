import unittest
from app import create_app
from app.db import db
from app.models import Student

class StudentTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def test_add_student(self):
        res = self.client.post('/api/v1/students', json={
            'name': 'John Doe',
            'age': 21,
            'grade': 'A'
        })
        self.assertEqual(res.status_code, 201)

    def test_healthcheck(self):
        res = self.client.get('/healthcheck')
        self.assertEqual(res.status_code, 200)