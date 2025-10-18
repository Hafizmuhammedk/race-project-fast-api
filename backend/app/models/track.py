from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base


class Track(Base):
    __tablename__ = "track"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=15), nullable=False)
    length = Column(Float, nullable=False)
    laps = Column(Integer, nullable=False)
