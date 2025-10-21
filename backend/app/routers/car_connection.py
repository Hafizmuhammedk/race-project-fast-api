# from fastapi import APIRouter, Depends   # HTTPException  # responses
# from fastapi.responses import JSONResponse
# from app.config.database import get_db
# from app.schema.schemas import Car_team, CarTeamCreate, CarTeamResponse
# from sqlalchemy.orm import Session
# from typing import List
# from app.services.car_connecton_mamagement import (
#     Get_car_team,
#     Update_Car_team,
#     Delete_car_team,
#     Create_Car_team
# )

# router = APIRouter()


# @router.post("/car_team", response_model=CarTeamResponse)
# def create_car_team(car_team: CarTeamCreate, db: Session = Depends(get_db)):
#     try:
#         return Create_Car_team(db, car_team)
#     except Exception as e:
#         return JSONResponse(
#             {"error": f"error in creating:{str(e)}"},
#             status_code=404
#             )


# @router.get("/car_team", response_model=List[Car_team])
# def get_car_team(db: Session = Depends(get_db)):
#     try:
#         return Get_car_team(db)
#     except Exception as e:
#         return JSONResponse(
#             {"error": f"not found:{str(e)}"},
#             status_code=404
#         )


# @router.put("/car_team", response_model=Car_team)
# def update_car_team(car_team_id: int, car_team_update: Car_team,
#                     db: Session = Depends(get_db)):
#     try:
#         db_car_team = Update_Car_team(db, car_team_id, car_team_update)
#         if not db_car_team:
#             return {"message": "car_team not updated"}
#         return JSONResponse({"message": "updated Successfully"},
#                             status_code=200)
#     except Exception as e:
#         return JSONResponse(
#             {"error": f"not updated:{str(e)}"},
#             status_code=404
#         )


# @router.delete("/car_team")
# def delete_car_team(car_team_id: int, db: Session = Depends(get_db)):
#     try:
#         db_car_team = Delete_car_team(db, car_team_id)
#         if not db_car_team:
#             return {"message": "car_team not found"}
#         return JSONResponse({"message": "deleted Successfully"},
#                             status_code=200)
#     except Exception as e:
#         return JSONResponse(detail={"error": f"Error in deleting:{str(e)}"},
#                             status_code=404)
