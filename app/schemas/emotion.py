from pydantic import BaseModel

class EmotionAnalysisResponse(BaseModel):
    text: str
    emotion: str
    confidence: float
