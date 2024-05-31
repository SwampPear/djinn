class Database:
    """
    Database interface.
    """
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path