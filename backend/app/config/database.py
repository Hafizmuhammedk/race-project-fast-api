from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import settings
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()


Base = declarative_base()


engine = create_engine(settings.DATABASE_URL)
sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
