from sqlalchemy import create_engine, Column, Integer, String, Sequence, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Executions(Base):
    __tablename__ = "executions"
    
    id = Column(Integer, Sequence("id"), primary_key=True)
    description = Column(String(50))
    type = Column(CHAR)


def load_data_into_db(db_url, data):
    """
    Loads data into a database using SQLAlchemy.

    Args:
        db_url (str): The database URL.
        data (list of tuples): The data to be inserted into the database.
    """
    # Create an engine and a session
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Insert data into the table
    for item in data:
        record = MyTable(column1=item[0], column2=item[1])
        session.add(record)

    # Commit the changes and close the session
    session.commit()
    session.close()

