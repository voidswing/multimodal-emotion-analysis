from app.core.llm import get_llm
from app.models.emotion import EmotionAnalysisResult
import base64

class EmotionService:
    def __init__(self):
        self.llm = get_llm()

    def analyze_emotion(self, text: str, image_bytes: bytes):
        image_base64 = base64.b64encode(image_bytes).decode()

        prompt = f"""
        다음의 텍스트와 이미지를 바탕으로 사용자의 감정을 다음 중에서 하나 골라줘:
        [기쁨, 슬픔, 분노, 놀람, 혐오, 두려움, 중립]

        텍스트: "{text}"
        이미지(Base64 인코딩됨): {image_base64[:100]}... (생략됨)

        응답 형식:
        감정: <선택된 감정>
        확신도: <0~1 사이의 실수>
        """

        response = self.llm.invoke(prompt).content
        emotion, confidence = self._parse_response(response)

        return {
            "text": text,
            "emotion": emotion,
            "confidence": confidence
        }

    def _parse_response(self, response: str):
        lines = response.strip().split("\n")
        emotion = lines[0].split(":")[1].strip()
        confidence = float(lines[1].split(":")[1].strip())
        return emotion, confidence
