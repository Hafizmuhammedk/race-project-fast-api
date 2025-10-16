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
