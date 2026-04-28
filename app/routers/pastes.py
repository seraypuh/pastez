from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.schemas import PasteCreate
from app.crud import create_paste, get_paste_by_slug, increment_views
import secrets

router = APIRouter()

@router.get("/p/{slug}")
def get_paste(slug: str):
    db = SessionLocal()

    try:
        paste = get_paste_by_slug(db, slug)

        if not paste:
            raise HTTPException(status_code=404, detail="Not found")

        increment_views(db, paste)

        return {
            "title": paste.title,
            "content": paste.content,
            "views": paste.views
        }

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