from fastapi import FastAPI
from config.database import Base
from config.database import engine  # sessionlocal
# from sqlalchemy.orm import Session
from routers.track import router as track_api
from routers.team import router as team_api
from routers.car import router as car_api

app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(track_api)
app.include_router(team_api)
app.include_router(car_api)

