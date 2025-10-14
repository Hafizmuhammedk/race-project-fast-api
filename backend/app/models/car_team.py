from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)

    car_team = relationship("car_team", back_populates="Car")


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)

    car_team = relationship("car_team", back_populates="Team")
    team = relationship("racers", back_populates="Team")


class Car_team(Base):
    __tablename__ = "car_team"
    team_id = Column(Integer, ForeignKey("team.id"), primary_key=True)
    car_id = Column(Integer, ForeignKey("car.id"), primary_key=True)

    car = relationship("Car", back_populates="car_team")
    team = relationship("Team", back_populates="car_taem")
