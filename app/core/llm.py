from langchain_openai import ChatOpenAI
from .config import get_settings

def get_llm():
    settings = get_settings()
    return ChatOpenAI(
        model=settings.OPENAI_MODEL,
        api_key=settings.OPENAI_API_KEY
    )
