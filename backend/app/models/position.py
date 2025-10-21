from sqlalchemy import Column, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Position(Base):
    __tablename__ = "position"
    year = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, index=False)

    position_year = relationship("Position_year", back_populates="position")


class Position_year(Base):
    __tablename__ = "position_year"
    id = Column(Integer, primary_key=True, index=False)
    position_id = Column(Integer, ForeignKey("position.id"))
    rank = Column(Integer, nullable=False)
    racers_id = Column(Integer, ForeignKey("racers.id"))
    point = Column(Integer, nullable=False)

    position = relationship("Position", back_populates="position_year")
    racers = relationship("Racers", back_populates="position_year")
