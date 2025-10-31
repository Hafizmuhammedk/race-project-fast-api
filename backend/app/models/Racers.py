# app/models/racer.py
from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Racer(Base):
    __tablename__ = "racer"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    team_id = Column(Integer, ForeignKey("team.id"))

    # must match Position_year.back_populates="racers"
    position_years = relationship("PositionYear", back_populates="racers",
                                  cascade="all, delete-orphan")
    team = relationship("Team", back_populates="racers")
