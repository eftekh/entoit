from typing import Any

from app import router

# Type alias for a JSON object
JSON = dict[str, Any]


@router.post("/ask_llm")
def get_llm_response(query: JSON) -> JSON:
    """
    Call OpenAI API with the user prompt and return the response.
    """
    response = "Hello, World!"
    return {"response": response}
