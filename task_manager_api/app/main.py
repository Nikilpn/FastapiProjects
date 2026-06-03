from fastapi import FastAPI

from app.database import engine, Base
from app.models import Task
from app.routers import tasks,auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router)
app.include_router(auth.router)