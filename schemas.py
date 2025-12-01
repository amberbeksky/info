from pydantic import BaseModel

class OTPRequest(BaseModel):
    phone: str

class OTPVerify(BaseModel):
    phone: str
    code: str

class AnnouncementIn(BaseModel):
    title: str
    text: str
    date: str
    author: str

class DocumentIn(BaseModel):
    title: str
    date: str
    type: str
    url: str

class EventIn(BaseModel):
    title: str
    date: str
    description: str
