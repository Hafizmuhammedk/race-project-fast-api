from sqlalchemy.orm import Session
from schema import schemas
from models.car_team import Team


def Create_Team(db: Session, team_data):
    db_racer = Team(name=team_data.name)
    db.add(db_racer)
    db.commit()
    db.refresh(db_racer)
    return db_racer


def Get_Team(db: Session):
    return db.query(Team).all()


def Get_team_by(db: Session, team_id: int):
    db_team_id = db.query(Team).filter(Team.id == team_id).first()
    if not db_team_id:
        return None
    return db_team_id


def Update_Team(db: Session, team_id: int,
                team_update: schemas.Team):
    db_team = db.query(Team).filter(Team.id == team_id).first()
    if db_team:
        db_team.name = team_update.name
        db.commit()
        db.refresh(db_team)
    return db_team


def Delete_team(db: Session, team_id: int):
    try:
        db.query(Team).filter(Team.id == team_id).delete()
        db.commit()
    except Exception as e:
        print(f'Error in Delete Team : {str(e)}')
        raise e
