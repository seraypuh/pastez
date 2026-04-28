from fastapi import FastAPI
from app.database import Base, engine
from app import models
from pydantic import BaseModel
import secrets
from app.database import SessionLocal
from fastapi import HTTPException
from app.routers.pastes import router as pastes_router

app = FastAPI()
app.include_router(pastes_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"status": "ok"}