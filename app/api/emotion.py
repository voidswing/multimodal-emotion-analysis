from fastapi import APIRouter, UploadFile, File, Form, Depends
from app.schemas.emotion import EmotionAnalysisResponse
from app.services.emotion_service import EmotionService

router = APIRouter(prefix="/api/emotion", tags=["Emotion Analysis"])

@router.post("/analyze", response_model=EmotionAnalysisResponse)
async def analyze_emotion(
    text: str = Form(...),
    image: UploadFile = File(...),
    service: EmotionService = Depends()
):
    image_bytes = await image.read()
    result = service.analyze_emotion(text, image_bytes)
    return result
