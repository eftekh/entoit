import os

from fastapi import HTTPException
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI


def get_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=400, detail="OpenAI API key not set.")
    return api_key


def translate(prompt: str) -> str:
    api_key = get_api_key()
    chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)

    chat_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are a helpful assistant that translates the user's text from "
                    "English to Italian."
                )
            ),
            HumanMessagePromptTemplate.from_template("{text}"),
        ]
    )

    message = chat_template.format_messages(text=prompt)

    return chat_model.invoke(message)