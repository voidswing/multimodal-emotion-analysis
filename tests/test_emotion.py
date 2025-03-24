from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Multimodal Emotion Analysis API is running 🚀"}

def test_emotion_analysis():
    with open("tests/sample.jpg", "rb") as img:
        response = client.post(
            "/api/emotion/analyze",
            files={"image": ("sample.jpg", img, "image/jpeg")},
            data={"text": "오늘은 기분이 정말 좋아요!"}
        )

    assert response.status_code == 200
    data = response.json()
    assert "emotion" in data
    assert "confidence" in data
    assert data["text"] == "오늘은 기분이 정말 좋아요!"
