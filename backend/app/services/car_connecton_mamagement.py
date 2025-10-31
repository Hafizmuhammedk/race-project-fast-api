# from sqlalchemy.orm import Session
# from app.models.car_team import CarTeam
# from app.models import Team
# from app.models import Car
# from app.schema.schemas import Car_teamCreate


# def Create_Car_team(db: Session, car_team: Car_teamCreate):
#     try:
#         team = db.query(Team).filter(Team.name == car_team.team_name).first()
#         if not team:
#             raise ValueError(f"Team '{car_team.team_name}' does not exist")

#         car = db.query(Car).filter(Car.model == car_team.car_model).first()
#         if not car:
#             raise ValueError(
#                 f"Car model '{car_team.car_model}' does not exist")

#         db_car_team = CarTeam(
#             team_name=car_team.team_name,
#             car_model=car_team.car_model
#         )
#         db.add(db_car_team)
#         db.commit()
#         db.refresh(db_car_team)
#         return db_car_team

#     except Exception as e:
#         db.rollback()
#         print(f"Creation failed: {str(e)}")
#         raise e


# def Get_car_team(db: Session):
#     try:
#         return db.query(CarTeam).all()
#     except Exception as e:
#         print(f"Retrieval failed: {str(e)}")
#         raise e


# def Update_Car_team(db: Session, car_team_id: int,
#                     car_team_update: Car_teamCreate):
#     try:
#         db_car_team = db.query(CarTeam).filter(
#             CarTeam.id == car_team_id).first()
#         if not db_car_team:
#             return None

#         team = db.query(Team).filter(
#             Team.name == car_team_update.team_name).first()
#         if not team:
#             raise ValueError(f"Team '{car_team_update.team_name}' does exist")

#         car = db.query(Car).filter(
#             Car.model == car_team_update.car_model).first()
#         if not car:
#             raise ValueError(
#                 f"Car model '{car_team_update.car_model}'not exist")

#         db_car_team.team_name = car_team_update.team_name
#         db_car_team.car_model = car_team_update.car_model

#         db.commit()
#         db.refresh(db_car_team)
#         return db_car_team

#     except Exception as e:
#         db.rollback()
#         print(f"Update failed: {str(e)}")
#         raise e


# def Delete_car_team(db: Session, car_team_id: int):
#     try:
#         db_car_team = db.query(CarTeam).filter(
#             CarTeam.id == car_team_id).first()
#         if not db_car_team:
#             return None

#         db.delete(db_car_team)
#         db.commit()
#         return True

#     except Exception as e:
#         db.rollback()
#         print(f"Delete failed: {str(e)}")
#         raise e
