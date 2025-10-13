from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Position_year(Base):
    __tablename__ = "position_year"
    winner_id = Column(Integer, ForeignKey("position.id"))
    position = Column(Integer, nullable=False)
    racers_id = Column(Integer, ForeignKey("racers.id"))
    point = Column(Integer, nullable=False)

    position_year = relationship("Position", back_populates="position_year")
    racer = relationship("Racers", back_populates="position_year")
