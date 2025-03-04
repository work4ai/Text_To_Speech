import fitz  # PyMuPDF
import pdfplumber
import PyPDF2
import os
import time

# Function to extract text using PyMuPDF (fast & accurate)
def extract_text_pymupdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Function to extract text using pdfplumber (good for scanned PDFs)
def extract_text_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n" if page.extract_text() else ""
    return text

# Function to extract text using PyPDF2 (structured PDFs)
def extract_text_pypdf2(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Function to save extracted text as a file with timestamp
def save_text_to_file(pdf_path, text):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(pdf_path)[0]  # Remove .pdf extension
    txt_filename = f"{base_name}_{timestamp}.txt"  # Create new filename
    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Extracted text saved as: {txt_filename}")

# Main Execution
pdf_path = "transformer.pdf"  # Change this to your PDF file

# Extract text using the best method
text = extract_text_pymupdf(pdf_path) or extract_text_pdfplumber(pdf_path) or extract_text_pypdf2(pdf_path)

# Save text to file
if text.strip():
    save_text_to_file(pdf_path, text)
else:
    print("No extractable text found in the PDF.")
