from fastapi import APIRouter, Depends   # HTTPException  # responses
from fastapi.responses import JSONResponse
from app.config.database import get_db
from app.schema.schemas import Car
from sqlalchemy.orm import Session
from typing import List
from app.services.car_management import (
    Create_Car,
    Get_car,
    Get_Car_by,
    Update_Car,
    Delete_car
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


@router.put("/car", response_model=Car)
def update_car(car_id: int, car_update: Car,
               db: Session = Depends(get_db)):
    try:
        db_car = Update_Car(db, car_id, car_update)
        if not db_car:
            return {"message": "car not updated"}
        return JSONResponse({"message": "updated Successfully"},
                            status_code=200)
    except Exception as e:
        return JSONResponse(
            {"error": f"not updated:{str(e)}"},
            status_code=404
        )


@router.delete("/car")
def delete_car(car_id: int, db: Session = Depends(get_db)):
    try:
        db_car = Delete_car(db, car_id)
        if not db_car:
            return {"message": "car not found"}
        return JSONResponse({"message": "deleted Successfully"},
                            status_code=200)
    except Exception as e:
        return JSONResponse(detail={"error": f"Error in deleting:{str(e)}"},
                            status_code=404)
