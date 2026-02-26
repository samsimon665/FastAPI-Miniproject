from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine
from app import models
from app.routers import user as user_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
