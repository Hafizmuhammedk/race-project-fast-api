from fastapi import FastAPI
from app.config.database import Base
from app.config.database import engine  # sessionlocal
# from sqlalchemy.orm import Session
from app.routers.track import router as track_api
from app.routers.team import router as team_api
from app.routers.car import router as car_api
# from app.routers.car_connection import router as carteam_api

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(track_api)
app.include_router(team_api)
app.include_router(car_api)
# app.include_router(carteam_api)
