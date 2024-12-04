from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_student(student):
    refresh = RefreshToken()
    refresh['email'] = student.email
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



import os
from docx import Document
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


class ResumeAnalyzer:
    @staticmethod
    def extract_text(file_path):
        """Extract text from a resume file."""
        _, extension = os.path.splitext(file_path)

        if extension == ".docx":
            doc = Document(file_path)
            return " ".join([para.text for para in doc.paragraphs])
        elif extension == ".pdf":
            reader = PdfReader(file_path)
            return " ".join([page.extract_text() for page in reader.pages])
        else:
            raise ValueError("Unsupported file format. Please upload a .docx or .pdf file.")

    @staticmethod
    def analyze_resume(file_path, required_keywords):
        """Analyze the resume and return a score."""
        text = ResumeAnalyzer.extract_text(file_path)

        # Tokenize and clean text
        tokens = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

        # Match keywords and calculate score
        matches = [word for word in filtered_tokens if word in required_keywords]
        score = len(matches) / len(required_keywords) * 100
        return score