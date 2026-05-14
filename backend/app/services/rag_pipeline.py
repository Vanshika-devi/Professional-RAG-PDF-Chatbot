from tempfile import NamedTemporaryFile

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain.chains import RetrievalQA

from app.services.pdf_loader import load_pdf

from app.services.vector_store import (
    create_vector_store
)

from app.services.llm_service import get_llm

vectordb = None


def process_pdf(file):

    global vectordb

    with NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp:

        temp.write(file.file.read())

        temp_path = temp.name

    documents = load_pdf(temp_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )

    split_docs = splitter.split_documents(
        documents
    )

    vectordb = create_vector_store(
        split_docs
    )

    return "PDF uploaded successfully"


def ask_question(question):

    global vectordb

    if vectordb is None:

        return "Please upload a PDF first."

    try:

        retriever = vectordb.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        llm = get_llm()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever
        )

        response = qa_chain.run(question)

        return response

    except Exception as e:

        print("ERROR:", e)

        return str(e)