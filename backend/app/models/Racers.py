from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship


class Racers(Base):
    __tablename__ = "racers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)
    team = Column(Integer, ForeignKey("team.id"))

    position_year = relationship("position_year", back_populates="Racers")
    team = relationship("Team", back_populates="racers")
