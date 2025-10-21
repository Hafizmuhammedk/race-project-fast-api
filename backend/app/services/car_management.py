from sqlalchemy.orm import Session
from app.schema import schemas
from app.models.car_team import Car, Car_team, Team


def Create_Car(team_id: str, db: Session, car: schemas.Car):
    db_team = db.query(Team).filter(Team.name == team_id).first()
    try:
        db_car = Car(model=car.model)
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
        db_car_team = Car_team(car_model=db_car.model, team_name=db_team.name)
        db.add(db_car_team)
        db.commit()
        db.refresh(db_car_team)
        return db_car
    except Exception as e:
        print(f"creation faild: {str(e)}")
        raise e


def Get_car(db: Session):
    try:
        db_car = db.query(Car).all()
        return db_car
    except Exception as e:
        print(f" not founded: {str(e)}")
        raise e


def Get_Car_by(db: Session, car_id: int):
    try:
        db_car_id = db.query(Car).filter(Car.id == car_id).first()
        if not db_car_id:
            return None
        return db_car_id
    except Exception as e:
        print(f"notfounded: {str(e)}")
        raise e


def Update_Car(db: Session, car_id: int,
               car_update: schemas.Car):
    try:
        db_car = db.query(Car).filter(Car.id == car_id).first()
        if db_car:
            db_car.model = car_update.model
            db.commit()
            db.refresh(db_car)
        return db_car
    except Exception as e:
        print(f"car not updated: {str(e)}")
        raise e


def Delete_car(db: Session, car_id: int):
    try:
        db.query(Car).filter(Car.id == car_id).delete()
        db.commit()
    except Exception as e:
        print(f'Error in Delete Team : {str(e)}')
        raise e
