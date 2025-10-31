from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.schema.schemas import RacerCreate, RacerResponse
from app.services.racer_management import (
    Create_Racer,
    Get_Racers,
    Get_Racer_By_ID,
    Update_Racer,
    Delete_Racer
)

router = APIRouter(prefix="/racer", tags=["Racer Management"])


@router.post("/", response_model=RacerResponse,
             status_code=status.HTTP_201_CREATED)
def create_racer(racer: RacerCreate, db: Session = Depends(get_db)):
    try:
        return Create_Racer(db, racer)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/", response_model=List[RacerResponse])
def get_racers(db: Session = Depends(get_db)):
    return Get_Racers(db)


@router.get("/{racer_id}", response_model=RacerResponse)
def get_racer_by_id(racer_id: int, db: Session = Depends(get_db)):
    db_racer = Get_Racer_By_ID(db, racer_id)
    if not db_racer:
        raise HTTPException(status_code=404, detail="Racer not found")
    return db_racer


@router.put("/{racer_id}", response_model=RacerResponse)
def update_racer(racer_id: int, racer_update: RacerCreate,
                 db: Session = Depends(get_db)):
    db_racer = Update_Racer(db, racer_id, racer_update)
    if not db_racer:
        raise HTTPException(status_code=404, detail="Racer not found")
    return db_racer


@router.delete("/{racer_id}")
def delete_racer(racer_id: int, db: Session = Depends(get_db)):
    deleted = Delete_Racer(db, racer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Racer not found")
    return {"message": "Racer deleted successfully"}
