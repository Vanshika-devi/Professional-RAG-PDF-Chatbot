# backend/app/services/rag_pipeline.py

import os
import uuid

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

    # UNIQUE FILE NAME
    unique_filename = (

        f"{uuid.uuid4()}_"
        f"{file.filename}"

    )

    # SAVE PDF
    file_path = os.path.join(

        UPLOAD_DIR,
        unique_filename

    )

    with open(file_path, "wb") as f:

        f.write(file.file.read())

    print(
        f"\nPDF STORED AT: {file_path}"
    )

    # LOAD PDF
    documents = load_pdf(file_path)

    print(
        "\nTOTAL DOCUMENTS:",
        len(documents)
    )

    if len(documents) == 0:

        return (
            "No readable text found "
            "inside PDF."
        )

    # UNIVERSAL CHUNKING
    splitter = RecursiveCharacterTextSplitter(

        chunk_size=700,

        chunk_overlap=150,

        separators=[

            "\n\n",

            "\n",

            ". ",

            " ",

            ""

        ]

    )

    split_docs = splitter.split_documents(
        documents
    )

    print(
        "\nTOTAL CHUNKS:",
        len(split_docs)
    )

    # CREATE VECTOR STORE
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

        # BETTER RETRIEVAL
        retriever = vectordb.as_retriever(

            search_type="similarity",

            search_kwargs={

                "k": 12

            }

        )

        llm = get_llm()

        # UNIVERSAL PROMPT
        prompt_template = """

You are a highly intelligent AI assistant.

Your task is to answer questions ONLY
from the provided PDF context.

IMPORTANT RULES:

- Carefully search through ALL context
- Answer accurately from the document
- Extract exact information precisely
- Answer any type of question including:
  - notes
  - resumes
  - assignments
  - research papers
  - books
  - technical PDFs
  - handwritten OCR text
  - concepts
  - definitions
  - summaries
  - formulas
  - explanations
  - skills
  - projects
  - education
  - dates
  - emails
  - phone numbers
  - technologies
  - theoretical questions

- If the answer exists in the document,
  provide the answer clearly

- If information truly does not exist,
  reply ONLY:
  "Information not found in PDF."

- Do NOT hallucinate
- Do NOT make assumptions
- Keep answers concise but accurate

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

        qa_chain = RetrievalQA.from_chain_type(

            llm=llm,

            retriever=retriever,

            return_source_documents=True,

            chain_type="stuff",

            chain_type_kwargs={

                "prompt": PROMPT

            }

        )

        response = qa_chain.invoke({

            "query": question

        })

        answer = response["result"]

        source_docs = response[
            "source_documents"
        ]

        print("\nQUESTION:", question)

        print("\nANSWER:", answer)

        sources = []

        for i, doc in enumerate(source_docs):

            print(f"\nSOURCE {i+1}")

            print(
                doc.page_content[:500]
            )

            sources.append({

                "page":
                doc.metadata.get(
                    "page",
                    "Unknown"
                ),

                "content":
                doc.page_content[:300]

            })

        return {

            "answer": answer,

            "sources": sources

        }

    except Exception as e:

        print("\nERROR:", e)

        return {

            "answer":
            "Error generating response.",

            "sources": []

        }