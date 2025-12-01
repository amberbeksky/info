from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import EventIn
from models import Event

router = APIRouter(prefix="/events", tags=["Events"])

def db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()

@router.get("/")
def get_events(db: Session = Depends(db)):
    return db.query(Event).all()

@router.post("/")
def create_event(data: EventIn, db: Session = Depends(db)):
    ev = Event(**data.dict())
    db.add(ev)
    db.commit()
    return {"success": True}
