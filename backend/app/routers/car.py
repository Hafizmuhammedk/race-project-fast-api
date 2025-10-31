from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.schema.schemas import Car
from app.services.car_management import (
    Create_Car,
    Get_car,
    Get_Car_by,
    Update_Car,
    Delete_car
)

router = APIRouter(prefix="/car", tags=["Car Management"])


@router.post("/car", response_model=Car)
def create_car(team_name: str = None, car: Car = None,
               db: Session = Depends(get_db)):

    try:
        created_car = Create_Car(team_name, db, car)
        return created_car
    except ValueError as e:
        return JSONResponse(
            {"error": str(e)},
            status_code=400
        )
    except Exception as e:
        return JSONResponse(
            {"error": f"Unexpected error: {str(e)}"},
            status_code=500
        )


@router.get("/car", response_model=List[Car])
def get_car(db: Session = Depends(get_db)):
    try:
        return Get_car(db)
    except Exception as e:
        return JSONResponse(
            {"error": f"not found: {str(e)}"},
            status_code=404
        )


@router.get("/car/{car_id}", response_model=Car)
def car_by_id(car_id: int, db: Session = Depends(get_db)):
    try:
        return Get_Car_by(db, car_id)
    except Exception as e:
        return JSONResponse(
            {"error": f"not found: {str(e)}"},
            status_code=404
        )


@router.put("/car", response_model=Car)
def update_car(car_id: int, car_update: Car, db: Session = Depends(get_db)):
    try:
        db_car = Update_Car(db, car_id, car_update)
        if not db_car:
            return JSONResponse({"message": "car not updated"},
                                status_code=404)
        return JSONResponse({"message": "updated Successfully"},
                            status_code=200)
    except Exception as e:
        return JSONResponse(
            {"error": f"not updated: {str(e)}"},
            status_code=400
        )


@router.delete("/car")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    try:
        db_car = Delete_car(db, car_id)
        if not db_car:
            return JSONResponse({"message": "car not found"},
                                status_code=404)
        return JSONResponse({"message": "deleted Successfully"},
                            status_code=200)
    except Exception as e:
        return JSONResponse(
            {"error": f"Error in deleting: {str(e)}"},
            status_code=400
        )
