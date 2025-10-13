from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Car(Base):
    __tablename__ = "car"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)

    car_team = relationship("car_team", back_populates="Car")
