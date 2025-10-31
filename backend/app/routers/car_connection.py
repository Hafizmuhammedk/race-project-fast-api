# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List
# from app.config.database import get_db
# from app.schema.schemas import Car_teamCreate, Car_teamResponse
# from app.services.car_connecton_mamagement import (
#     Create_Car_team,
#     Get_car_team,
#     Update_Car_team,
#     Delete_car_team
# )

# router = APIRouter(prefix="/car_team", tags=["Car Team Management"])


# @router.post("/", response_model=Car_teamResponse,
#              status_code=status.HTTP_201_CREATED)
# def create_car_team(car_team: Car_teamCreate, db: Session = Depends(get_db)):

#     try:
#         created_team = Create_Car_team(db, car_team)
#         return created_team
#     except ValueError as e:

#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail=str(e))


# @router.get("/", response_model=List[Car_teamResponse])
# def get_car_team(db: Session = Depends(get_db)):
#     try:
#         return Get_car_team(db)
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail=str(e))


# @router.put("/{car_team_id}", response_model=Car_teamResponse)
# def update_car_team(car_team_id: int, car_team: Car_teamCreate,
#                     db: Session = Depends(get_db)):
#     try:
#         updated = Update_Car_team(db, car_team_id, car_team)
#         if not updated:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail="Car_team not found")
#         return updated
#     except ValueError as e:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail=str(e))


# @router.delete("/{car_team_id}", status_code=status.HTTP_200_OK)
# def delete_car_team(car_team_id: int, db: Session = Depends(get_db)):

#     try:
#         deleted = Delete_car_team(db, car_team_id)
#         if not deleted:
#             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                                 detail="Car_team not found")
#         return {"message": "Deleted successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#                             detail=str(e))
