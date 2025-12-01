from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import DocumentIn
from models import Document

router = APIRouter(prefix="/documents", tags=["Documents"])

def db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()

@router.get("/")
def get_documents(db: Session = Depends(db)):
    return db.query(Document).all()

@router.post("/")
def create_document(data: DocumentIn, db: Session = Depends(db)):
    doc = Document(**data.dict())
    db.add(doc)
    db.commit()
    return {"success": True}
