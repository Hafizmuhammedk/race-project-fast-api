from pydantic import BaseModel


class TrackCreate(BaseModel):
    name: str
    length: float
    laps: int


class Racer(BaseModel):
    id: int
    name: str
    team: str


class Team(BaseModel):
    id: int
    name: str


class Car(BaseModel):
    id: int
    model: str


class Winner(BaseModel):
    year: int
    id: int


class Car_team(BaseModel):
    team: str
    car: str


class Winner_year(BaseModel):
    id: int
    position: int
    racers: str
    point: int
