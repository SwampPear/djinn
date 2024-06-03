from djinn.db import Database


def create_log_table() -> None:
    db = Database('data.db')

    sql = """
    CREATE TABLE IF NOT EXISTS log (
        id INTEGER PRIMARY KEY AUTOINC NOT NULL,
        type TEXT NOT NULL,
        type TEXT NOT NULL
    );
    """

    db.query(sql)
    

if __name__ == '__main__':
    create_log_table()