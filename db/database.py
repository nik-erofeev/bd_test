from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import SQLALCHEMY_DATABASE

DATABASE_URL = SQLALCHEMY_DATABASE


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


Base.metadata.create_all(engine)


# def get_db():
#     with session() as db:
#         yield db


def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
