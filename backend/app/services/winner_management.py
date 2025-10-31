from sqlalchemy.orm import Session
from app.models.winner import Winner, WinnerResult
from app.schema.schemas import WinnerCreate, WinnerResultCreate


def create_winner(db: Session, winner: WinnerCreate):

    db_winner = Winner(year=winner.year)
    db.add(db_winner)
    db.commit()
    db.refresh(db_winner)
    return db_winner


def get_all_winners(db: Session):
    return db.query(Winner).all()


def get_winner_by_id(db: Session, winner_id: int):
    return db.query(Winner).filter(Winner.id == winner_id).first()


def add_winner_result(db: Session, result: WinnerResultCreate):
    db_result = WinnerResult(
        winner_id=result.winner_id,
        position=result.position,
        racer_id=result.racer_id,
        points=result.points
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


def get_results_by_winner(db: Session, winner_id: int):

    return db.query(WinnerResult).filter(
        WinnerResult.winner_id == winner_id).all()


def delete_winner(db: Session, winner_id: int):
    db_winner = db.query(Winner).filter(Winner.id == winner_id).first()
    if db_winner:
        db.delete(db_winner)
        db.commit()
        return {"message": f"Winner {winner_id} deleted"}
    return {"error": "Winner not found"}
