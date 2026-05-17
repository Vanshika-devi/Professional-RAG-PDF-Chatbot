from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from app.auth.auth_bearer import JWTBearer

from app.services.rag_pipeline import (
    process_pdf,
    ask_question
)

router = APIRouter()


@router.post(
    "/upload",
    dependencies=[Depends(JWTBearer())]
)
async def upload_pdf(
    file: UploadFile = File(...)
):

    response = process_pdf(file)

    return {
        "message": response
    }


@router.post(
    "/ask",
    dependencies=[Depends(JWTBearer())]
)
async def ask(data: dict):

    question = data["question"]

    response = ask_question(question)

    return response