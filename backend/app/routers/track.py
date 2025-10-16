from fastapi import APIRouter, Depends, HTTPException  # responses
from fastapi.responses import JSONResponse
from config.database import get_db
from schema.schemas import TrackCreate
from sqlalchemy.orm import Session
from typing import List
from services.track_management import (
    Creat_Track,
    Get_Track,
    Update_Track,
    Delete_Track,
    Get_Track_by
    )


router = APIRouter()


@router.post("/track", response_model=TrackCreate)
def creat_Track(track: TrackCreate, db: Session = Depends(get_db)):
    return Creat_Track(db, track)


@router.get("/track", response_model=List[TrackCreate])
def get_track(db: Session = Depends(get_db)):
    return Get_Track(db)


@router.get("/track/{track_id}", response_model=TrackCreate)
def track_by_id(rack_id: int, db: Session = Depends(get_db)):
    return Get_Track_by(db, rack_id)


@router.put("/track", response_model=TrackCreate)
def update_track(track_id: int, track_update: TrackCreate,
                 db: Session = Depends(get_db)):
    db_track = Update_Track(db, track_id, track_update)
    if not db_track:
        return {"message": "Track not found"}
    return db_track


@router.delete("/track")
def delete_track(track_id: int, db: Session = Depends(get_db)):
    try:
        db_team = Delete_Track(db, track_id)
        if not db_team:
            return {"message": "track not found"}
        return JSONResponse({"message": "deleted Successfully"},
                            status_code=200)
    except Exception as e:
        return HTTPException(status_code=404,
                             detail={"error": f"Error in deleting :{str(e)}"})
