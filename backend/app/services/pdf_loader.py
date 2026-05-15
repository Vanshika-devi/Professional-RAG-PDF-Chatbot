# backend/app/services/pdf_loader.py

import fitz
import pytesseract
import re

from PIL import Image
from io import BytesIO

from langchain.schema import Document


def clean_text(text):

    text = text.replace("\n", " ")

    text = " ".join(text.split())

    return text


def is_garbage_text(text):

    if len(text) < 40:
        return True

    words = text.split()

    if len(words) < 8:
        return True

    readable_words = 0

    for word in words:

        if re.match(
            r"^[A-Za-z]+$",
            word
        ):
            readable_words += 1

    ratio = readable_words / max(
        len(words),
        1
    )

    return ratio < 0.4


def extract_ocr_text(page):

    pix = page.get_pixmap(
        matrix=fitz.Matrix(3, 3)
    )

    img_bytes = pix.tobytes("png")

    image = Image.open(
        BytesIO(img_bytes)
    )

    gray = image.convert("L")

    binary = gray.point(
        lambda x:
        0 if x < 140 else 255,
        "1"
    )

    text = pytesseract.image_to_string(
        binary
    )

    return clean_text(text)


def load_pdf(pdf_path):

    documents = []

    pdf = fitz.open(pdf_path)

    for page_num in range(len(pdf)):

        page = pdf[page_num]

        text = page.get_text("text")

        text = clean_text(text)

        # OCR fallback
        if is_garbage_text(text):

            print(
                f"OCR Running on Page {page_num+1}"
            )

            text = extract_ocr_text(page)

        # Skip garbage
        if not is_garbage_text(text):

            documents.append(
                Document(
                    page_content=text,

                    metadata={
                        "page":
                        page_num + 1,

                        "source":
                        pdf_path
                    }
                )
            )

    return documents