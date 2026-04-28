from app import models

def create_paste(db, paste, slug):
    new_paste = models.Paste(
        title=paste.title,
        content=paste.content,
        slug=slug
    )
    db.add(new_paste)
    db.commit()
    db.refresh(new_paste)
    return new_paste


def get_paste_by_slug(db, slug: str):
    return db.query(models.Paste).filter(
        models.Paste.slug == slug
    ).first()


def increment_views(db, paste):
    paste.views += 1
    db.commit()
    return paste