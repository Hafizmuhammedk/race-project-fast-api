from sqlalchemy.orm import Session
from app.schema import schemas
from app.models.car_team import Team
from fastapi import HTTPException, status


def Create_Team(db, team):
    existing_team = db.query(Team).filter(Team.name == team.name).first()
    if existing_team:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Team '{team.name}' already exists."
        )

    new_team = Team(name=team.name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team


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
