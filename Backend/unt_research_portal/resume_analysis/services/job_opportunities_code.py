import os
from rake_nltk import Rake
import nltk
import numpy as np

nltk.download("stopwords")


def extract_text_from_docx(docx_path):
    """Try multiple methods to extract text from docx"""
    # First try python-docx
    try:
        from docx import Document

        doc = Document(docx_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        print(f"Warning: docx method failed, trying raw read for {docx_path}")

    # Fallback to raw text reading if docx fails
    try:
        with open(docx_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"Warning: All methods failed for {docx_path}")
        return None


def extract_text_from_pdf(pdf_path):
    try:
        import PyPDF2

        text = ""
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Warning: Failed to read PDF {pdf_path}")
        return None


def clean_text(text):
    if text is None:
        return ""
    import re

    return re.sub(r"\W+", " ", text)


def extract_keywords(text):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:10]


def process_research_document(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":
        raw_text = extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        raw_text = extract_text_from_docx(file_path)
    else:  # Handle as regular text file
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                raw_text = f.read()
        except Exception as e:
            print(f"Warning: Failed to read file {file_path}")
            raw_text = None

    cleaned_text = clean_text(raw_text)
    keywords = extract_keywords(cleaned_text)
    return keywords


# Only run this if the script is run directly (not when imported)
if __name__ == "__main__":
    professor_files = {
        "Junhua_ding.docx": "../data/job_postings/Junhua_ding.docx",
        "sharmaresearch.docx": "../data/job_postings/sharmaresearch.docx",
        "Haihua_chen.docx": "../data/job_postings/Haihua_chen.docx",
    }

    # Loop through the dictionary and process each file
    for file_name, file_path in professor_files.items():
        print(f"\nProcessing {file_name}...")
        keywords = process_research_document(file_path)  # Extract keywords
        keywords_array = np.array(keywords)  # Convert to a numpy array (optional)
        print(f"Extracted Keywords from {file_name}: {keywords_array}")
        print(f"Type of Keywords: {type(keywords_array)}")
