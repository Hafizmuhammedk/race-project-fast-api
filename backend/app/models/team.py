from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)

    car_team = relationship("car_team", back_populates="Team")
    team = relationship("racers", back_populates="Team")
