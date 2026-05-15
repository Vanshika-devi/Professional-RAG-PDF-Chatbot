# backend/app/services/vector_store.py

import shutil
import os

from langchain_community.vectorstores import (
    Chroma
)

from app.services.embeddings import (
    embeddings
)


CHROMA_DIR = "./chroma_db"


def create_vector_store(documents):

    # Delete old database
    if os.path.exists(CHROMA_DIR):

        shutil.rmtree(CHROMA_DIR)

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    vectordb.persist()

    return vectordb