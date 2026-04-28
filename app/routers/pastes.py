from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.schemas import PasteCreate
from app.crud import create_paste, get_paste_by_slug, increment_views
import secrets

router = APIRouter()

@router.post("/pastes")
def create(paste: PasteCreate):
    db = SessionLocal()
    try:
        slug = secrets.token_urlsafe(5)
        new_paste = create_paste(db, paste, slug)
        return {"slug": new_paste.slug}
    finally:
        db.close()

@router.post("/pastes")
def create(paste: PasteCreate):
    db = SessionLocal()
    try:
        slug = secrets.token_urlsafe(5)
        new_paste = create_paste(db, paste, slug)
        return {"slug": new_paste.slug}
    finally:
        db.close()