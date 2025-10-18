from sqlalchemy.orm import Session
from app.schema import schemas
from app.models.car_team import Car_team


def Create_Car_team(db: Session, car_team_data):
    try:
        db_car_team = Car_team(model=car_team_data.car.model,
                               name=car_team_data.team.name)
        db.add(db_car_team)
        db.commit()
        db.refresh(db_car_team)
        return db_car_team
    except Exception as e:
        print(f"creation faild: {str(e)}")
        raise e


def Get_car_team(db: Session):
    try:
        return db.query(Car_team).all()
    except Exception as e:
        print(f" not founded: {str(e)}")
        raise e


def Update_Car_team(db: Session, car_team_id: int,
                    car_team_update: schemas.Car_team):
    try:
        car_team = (
            db.query(Car_team)
            .filter(Car_team.car_team == car_team_id)
            .first()
        )
        if not car_team:
            print(" not updated")

        car_team.team = car_team_update.team
        car_team.car = car_team_update.car

        db.commit()
        db.refresh(car_team)
        return car_team

    except Exception as e:
        print(f" not updated: {str(e)}")
        raise e


def Delete_car_team(db: Session, car_team_id: int):
    try:
        db.query(Car_team).filter(Car_team.id == car_team_id).delete()
        db.commit()
    except Exception as e:
        print(f'Error in Delete Team : {str(e)}')
        raise e
