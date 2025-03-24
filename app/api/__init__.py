from fastapi import APIRouter
from .emotion import router as emotion_router

api_router = APIRouter()
api_router.include_router(emotion_router)