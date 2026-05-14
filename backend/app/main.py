import warnings
import logging

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from app.api.routes import router

# Hide warnings
warnings.filterwarnings("ignore")

# Reduce logs
logging.getLogger("transformers").setLevel(
    logging.ERROR
)

logging.getLogger("sentence_transformers").setLevel(
    logging.ERROR
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)