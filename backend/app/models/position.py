# app/models/position.py
from sqlalchemy import Column, Integer, ForeignKey, String
from app.config.database import Base
from sqlalchemy.orm import relationship


class Position(Base):
    __tablename__ = "position"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)

    position_years = relationship("PositionYear", back_populates="position",
                                  cascade="all, delete-orphan")


class PositionYear(Base):
    __tablename__ = "position_year"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    racers_id = Column(Integer, ForeignKey("racer.id"))
    point = Column(Integer)
    position_id = Column(Integer, ForeignKey("position.id"))

    position = relationship("Position", back_populates="position_years")
    racers = relationship("Racer", back_populates="position_years")
