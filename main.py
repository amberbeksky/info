from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
from auth import router as auth_router
from announcements import router as ann_router
from documents import router as doc_router
from events import router as events_router

app = FastAPI(title="KCSON API")

# CORS (чтобы Flutter мог обращаться)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Создаем БД
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(auth_router)
app.include_router(ann_router)
app.include_router(doc_router)
app.include_router(events_router)

@app.get("/")
def root():
    return {"status": "KCSON API is running"}
