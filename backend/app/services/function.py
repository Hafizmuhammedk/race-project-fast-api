from sqlalchemy.orm import Session
from app.schema import schema
from app.models import (
    car,
    connection_car_team,
    connection_position_year,
    Racers,
    position,
    team,
    track
)


def creat_track(db: Session = Depends(get_db), track: schema.Track):
    db_track = track()