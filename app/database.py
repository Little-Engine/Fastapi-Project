import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set!")

if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgres://", "postgresql://", 1)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='sammy2005', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(5)
