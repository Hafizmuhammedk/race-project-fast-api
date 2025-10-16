from fastapi import APIRouter, Depends, HTTPException  # responses
from fastapi.responses import JSONResponse
from config.database import get_db
from schema.schemas import Team
from sqlalchemy.orm import Session
from typing import List
from services.team_management import (
    Create_Team,
    Get_Team,
    Get_team_by,
    Update_Team,
    Delete_team
    )


router = APIRouter()


@router.post("/team", response_model=Team)
def create_team(team: Team, db: Session = Depends(get_db)):
    return Create_Team(db, team)


@router.get("/team", response_model=List[Team])
def get_team(db: Session = Depends(get_db)):
    return Get_Team(db)


@router.get("/team/{team_id}", response_model=Team)
def team_by_id(team_id: int, db: Session = Depends(get_db)):
    return Get_team_by(db, team_id)


@router.put("/team", response_model=Team)
def update_team(team_id: int, team_update: Team,
                db: Session = Depends(get_db)):
    db_team = Update_Team(db, team_id, team_update)
    if not db_team:
        return {"message": "Team not found"}
    return db_team


@router.delete("/team")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    try:
        db_team = Delete_team(db, team_id)
        if not db_team:
            return {"message": "Team not found"}
        return JSONResponse({"message": "deleted Successfully"},
                            status_code=200)
    except Exception as e:
        return HTTPException(status_code=404,
                             detail={"error": f"Error in deleting:{str(e)}"})
