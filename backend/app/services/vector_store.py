from langchain_community.vectorstores import Chroma

from app.services.embeddings import embeddings


def create_vector_store(documents):

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vectordb