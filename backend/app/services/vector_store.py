import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"

from chromadb.config import Settings

import chromadb

from langchain_chroma import Chroma

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

CHROMA_DIR = "./chroma_db"

embedding_model = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"

)

client = chromadb.PersistentClient(

    path=CHROMA_DIR,

    settings=Settings(
        anonymized_telemetry=False
    )
)


def create_vector_store(split_docs):

    # DELETE OLD COLLECTION
    try:

        client.delete_collection(
            "pdf_collection"
        )

    except:
        pass

    vectordb = Chroma.from_documents(

        documents=split_docs,

        embedding=embedding_model,

        client=client,

        collection_name="pdf_collection"

    )

    return vectordb