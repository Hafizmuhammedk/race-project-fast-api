from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Position(Base):
    __tablename__ = "position"
    year = Column(Integer, nullable=False)
    id = Column(Integer, primary_key=True, index=False)

    position_year = relationship("Position_year", back_populates="positi")
