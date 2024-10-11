import nltk
from nltk.corpus import stopwords
import spacy
import re

# Download necessary NLTK data
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def simple_tokenize(text):
    return re.findall(r'\w+', text.lower())

def preprocess_text(text):
    tokens = simple_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def extract_skills(text, skills_list):
    tokens = set(simple_tokenize(text))
    return [skill for skill in skills_list if skill.lower() in tokens]

def extract_education(text):
    education_keywords = ['bachelor', 'master', 'phd', 'degree', 'diploma', 'certificate']
    doc = nlp(text)
    education_info = []
    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in education_keywords):
            education_info.append(sent.text)
    return education_info

def score_resume(resume_text, job_description, skills_list):
    resume_skills = extract_skills(resume_text, skills_list)
    job_skills = extract_skills(job_description, skills_skills)
    
    skill_match_score = len(set(resume_skills) & set(job_skills)) / len(set(job_skills)) * 100
    
    # You can add more scoring criteria here
    
    return skill_match_score

# Test the functions
if __name__ == "__main__":
    sample_resume = """
    John Doe
    Software Engineer

    Education:
    Bachelor of Science in Computer Science, University of Washington

    Skills:
    Python, Java, C++, Machine Learning, Data Analysis

    Experience:
    Software Engineer at Microsoft, Seattle (2018-present)
    - Developed machine learning models for product recommendations
    - Implemented data analysis pipelines using Python and SQL
    """

    sample_job_description = """
    We are looking for a Software Engineer with skills in Python, Machine Learning, and Data Analysis.
    The ideal candidate should have a degree in Computer Science or related field.
    """

    skills_list = ['Python', 'Java', 'C++', 'JavaScript', 'Machine Learning', 'Data Analysis', 'SQL']

    print("Preprocessed:", preprocess_text(sample_resume))
    print("Entities:", extract_entities(sample_resume))
    print("Skills:", extract_skills(sample_resume, skills_list))
    print("Education:", extract_education(sample_resume))
    print("Resume Score:", score_resume(sample_resume, sample_job_description, skills_list))