# backend/app/services/rag_pipeline.py

import os

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain.chains import RetrievalQA

from langchain.prompts import PromptTemplate

from app.services.pdf_loader import load_pdf

from app.services.vector_store import (
    create_vector_store
)

from app.services.llm_service import (
    get_llm
)


vectordb = None

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def process_pdf(file):

    global vectordb

    # Save uploaded PDF
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as f:

        f.write(file.file.read())

    print(f"PDF Saved: {file_path}")

    # Load PDF
    documents = load_pdf(file_path)

    print(
        "TOTAL DOCUMENTS:",
        len(documents)
    )

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(
        documents
    )

    print(
        "TOTAL CHUNKS:",
        len(split_docs)
    )

    # Create vector database
    vectordb = create_vector_store(
        split_docs
    )

    return "PDF uploaded successfully"


def ask_question(question):

    global vectordb

    if vectordb is None:

        return {
            "answer":
            "Please upload a PDF first.",
            "sources": []
        }

    try:

        # Better Retriever
        retriever = vectordb.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "score_threshold": 0.5,
                "k": 5
            }
        )

        llm = get_llm()

        # Better Prompt
        prompt_template = """

You are an expert AI assistant for answering questions from PDFs.

Rules:
- Answer ONLY from the PDF context.
- Do not make up facts.
- If unsure, say:
  "Information not found in PDF."
- Keep answers short and accurate.
- For technical questions:
  - give direct factual answers
  - avoid assumptions
  - avoid unnecessary explanation

Context:
{context}

Question:
{question}

Answer:

"""

        PROMPT = PromptTemplate(
            template=prompt_template,
            input_variables=[
                "context",
                "question"
            ]
        )

        # QA Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={
                "prompt": PROMPT
            }
        )

        # Modern invoke()
        response = qa_chain.invoke(
            {"query": question}
        )

        answer = response["result"]

        source_docs = response[
            "source_documents"
        ]

        # Extract sources
        sources = []

        for doc in source_docs:

            sources.append({
                "page":
                doc.metadata.get(
                    "page",
                    "Unknown"
                ),

                "content":
                doc.page_content[:300]
            })

        print(
            "Generated Answer:",
            answer
        )

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "answer": str(e),
            "sources": []
        }