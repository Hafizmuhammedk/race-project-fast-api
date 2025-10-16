from fastapi import APIRouter, Depends   # HTTPException  # responses
from fastapi.responses import JSONResponse
from config.database import get_db
from schema.schemas import Car
from sqlalchemy.orm import Session
from typing import List
from services.car_management import (
    Create_Car,
    Get_car,
    Get_Car_by,
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


@router.get("/car", response_model=List[Car])
def get_car(db: Session = Depends(get_db)):
    try:
        return Get_car(db)
    except Exception as e:
        return JSONResponse(
            {"error": f"not found:{str(e)}"},
            status_code=404
        )


@router.get("/car/{car_id}", response_model=Car)
def car_by_id(car_id: int, db: Session = Depends(get_db)):
    try:
        return Get_Car_by(db, car_id)
    except Exception as e:
        return JSONResponse(
            {"error": f"not found:{str(e)}"},
            status_code=404
        )
