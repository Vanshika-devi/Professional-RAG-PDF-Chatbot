import fitz

import pytesseract

from PIL import Image

from io import BytesIO

from langchain.schema import Document

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def load_pdf(pdf_path):

    documents = []

    pdf = fitz.open(pdf_path)

    for page_num in range(len(pdf)):

        page = pdf[page_num]

        text = page.get_text()

        # OCR fallback
        if not text.strip():

            pix = page.get_pixmap()

            img_bytes = pix.tobytes("png")

            image = Image.open(
                BytesIO(img_bytes)
            )

            text = pytesseract.image_to_string(
                image
            )

        if text.strip():

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "page": page_num + 1
                    }
                )
            )

    return documents