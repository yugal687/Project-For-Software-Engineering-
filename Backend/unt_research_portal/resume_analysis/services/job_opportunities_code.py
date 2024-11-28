import PyPDF2
from docx import Document
from rake_nltk import Rake
import re
import os
import nltk
import numpy as np

nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)  
    return text

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
    else:
        raise ValueError("Unsupported file type. Use a PDF(.pdf) or Word (.docx) file.")

    cleaned_text = clean_text(raw_text)
    keywords = extract_keywords(cleaned_text)

    return keywords

# Only run this if the script is run directly (not when imported)
if __name__ == "__main__":
    professor_files = {
        "Junhua_ding.docx": "../data/job_postings/Junhua_ding.docx",
        "sharmaresearch.docx": "../data/job_postings/sharmaresearch.docx",
        "Haihua_chen.docx": "../data/job_postings/Haihua_chen.docx"
    }

    # Loop through the dictionary and process each file
    for file_name, file_path in professor_files.items():
        print(f"\nProcessing {file_name}...")
        keywords = process_research_document(file_path)  # Extract keywords
        keywords_array = np.array(keywords)  # Convert to a numpy array (optional)
        print(f"Extracted Keywords from {file_name}: {keywords_array}")
        print(f"Type of Keywords: {type(keywords_array)}")