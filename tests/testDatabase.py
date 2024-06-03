import unittest
from djinn import Database


class TestDatabase(unittest.TestCase):
    """
    Creates a tempoorary database interface.
    """
    def setUp(self):
        self.db = Database('test.db')

        sql = 'DROP TABLE IF EXISTS log'

        self.db.query(sql)

        sql = """
        CREATE TABLE IF NOT EXISTS log (
            id INTEGER PRIMARY KEY NOT NULL,
            type TEXT NOT NULL,
            contents TEXT NOT NULL
        );
        """

        self.db.query(sql)

    
    """
    Test creating log.
    """
    def test_create_log_entry(self):
        self.db.create(type='OT', contents='This is a test log entry.')
        results = self.db.read(type='OT')

        # new log created
        self.assertEqual(len(results), 1)

        # type set
        self.assertEqual(results[0][1], 'OT')

        # contents set
        self.assertEqual(results[0][2], 'This is a test log entry.')