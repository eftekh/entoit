import argparse
from getpass import getpass

from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI

"""
This script can be used to chat directly with the translator.

Usage
-----
Inside the `entoit` development environment, running::

    python scripts/chat.py PROMPT

will send PROMPT to an OpenAI model and have it translated from English to Italian.
"""


def main(prompt: str) -> str:
    api_key = getpass("Please enter your OpenAI API key:")
    chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)

    chat_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=(
                    "You are a helpful assistant that translates the user's text from"
                    "English to Italian."
                )
            ),
            HumanMessagePromptTemplate.from_template("{text}"),
        ]
    )

    message = chat_template.format_messages(text=prompt)

    return chat_model.invoke(message)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chat with the translator")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()
    user_prompt = args.prompt

    main(user_prompt)
