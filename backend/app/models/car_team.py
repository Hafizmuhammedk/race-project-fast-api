from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)

    car_team = relationship("Car_team", back_populates="car")


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)

    car_team = relationship("Car_team", back_populates="team")
    racers = relationship("Racers", back_populates="team")


class Car_team(Base):
    __tablename__ = "car_team"
    id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, ForeignKey("team.name"))
    car_model = Column(String, ForeignKey("car.model"))

    car = relationship("Car", back_populates="car_team")
    team = relationship("Team", back_populates="car_team")
