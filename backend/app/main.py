from fastapi import FastAPI
from config.database import Base
from config.database import engine  # sessionlocal
# from sqlalchemy.orm import Session
from routers.track import router


app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(router)
