from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("db_url")

engine = create_engine(db_url)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
