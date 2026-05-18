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

    # BETTER CHUNKING
    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=80,

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

                "k": 5

            }

        )

        llm = get_llm()

        # STRICT UNIVERSAL PROMPT
        prompt_template = """

You are a strict AI assistant.

Answer the question ONLY
from the provided PDF context.

IMPORTANT RULES:

- Do NOT use outside knowledge
- Do NOT guess answers
- Do NOT hallucinate
- Carefully search the context
- Extract exact information accurately
- Keep answers concise and clear

- If OCR text is corrupted,
  answer only from readable content

- Supported document types:
  - resumes
  - notes
  - assignments
  - research papers
  - technical PDFs
  - OCR PDFs

- Supported questions:
  - definitions
  - summaries
  - concepts
  - formulas
  - resume details
  - skills
  - projects
  - education
  - theoretical questions

- If answer is not found,
  reply ONLY:
  "Information not found in PDF."

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