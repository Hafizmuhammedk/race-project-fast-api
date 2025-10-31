from sqlalchemy import Column, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship


class Winner(Base):
    __tablename__ = "winner"

    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, unique=True)

    results = relationship("WinnerResult", back_populates="winner",
                           cascade="all, delete-orphan")


class WinnerResult(Base):
    __tablename__ = "winner_result"

    id = Column(Integer, primary_key=True, index=True)
    winner_id = Column(Integer, ForeignKey("winner.id"), nullable=False)
    position = Column(Integer, nullable=False)
    racer_id = Column(Integer, ForeignKey("racer.id"), nullable=False)
    points = Column(Integer, nullable=False)

    winner = relationship("Winner", back_populates="results")
    racer = relationship("Racer", back_populates="winner_results")
