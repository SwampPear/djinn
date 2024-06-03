import unittest
from djinn import Database


class TestDatabase(unittest.TestCase):
    """
    Creates a tempoorary database interface.
    """
    def setUp(self):
        self.db_path = 'test_example.db'
        self.db = Database(self.db_path)

    
    """
    Test creating log object.
    """
    def test_create_log_entry(self):
        self.db.create(type='OT', contents='This is a test log entry.')
        results = self.db.read(type='OT')

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1], 'test')
        self.assertEqual(results[0][2], 'This is a test log entry.')