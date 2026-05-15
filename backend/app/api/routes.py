# backend/app/api/routes.py

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from pydantic import BaseModel

from app.services.rag_pipeline import (
    process_pdf,
    ask_question
)

router = APIRouter()


class QuestionRequest(BaseModel):

    question: str


@router.get("/")
def home():

    return {
        "message":
        "RAG PDF Chatbot Backend Running"
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

    response = ask_question(
        request.question
    )

    return response