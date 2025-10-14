from fastapi import APIRouter, Depends  # responses
from config.database import get_db
from schema.schemas import TrackCreate
from services.function import creat_track
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/track", response_model=TrackCreate)
def creat_Track(track: TrackCreate, db: Session = Depends(get_db)):
    return creat_track(db, track)
