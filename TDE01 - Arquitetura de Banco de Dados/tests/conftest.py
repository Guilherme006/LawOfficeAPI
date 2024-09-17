import sys
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Base, engine

@pytest.fixture(scope="session")
def db_engine():
    return engine

@pytest.fixture(scope="session")
def db_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
