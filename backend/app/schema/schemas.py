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


class WinnerBase(BaseModel):
    year: int


class WinnerCreate(WinnerBase):
    pass


class WinnerResponse(WinnerBase):
    id: int

    class Config:
        from_attributes = True


class WinnerResultBase(BaseModel):
    winner_id: int
    position: int
    racer_id: int
    points: int


class WinnerResultCreate(WinnerResultBase):
    pass


class WinnerResultResponse(WinnerResultBase):
    id: int

    class Config:
        from_attributes = True
