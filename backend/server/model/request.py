from pydantic import BaseModel


class APIKeyRequest(BaseModel):
    api_key: str


class UserPrompt(BaseModel):
    prompt: str
