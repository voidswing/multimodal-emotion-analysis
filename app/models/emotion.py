from pydantic import BaseModel

class EmotionAnalysisResult(BaseModel):
    emotion: str
    confidence: float
