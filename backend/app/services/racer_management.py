from sqlalchemy.orm import Session
from app.models.Racers import Racer
from app.models.car_team import Team
from app.schema.schemas import RacerCreate


def Create_Racer(db: Session, racer: RacerCreate):

    db_team = db.query(Team).filter(Team.id == racer.team_id).first()
    if not db_team:
        raise ValueError(f"Team with id '{racer.team_id}' not found")

    db_racer = Racer(name=racer.name, team_id=racer.team_id)
    db.add(db_racer)
    db.commit()
    db.refresh(db_racer)
    return db_racer


def Get_Racers(db: Session):
    return db.query(Racer).all()


def Get_Racer_By_ID(db: Session, racer_id: int):
    return db.query(Racer).filter(Racer.id == racer_id).first()


def Update_Racer(db: Session, racer_id: int, racer_update: RacerCreate):
    db_racer = db.query(Racer).filter(Racer.id == racer_id).first()
    if not db_racer:
        return None

    db_racer.name = racer_update.name
    db_racer.team_id = racer_update.team_id  # ✅ match model
    db.commit()
    db.refresh(db_racer)
    return db_racer


def Delete_Racer(db: Session, racer_id: int):
    db_racer = db.query(Racer).filter(Racer.id == racer_id).first()
    if not db_racer:
        return None

    db.delete(db_racer)
    db.commit()
    return True
