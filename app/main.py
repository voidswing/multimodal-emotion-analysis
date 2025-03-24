from fastapi import FastAPI
from app.api import api_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title="Multimodal Emotion Analysis API",
    description="텍스트와 이미지를 분석하여 감정을 추론하는 멀티모달 서비스입니다.",
    version="1.0.0",
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Multimodal Emotion Analysis API is running 🚀"}
