import unittest
from datetime import datetime

from app import app, db, Todo


class TodoAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_update_page_formats_created_date_as_dd_mm_yyyy(self):
        with app.app_context():
            todo = Todo(title="Sample", desc="Details", date_created=datetime(2024, 1, 2, 3, 4, 5))
            db.session.add(todo)
            db.session.commit()

        response = self.client.get('/update/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'02-01-2024', response.data)
        self.assertNotIn(b'2024-01-02', response.data)

    def test_search_only_matches_titles(self):
        with app.app_context():
            todo = Todo(title='Alpha Task', desc='keyword in description')
            db.session.add(todo)
            db.session.commit()

        response = self.client.get('/search?search=keyword')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Alpha Task', response.data)
        self.assertIn(b'Search tasks by title only.', response.data)


if __name__ == '__main__':
    unittest.main()
