from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentLoginSerializer
from professor.views import ResearchOpportunityViewSet
# from professor.serializers import ResearchOpportunitySerializers
from professor.models import ResearchOpportunity, Professor

class Apply(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data
            # professor = serializer.validated_data
            research_posts = ResearchOpportunity.objects.values(
                'id', 'title', 'description', 'posted_on', 'deadline', 
                'is_active', 'required_skills', 'research_tags', 
                'max_applications', 'current_applications'
            )
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
                "opportunities": research_posts
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data
            # professor = serializer.validated_data
            research_posts = ResearchOpportunity.objects.values(
                'id', 'title', 'description', 'posted_on', 'deadline', 
                'is_active', 'required_skills', 'research_tags', 
                'max_applications', 'current_applications'
            )
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
                "opportunities": research_posts
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
