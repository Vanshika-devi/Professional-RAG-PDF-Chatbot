# backend/app/services/llm_service.py

from langchain_community.llms import (
    Ollama
)


def get_llm():

    llm = Ollama(
        model="phi3"
    )

    return llm