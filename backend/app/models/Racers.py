from sqlalchemy import Column, Integer, String, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Racers(Base):
    __tablename__ = "racers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)
    team_name = Column(Integer, ForeignKey("team.name"))

    position_year = relationship("Position_year", back_populates="racers")
    team = relationship("Team", back_populates="racers")
