from pydantic import BaseModel


class TrackCreate(BaseModel):
    name: str
    length: float
    laps: int


class Racer(BaseModel):
    name: str
    team: str


class Team(BaseModel):
    name: str


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
