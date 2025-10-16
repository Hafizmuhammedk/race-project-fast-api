from fastapi import APIRouter, Depends   # HTTPException  # responses
from fastapi.responses import JSONResponse
from config.database import get_db
from schema.schemas import Car
from sqlalchemy.orm import Session
from typing import List
from services.car_management import (
    Create_Car
)

router = APIRouter()


@router.post("/car", response_model=Car)
def create_car(car: Car, db: Session = Depends(get_db)):
    try:
        return Create_Car(db, car)
    except Exception as e:
        return JSONResponse(
            {"error": f"error in creating:{str(e)}"},
            status_code=404
            )
