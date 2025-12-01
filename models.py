from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class OTPCode(Base):
    __tablename__ = "otp_codes"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    code = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Announcement(Base):
    __tablename__ = "announcements"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(Text)
    date = Column(String)
    author = Column(String)

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    type = Column(String)
    url = Column(String)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    date = Column(String)
    description = Column(Text)
