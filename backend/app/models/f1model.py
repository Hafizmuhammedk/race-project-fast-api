from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

Base = declarative_base()


class Track(Base):
    __tablename__ = "track"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    length = Column(Float, nullable=False)
    laps = Column(int, nullable=False)


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)


class 
