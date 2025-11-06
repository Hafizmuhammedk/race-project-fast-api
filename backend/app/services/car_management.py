from sqlalchemy.orm import Session
from app.models.car_team import Car as CarModel
# from app.models.car_team import Team as TeamModel


def Create_Car(team_name: str, db: Session, car):

    existing_car = db.query(CarModel).filter(
        CarModel.model == car.model).first()
    if existing_car:
        raise ValueError(f"Car model '{car.model}' already exists.")
    new_car = CarModel(model=car.model)
    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


def Get_car(db: Session):
    return db.query(CarModel).all()


def Get_Car_by(db: Session, car_id: int):
    return db.query(CarModel).filter(CarModel.id == car_id).first()


def Update_Car(db: Session, car_id: int, car_update):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        return None
    db_car.model = car_update.model
    db.commit()
    db.refresh(db_car)
    return db_car


def Delete_car(db: Session, car_id: int):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        return None
    db.delete(db_car)
    db.commit()
    return True
