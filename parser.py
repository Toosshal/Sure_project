import os
import re
import sys
import json
import pdfplumber
import pytesseract
from PIL import Image
from rich import print_json

from parsers.chase_parser import parse_chase
from parsers.hdfc_parser import parse_hdfc
from parsers.sbi_parser import parse_sbi
from parsers.citi_parser import parse_citi
from parsers.amex_parser import parse_amex

# -------------------------------
# 🧠 Helper functions
# -------------------------------
def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdfplumber. Fallback to OCR if text is too short."""
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

        # Fallback to OCR if text too short
        if len(text.strip()) < 100:
            print("[yellow]Text too short, using OCR...[/yellow]")
            text = ocr_extract(pdf_path)
            used_ocr = True
        else:
            used_ocr = False

        return text, used_ocr

    except Exception as e:
        print(f"[red]Error extracting text: {e}[/red]")
        return "", False


def ocr_extract(pdf_path):
    """Perform OCR extraction using pytesseract."""
    from pdf2image import convert_from_path
    text = ""
    try:
        pages = convert_from_path(pdf_path)
        for page in pages:
            text += pytesseract.image_to_string(page)
    except Exception as e:
        print(f"[red]OCR extraction failed: {e}[/red]")
    return text


def detect_issuer(text):
    """Rudimentary bank detection logic based on keywords."""
    text_lower = text.lower()
    if "chase" in text_lower:
        return "chase"
    elif "hdfc" in text_lower:
        return "hdfc"
    elif "state bank" in text_lower or "sbi" in text_lower:
        return "sbi"
    elif "citibank" in text_lower or "citi" in text_lower:
        return "citi"
    elif "american express" in text_lower or "amex" in text_lower:
        return "amex"
    else:
        return "unknown"


# -------------------------------
# 🚀 Main PDF Parser
# -------------------------------
def main(pdf_path):
    text, used_ocr = extract_text_from_pdf(pdf_path)
    issuer = detect_issuer(text)

    data = {
        "issuer": issuer,
        "used_ocr": used_ocr,
    }

    if issuer == "chase":
        data.update(parse_chase(text))
    elif issuer == "hdfc":
        data.update(parse_hdfc(text))
    elif issuer == "sbi":
        data.update(parse_sbi(text))
    elif issuer == "citi":
        data.update(parse_citi(text))
    elif issuer == "amex":
        data.update(parse_amex(text))
    else:
        data["error"] = "Unknown issuer, no matching parser found."

    # Display output in JSON format
    print_json(json.dumps(data, indent=2))


# -------------------------------
# 🏁 Entry Point
# -------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[red]Usage: python parser.py <pdf_path>[/red]")
        sys.exit(1)

    pdf_path = sys.argv[1]

    if not os.path.exists(pdf_path):
        print(f"[red]File not found: {pdf_path}[/red]")
        sys.exit(1)

    main(pdf_path)
