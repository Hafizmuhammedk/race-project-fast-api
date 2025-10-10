from sqlalchemy import Column, Integer, String, Float, ForeignKey
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
    name = Column(String(length=15), nullable=False)

    car_team = relationship("car_team", back_populates="Team")
    team = relationship("racers", back_populates="Team")


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)

    car_team = relationship("car_team", back_populates="Car")


class Winner(Base):
    __tablename__ = "winner"
    year = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, index=False)

    winner_year = relationship("Winner_year", back_populates="winner")


class Racers(Base):
    __tablename__ = "racers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    team = Column(Integer, ForeignKey("team.id"))

    winner_year = relationship("winner_year", back_populates="Racers")
    team = relationship("Team", back_populates="racers")


class Car_team(Base):
    __tablename__ = "car_team"
    team_id = Column(Integer, ForeignKey("team.id"))
    car_id = Column(Integer, ForeignKey("car.id"))

    car = relationship("Car", back_populates="car_team")
    team = relationship("Team", back_populates="car_taem")


class Winner_year(Base):
    __tablename__ = "winner_year"
    winner_id = Column(Integer, ForeignKey("winner.id"))
    position = Column(Integer, nullable=False)
    racer_id = Column(Integer, ForeignKey("racers.id"))
    point = Column(Integer, nullable=False)

    winner = relationship("Winner", back_populates="winner_year")
    racer = relationship("Racers", back_populates="winner_year")
