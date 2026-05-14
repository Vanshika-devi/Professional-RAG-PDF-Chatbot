from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)