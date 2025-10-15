from fastapi import APIRouter, Depends  # responses
from config.database import get_db
from schema.schemas import TrackCreate
from services.create_track import Creat_Track, Get_Track, Update_Track, Delete_Track
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.post("/track", response_model=TrackCreate)
def creat_Track(track: TrackCreate, db: Session = Depends(get_db)):
    return Creat_Track(db, track)


@router.get("/track", response_model=List[TrackCreate])
def get_track(db: Session = Depends(get_db)):
    return Get_Track(db)


@router.put("/track", response_model=TrackCreate)
def update_track(track_id: int, track_update: TrackCreate,
                 db: Session = Depends(get_db)):
    db_track = Update_Track(db, track_id, track_update)
    if not db_track:
        return {"message": "Track not found"}
    return db_track


@router.delete("/track")
def delete_track(track_id: int, db: Session = Depends(get_db)):
    db_track = Delete_Track(db, track_id)
    if not db_track:
        return {"message": "Track not found"}
    return db_track
