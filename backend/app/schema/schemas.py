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
    team_name: str
    car: str


# class CarTeamBase(BaseModel):
#     team_name: str
#     car_model: str


# class CarTeamCreate(CarTeamBase):
#     pass


# class CarTeamResponse(CarTeamBase):
#     id: int

#     class Config:
#         orm_mode = True


class Winner_year(BaseModel):
    position: int
    racers: str
    point: int
