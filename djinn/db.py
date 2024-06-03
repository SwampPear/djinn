import sqlite3
from typing import List


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
    def query(self, sql: str, params: List[str]) -> None:
        cursor = self.conn.cursor()
        cursor.execute(sql, params)

        self.conn.commit()

    
    """
    Create functionality for log table.

    Params:
        type - type specifier
        contents - log contents
    """
    def create(self, type: str, contents: str=None) -> None:
        sql = "INSERT INTO log (type, contents) VALUES (?, ?)"
        self.query(sql, (type, contents))


    """
    Read functionality for log table.

    Params:
        kwargs - querying parameters
    """
    def read(self, **kwargs: str):  # TODO: change return type
        sql = "SELECT * FROM log WHERE " + " AND ".join(f"{key} = ?" for key in kwargs)
        params = tuple(kwargs.values())
        cursor = self.conn.cursor()
        cursor.execute(sql, params)

        return cursor.fetchall()


    """
    Update functionality for log table.

    Params:
        id - id of object to update
        kwargs - updating parameters
    """
    def update(self, id: str, **kwargs: str) -> None:
        sql = "UPDATE log SET " + ", ".join(f"{key} = ?" for key in kwargs) + " WHERE id = ?"
        params = tuple(kwargs.values()) + (id,)
        self.query(sql, params)


    """
    Delete functionality for log table.

    Params:
        id - id of object to be deleted
    """
    def delete(self, id: str) -> None:
        sql = "DELETE FROM log WHERE id = ?"
        self.query(sql, (id,))

    def __del__(self):
        self.conn.close()