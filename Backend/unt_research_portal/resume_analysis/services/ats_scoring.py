import numpy as np
from typing import List, Dict, Tuple
import os
import re
from .student_resume_analysis import process_resume
from .job_opportunities_code import process_research_document


class JobPostingProcessor:
    """
    Uses Deepika's implementation to process job postings
    """
    def __init__(self):
        self.keyword_categories = {
            "technical_skills": [
                "python", "data science", "machine learning", "ai", "programming",
                "software", "analysis", "research", "algorithm", "statistics",
                "computer", "nlp", "database", "sql", "data mining",
                "information retrieval", "natural language processing", "text mining",
            ],
            "education": [
                "phd", "master", "bachelor", "degree", "university", "graduate",
                "undergraduate", "computer science", "information science", "data science",
            ],
            "experience": [
                "research", "project", "development", "analysis", "design",
                "implementation", "team", "laboratory", "publication",
            ],
            "soft_skills": [
                "communication", "collaboration", "team", "problem solving",
                "leadership", "organization", "management", "independent",
            ],
        }

    def extract_keywords(self, text: str) -> Dict[str, List[str]]:
        """Extract keywords from text based on predefined categories"""
        # For now, just split the text into words
        keywords = text.lower().split()
        
        # Categorize keywords
        found_keywords = {category: [] for category in self.keyword_categories}

        for category, category_keywords in self.keyword_categories.items():
            for keyword in category_keywords:
                if keyword in text.lower():
                    found_keywords[category].append(keyword)

        return found_keywords


class ATSScorer:
    def __init__(self):
        self.job_processor = JobPostingProcessor()
        self.weights = {
            "technical_skills": 0.4,
            "education": 0.3,
            "experience": 0.2,
            "soft_skills": 0.1,
        }

    def calculate_category_score(
        self, resume_keywords: List[str], posting_keywords: List[str]
    ) -> float:
        """Calculate matching score for a specific category"""
        if not resume_keywords or not posting_keywords:
            return 0.0

        resume_keywords = [k.lower() for k in resume_keywords]
        posting_keywords = [k.lower() for k in posting_keywords]

        matches = sum(
            1
            for k in posting_keywords
            if any(k in r or r in k for r in resume_keywords)
        )
        return (matches / len(posting_keywords)) * 100 if posting_keywords else 0

    def calculate_ats_score(
        self, resume_text: str, job_posting_text: str
    ) -> Tuple[float, Dict, List[str]]:
        """Calculate ATS score and provide recommendations"""
        # Extract keywords from resume
        resume_keywords = resume_text.lower().split()
        
        # Extract keywords from job posting
        posting_keywords = self.job_processor.extract_keywords(job_posting_text)

        scores = {}
        for category, weight in self.weights.items():
            category_score = self.calculate_category_score(
                resume_keywords, posting_keywords.get(category, [])
            )
            scores[category] = round(category_score, 2)

        final_score = sum(scores[cat] * weight for cat, weight in self.weights.items())

        recommendations = []
        for category, score in scores.items():
            if score < 70:
                missing = [
                    k
                    for k in posting_keywords.get(category, [])
                    if not any(
                        k.lower() in r.lower() or r.lower() in k.lower()
                        for r in resume_keywords
                    )
                ]
                if missing:
                    recommendations.append(
                        f"Consider adding these {category.replace('_', ' ')}: "
                        f"{', '.join(missing)}"
                    )

        return round(final_score, 2), scores, recommendations


def process_all_postings(resume_path: str, postings_dir: str) -> List[Dict]:
    """Process all job postings and return sorted results"""
    resume_keywords = process_resume(resume_path)

    scorer = ATSScorer()
    results = []

    for filename in os.listdir(postings_dir):
        if filename.endswith((".pdf", ".docx")):  # Only process PDF and DOCX files
            posting_path = os.path.join(postings_dir, filename)

            score, detailed_scores, recommendations = scorer.calculate_ats_score(
                resume_keywords, posting_path
            )

            results.append(
                {
                    "posting_name": filename,
                    "overall_score": score,
                    "detailed_scores": detailed_scores,
                    "recommendations": recommendations,
                }
            )

    results.sort(key=lambda x: x["overall_score"], reverse=True)
    return results


if __name__ == "__main__":
    resume_path = "../data/resumes/Sarah_Johnson_Resume.pdf"

    print("Processing resume and job postings...")
    try:
        results = process_all_postings(resume_path, "../data/job_postings")

        print("\nATS Analysis Results:")
        print("=" * 50)
        for i, result in enumerate(results, 1):
            print(f"\n{i}. Posting: {result['posting_name']}")
            print(f"Overall Score: {result['overall_score']}%")
            print("\nDetailed Scores:")
            for category, score in result["detailed_scores"].items():
                print(f"- {category.replace('_', ' ').title()}: {score}%")
            if result["recommendations"]:
                print("\nRecommendations:")
                for rec in result["recommendations"]:
                    print(f"- {rec}")
            print("-" * 50)

    except Exception as e:
        print(f"Error processing files: {str(e)}")
        print("Please ensure:")
        print("1. The resume file exists in data/resumes/")
        print("2. The job posting files exist in data/job_postings/")
        print("3. All required packages are installed")