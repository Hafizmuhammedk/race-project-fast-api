from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Car_team(Base):
    __tablename__ = "car_team"
    team_id = Column(Integer, ForeignKey("team.id"))
    car_id = Column(Integer, ForeignKey("car.id"))

    car = relationship("Car", back_populates="car_team")
    team = relationship("Team", back_populates="car_taem")
