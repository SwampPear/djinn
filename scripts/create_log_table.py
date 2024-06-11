import os
import sys


sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


from djinn import Database


def create_log_table() -> None:
    db = Database('data.db')

    sql = 'DROP TABLE IF EXISTS log'

    db.query(sql)

    sql = """
    CREATE TABLE IF NOT EXISTS log (
        id INTEGER PRIMARY KEY NOT NULL,
        type TEXT NOT NULL,
        contents TEXT NOT NULL
    );
    """

    db.query(sql)


if __name__ == '__main__':
    create_log_table()