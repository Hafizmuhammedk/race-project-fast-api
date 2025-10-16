from sqlalchemy.orm import Session
from schema import schemas
from models.car_team import Car


def Create_Car(db: Session, car_data):
    try:
        db_car = Car(model=car_data.model)
        db.add(db_car)
        db.commit()
        db.refresh(db_car)
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
