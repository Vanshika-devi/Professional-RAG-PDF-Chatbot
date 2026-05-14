from langchain_community.llms import Ollama


def get_llm():

    llm = Ollama(
        model="phi3"
    )

    return llm