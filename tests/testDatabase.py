import unittest
from djinn import Database


class TestDatabase(unittest.TestCase):
    """
    Creates a tempoorary database interface.
    """
    def setUp(self):
        self._setupDB()

    """
    Creates a temporary database interface.
    """
    def _setupDB(self):
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
    def test_create_read_log(self):
        self._setupDB()

        id = self.db.create(type='OT', contents='This is a test log entry.')
        result = self.db.read(id=id)

        # new log created
        self.assertEqual(result[0][0], 1)

        # type set
        self.assertEqual(result[0][1], 'OT')

        # contents set
        self.assertEqual(result[0][2], 'This is a test log entry.')


    """
    Test updating log.
    """
    def test_update_log(self):
        self._setupDB()

        # TODO: implement this

        pass


    """
    Test deleting log.
    """
    def test_delete_log(self):
        self._setupDB()

        id = self.db.create(type='OT', contents='something')
        
        self.db.delete(id)

        results = self.db.read(type='OT', contents='somthing')

        self.assertEqual(len(results), 0)
        