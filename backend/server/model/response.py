from pydantic import BaseModel


class LLMResponse(BaseModel):
    prompt: str
    translation: str