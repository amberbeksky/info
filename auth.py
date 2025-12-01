from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import OTPCode
from schemas import OTPRequest, OTPVerify
from random import randint

router = APIRouter(prefix="/auth", tags=["Auth"])

def db():
    d = SessionLocal()
    try:
        yield d
    finally:
        d.close()

@router.post("/request_code")
def request_code(data: OTPRequest, db: Session = Depends(db)):
    code = str(randint(1000, 9999))
    db_item = OTPCode(phone=data.phone, code=code)
    db.add(db_item)
    db.commit()
    return {"success": True, "code": code}

@router.post("/verify_code")
def verify_code(data: OTPVerify, db: Session = Depends(db)):
    item = db.query(OTPCode).filter(
        OTPCode.phone == data.phone,
        OTPCode.code == data.code
    ).first()

    if item:
        return {"success": True, "token": f"TOKEN-{data.phone}"}
    return {"success": False}
