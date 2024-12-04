import PyPDF2
from docx import Document
from rake_nltk import Rake
import re
import os
import nltk
import numpy as np
import io

nltk.download('stopwords')

def extract_text_from_pdf(file_obj):
    text = ""
    reader = PyPDF2.PdfReader(file_obj)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_obj):
    doc = Document(file_obj)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)  
    return text

def extract_keywords(text):
    rake = Rake() 
    rake.extract_keywords_from_text(text)
    return rake.get_ranked_phrases()[:10]

def process_resume(file_obj, file_extension):
    if file_extension.lower() == ".pdf":
        raw_text = extract_text_from_pdf(file_obj)
    elif file_extension.lower() == ".docx":
        raw_text = extract_text_from_docx(file_obj)
    else:
        raise ValueError("Unsupported file type. Use a PDF(.pdf) or Word (.docx) file.")

    cleaned_text = clean_text(raw_text)
    keywords = extract_keywords(cleaned_text)

    return keywords
