from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, unique=True, nullable=False)

    car_teams = relationship("CarTeam", back_populates="car",
                             cascade="all, delete-orphan")


class Team(Base):
    __tablename__ = "team"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), unique=True, nullable=False)

    racers = relationship("Racer", back_populates="team",
                          cascade="all, delete-orphan")
    car_teams = relationship("CarTeam", back_populates="team",
                             cascade="all, delete-orphan")


class CarTeam(Base):
    __tablename__ = "car_team"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("team.id"), nullable=False)
    car_id = Column(Integer, ForeignKey("car.id"), nullable=False)

    team = relationship("Team", back_populates="car_teams")
    car = relationship("Car", back_populates="car_teams")
