""" FastAPI backend server """

import os

from fastapi import APIRouter, HTTPException
from model.request import APIKeyRequest, UserPrompt
from model.response import LLMResponse
from model.translate import translate


router = APIRouter(prefix="/api/v1")

@router.post("/set_api_key")
def set_api_key(request: APIKeyRequest):
    """Store a user-provided API key in an environment variable."""
    os.environ["OPENAI_API_KEY"] = request.api_key
    return {"message": "OpenAI API key set successfully."}


@router.post("/ask_llm", response_model=LLMResponse)
def get_llm_response(request: UserPrompt) -> LLMResponse:
    """
    Call OpenAI API with the user prompt and return the LLM response.
    """
    try:
        translation = translate(request.prompt)
        return LLMResponse(prompt=request.prompt, translation=translation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

