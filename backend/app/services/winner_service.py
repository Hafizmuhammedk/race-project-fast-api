from sqlalchemy.orm import Session
from app.models.winner import Winner, WinnerResult
from app.schema.schemas import WinnerCreate, WinnerResultCreate


def create_winner(db: Session, winner_data: WinnerCreate):
    winner = Winner(year=winner_data.year)
    db.add(winner)
    db.commit()
    db.refresh(winner)
    return winner


def get_winners(db: Session):
    return db.query(Winner).all()


def create_winner_result(db: Session, result_data: WinnerResultCreate):
    result = WinnerResult(
        winner_id=result_data.winner_id,
        position=result_data.position,
        racer_id=result_data.racer_id,
        points=result_data.points
    )
    db.add(result)
    db.commit()
    db.refresh(result)
    return result


def get_winner_results(db: Session, winner_id: int):
    return db.query(WinnerResult).filter(
        WinnerResult.winner_id == winner_id).all()
