from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentLoginSerializer
from resume_analysis.services.ats_scoring import ATSScorer
from resume_analysis.services.student_resume_analysis import process_resume
from professor.models import ResearchOpportunity
import json
import os


class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data

            # Prepare student profile data
            student_data = {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "phone_number": student.phone_number,
                "year": student.year,
                "address": student.address,
                "resume": student.resume.url if student.resume else None,
                "profile_picture": student.profile_picture.url if student.profile_picture else None,
                "skills": student.skills,
                "gpa": student.gpa,
                "major": student.major,
                "graduation_year": student.graduation_year,
                "certifications": student.certifications,
                "linked_in_profile": student.linked_in_profile,
                "portfolio_website": student.portfolio_website,
                "github_profile": student.github_profile,
            }

            return Response({
                "message": "Login successful",
                "student": student_data,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentResumeAnalysisView(APIView):
    def get(self, request, student_id):
        try:
            # Get the student and their resume
            student = Student.objects.get(id=student_id)
            if not student.resume:
                return Response({
                    "error": "No resume found for this student"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Get all research opportunities
            opportunities = ResearchOpportunity.objects.filter(is_active=True)
            
            # Initialize ATS scorer
            scorer = ATSScorer()
            results = []

            # Get file extension
            _, file_extension = os.path.splitext(student.resume.name)

            # Process resume
            with student.resume.open('rb') as resume_file:
                resume_keywords = process_resume(resume_file, file_extension)

            # Score against each opportunity
            for opportunity in opportunities:
                score, detailed_scores, recommendations = scorer.calculate_ats_score(
                    " ".join(resume_keywords),
                    opportunity.description
                )

                results.append({
                    "opportunity_id": opportunity.id,
                    "opportunity_title": opportunity.title,
                    "overall_score": score,
                    "detailed_scores": detailed_scores,
                    "recommendations": recommendations
                })

            # Sort results by score
            results.sort(key=lambda x: x["overall_score"], reverse=True)

            return Response({
                "results": results
            }, status=status.HTTP_200_OK)

        except Student.DoesNotExist:
            return Response({
                "error": "Student not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class StudentResumeUploadView(APIView):
    def post(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            if 'resume' not in request.FILES:
                return Response({
                    "error": "No resume file provided"
                }, status=status.HTTP_400_BAD_REQUEST)

            # Save the new resume
            student.resume = request.FILES['resume']
            student.save()

            return Response({
                "message": "Resume uploaded successfully"
            }, status=status.HTTP_200_OK)

        except Student.DoesNotExist:
            return Response({
                "error": "Student not found"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
