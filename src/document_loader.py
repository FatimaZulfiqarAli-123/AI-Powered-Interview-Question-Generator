# ============================================================
# SECTION 04: DOCUMENT LOADER
# ============================================================

import os

from pypdf import PdfReader
from docx import Document


def read_pdf(file_path):
    """
    Extract text from a PDF file.
    """

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def read_docx(file_path):
    """
    Extract text from a DOCX file.
    """

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text


def read_txt(file_path):
    """
    Read a TXT file.
    """

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


def read_file(file_path):
    """
    Automatically detect the file type
    and extract its text.
    """

    extension = os.path.splitext(
        file_path
    )[1].lower()

    if extension == ".pdf":

        return read_pdf(file_path)

    elif extension == ".docx":

        return read_docx(file_path)

    elif extension == ".txt":

        return read_txt(file_path)

    else:

        raise ValueError(
            f"Unsupported file type: {extension}"
        )


def clean_text(text):
    """
    Clean extracted document text.
    """

    text = text.replace("\x00", "")

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line:
            lines.append(line)

    return "\n".join(lines)