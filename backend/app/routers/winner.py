from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schema.schemas import (
    WinnerCreate,
    WinnerResponse,
    WinnerResultCreate,
    WinnerResultResponse,
)
from app.services import winner_service as service

router = APIRouter(prefix="/winners", tags=["Winners"])


@router.post("/", response_model=WinnerResponse)
def create_winner(payload: WinnerCreate, db: Session = Depends(get_db)):
    return service.create_winner(db, payload)


@router.get("/", response_model=list[WinnerResponse])
def get_winners(db: Session = Depends(get_db)):
    return service.get_winners(db)


@router.post("/results", response_model=WinnerResultResponse)
def create_winner_result(payload: WinnerResultCreate, db: Session = Depends(get_db)):
    return service.create_winner_result(db, payload)


@router.get("/{winner_id}/results", response_model=list[WinnerResultResponse])
def get_winner_results(winner_id: int, db: Session = Depends(get_db)):
    return service.get_winner_results(db, winner_id)
