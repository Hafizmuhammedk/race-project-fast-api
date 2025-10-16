from pydantic import BaseModel


class TrackCreate(BaseModel):
    name: str
    length: float
    laps: int


class Team(BaseModel):
    name: str


class Racer(BaseModel):
    name: str
    team: str


class Car(BaseModel):
    model: str


class Winner(BaseModel):
    year: int


class Car_team(BaseModel):
    team: str
    car: str


class Winner_year(BaseModel):
    position: int
    racers: str
    point: int
