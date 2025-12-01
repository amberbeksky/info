from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import AnnouncementIn
from models import Announcement

router = APIRouter(prefix="/announcements", tags=["Announcements"])

def db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()

@router.get("/")
def all_announcements(db: Session = Depends(db)):
    return db.query(Announcement).all()

@router.post("/")
def create_announcement(data: AnnouncementIn, db: Session = Depends(db)):
    new = Announcement(**data.dict())
    db.add(new)
    db.commit()
    return {"success": True}
