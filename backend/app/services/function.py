from sqlalchemy.orm import Session
# from schema import schemas
from models.track import Track


def creat_track(db: Session, track_data):
    db_track = Track(name=track_data.name, length=track_data.length,
                     laps=track_data.laps)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track
