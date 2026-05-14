from fastapi import APIRouter
from pydantic import BaseModel

from app.services.rag_pipeline import (
    ask_question,
    process_pdf
)

from fastapi import UploadFile, File

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.get("/")
def home():

    return {
        "message": "RAG PDF Chatbot Backend Running"
    }


@router.post("/upload")
def upload_pdf(
    file: UploadFile = File(...)
):

    response = process_pdf(file)

    return {
        "message": response
    }


@router.post("/ask")
def ask(
    request: QuestionRequest
):

    print("Question Received:", request.question)

    answer = ask_question(request.question)

    print("Generated Answer:", answer)

    return {
        "answer": answer
    }