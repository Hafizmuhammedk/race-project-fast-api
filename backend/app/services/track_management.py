from sqlalchemy.orm import Session
from schema import schemas
from models.track import Track


def Creat_Track(db: Session, track_data):
    db_track = Track(name=track_data.name, length=track_data.length,
                     laps=track_data.laps)
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track


def Get_Track(db: Session):
    return db.query(Track).all()


def Get_Track_by(db: Session, track_id: int):
    db_track_id = db.query(Track).filter(Track.id == track_id).first()
    if not db_track_id:
        return None
    return db_track_id


def Update_Track(db: Session, track_id: int,
                 track_update: schemas.TrackCreate):
    db_track = db.query(Track).filter(Track.id == track_id).first()
    if db_track:
        db_track.name = track_update.name
        db_track.length = track_update.length
        db_track.laps = track_update.laps
        db.commit()
        db.refresh(db_track)
    return db_track


def Delete_Track(db: Session, track_id: int):
    db_track = db.query(Track).filter(Track.id == track_id).first()
    if db_track:
        db.delete(db_track)
        db.commit()
    return db_track
