import sqlite3


class Database:
    """
    Database interface.
    """
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path

        self.conn = sqlite3.connect(self.db_path)


    """
    Querys the database.
    """
    def query(self, sql: str) -> None:
        cursor = self.conn.cursor()
        cursor.execute(sql)

        self.conn.commit()