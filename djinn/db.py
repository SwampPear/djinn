import sqlite3
from typing import List


class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)


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
        if type == 'OT':        # standard out
            pass
        elif type == 'IN':      # standard in
            pass
        elif type == 'ER':      # standard error
            pass
        elif type == 'FT':      # file tree
            pass
        elif type == 'FC':      # file contents
            pass
        elif type == 'PI':      # prompt in
            pass
        elif type == 'PO':      # prompt out
            pass
        else:
            raise DatabaseException(f'\'{type}\' is not a valid type specifier')

        sql = '''
        INSERT INTO 
            log (type, contents) 
        VALUES (?, ?)
        '''

        self.query(sql, (type, contents))


    """
    Read functionality for log table.

    Params:
        kwargs - querying parameters
    """
    def read(self, **kwargs: str):  # TODO: change return type
        query = 'AND '.join(f'{key} = ?' for key in kwargs)
        query_pos = ', '.join('?' for i in range(len(kwargs)))

        sql = f'''
        SELECT * FROM log
        WHERE
            {query}
        VALUES {query_pos}
        '''

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