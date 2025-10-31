from pydantic import BaseModel


class TrackCreate(BaseModel):
    name: str
    length: float
    laps: int


class Team(BaseModel):
    name: str


class RacerBase(BaseModel):
    name: str
    team_id: int


class RacerCreate(RacerBase):
    pass


class RacerResponse(RacerBase):
    id: int

    class Config:
        from_attributes = True


class Car(BaseModel):
    model: str


class Winner(BaseModel):
    year: int


class Car_teamCreate(BaseModel):
    team_name: str
    car_model: str

    class Config:
        from_attributes = True


class Car_teamBase(BaseModel):
    team_name: str
    car_model: str


class Car_teamResponse(Car_teamBase):
    id: int

    class Config:
        from_attributes = True


class Winner_year(BaseModel):
    position: int
    racers: str
    point: int
