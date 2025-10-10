from pydantic import BaseModel


class Track(BaseModel):
    id: int
    name: str
    lenght: float
    laps: int


class Racer(BaseModel):
    id: int
    name: str
    team: str


class Team(BaseModel):
    id: int
    name: str

