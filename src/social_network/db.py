import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(
    engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
