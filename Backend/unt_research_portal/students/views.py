# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentLoginSerializer


# class StudentLoginView(APIView):
#     def post(self, request):
#         serializer = StudentLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             student = serializer.validated_data

#             # Prepare student profile data
#             student_data = {
#                 "id": student.id,
#                 "first_name": student.first_name,
#                 "last_name": student.last_name,
#                 "email": student.email,
#                 "phone_number": student.phone_number,
#                 "year": student.year,
#                 "address": student.address,
#                 "resume": student.resume.url if student.resume else None,
#                 "profile_picture": student.profile_picture.url if student.profile_picture else None,
#                 "skills": student.skills,
#                 "gpa": student.gpa,
#                 "major": student.major,
#                 "graduation_year": student.graduation_year,
#                 "certifications": student.certifications,
#                 "linked_in_profile": student.linked_in_profile,
#                 "portfolio_website": student.portfolio_website,
#                 "github_profile": student.github_profile,
#             }

#             return Response({
#                 "message": "Login successful",
#                 "student": student_data,
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Using session authentication and without searlizers

# from django.views import View
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from .models import Student
# import json
# from django.middleware.csrf import get_token


# @method_decorator(csrf_exempt, name='dispatch')
# class StudentLoginView(View):
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             email = data.get("email")
#             password = data.get("password")

#             # Validate credentials
#             student = Student.objects.get(email=email)
#             if student.password != password:  # Replace with hashed password validation
#                 return JsonResponse({"error": "Invalid email or password"}, status=401)

#             # Create session
#             request.session['student_id'] = student.id
#             request.session['student_email'] = student.email

#             return JsonResponse({"message": "Login successful", "student_email": student.email})
#         except Student.DoesNotExist:
#             return JsonResponse({"error": "Invalid email or password"}, status=401)
#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=400)
        
        
# class StudentDashboardView(View):
#     def get(self, request):
#         student_id = request.session.get('student_id')
#         if not student_id:
#             return JsonResponse({"error": "Not authenticated. Please log in first."}, status=401)

#         try:
#             student = Student.objects.get(id=student_id)
#             return JsonResponse({
#                 "message": f"Welcome, {student.first_name}!",
#                 "data": {
#                     "email": student.email,
#                     "name": f"{student.first_name} {student.last_name}",
#                     "major": student.major,
#                     "gpa": student.gpa,
#                 },
#             })
#         except Student.DoesNotExist:
#             return JsonResponse({"error": "Student not found"}, status=404)


# class StudentLogoutView(View):
#     def post(self, request):
#         if 'student_id' in request.session:
#             request.session.flush()  # Clears the session
#             return JsonResponse({"message": "Logged out successfully."})
#         return JsonResponse({"error": "No active session found."}, status=400)
    

# class CSRFTokenView(View):
#     def get(self, request):
#         csrf_token = get_token(request)
#         return JsonResponse({"csrfToken": csrf_token})



# Using session and searilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentApplicationSerializer, StudentLoginSerializer, StudentSerializer, ResearchOpportunityStudentSerializer
from .models import Student, StudentApplication
from django.middleware.csrf import get_token
from professor.models import ResearchOpportunity
from professor.serializers import ApplicationSerializer, ResearchOpportunitySerializer



class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data

            # Save student info in session
            request.session['student_id'] = student.id
            request.session['student_email'] = student.email
            request.session.save()
            
            print("Session Data:", request.session.items())

            student_data = StudentSerializer(student).data
            return Response({
                "message": "Login successful",
                "student": student_data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDashboardView(APIView):
    def get(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Fetch the authenticated student
            student = Student.objects.get(id=student_id)
            student_serializer = StudentSerializer(student)
            # student_skills = student.skills.split(",")

            # Fetch all active research opportunities
            research_opportunities = ResearchOpportunity.objects.filter(is_active=True)
            research_serializer = ResearchOpportunityStudentSerializer(research_opportunities, many=True)

            return Response({
                "message": f"Welcome, {student.first_name}!",
                "student_data": student_serializer.data,
                "research_opportunities": research_serializer.data
            }, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

# class StudentDashboardView(APIView):
#     def get(self, request):
#         student_id = request.session.get('student_id')
#         if not student_id:
#             return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             student = Student.objects.get(id=student_id)
#             serializer = StudentSerializer(student)
#             return Response({
#                 "message": f"Welcome, {student.first_name}!",
#                 "data": serializer.data
#             }, status=status.HTTP_200_OK)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


class StudentLogoutView(APIView):
    def post(self, request):
        if 'student_id' in request.session:
            request.session.flush()  # Clears all session data
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "No active session found."}, status=status.HTTP_400_BAD_REQUEST)



# class ApplyResearchOpportunityView(APIView):
#     def post(self, request):
#         student_id = request.session.get('student_id')  # Get student from session
#         if not student_id:
#             return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

#         opportunity_id = request.data.get('research_opportunity')
#         if not opportunity_id:
#             return Response({"error": "Research opportunity ID is required."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             research_opportunity = ResearchOpportunity.objects.get(id=opportunity_id)
#         except ResearchOpportunity.DoesNotExist:
#             return Response({"error": "Research opportunity not found."}, status=status.HTTP_404_NOT_FOUND)

#         # Check if student has already applied
#         if Student_Application.objects.filter(student_id=student_id, research_opportunity=research_opportunity).exists():
#             return Response({"error": "You have already applied for this research opportunity."}, status=status.HTTP_400_BAD_REQUEST)

#         # Create application
#         application = Student_Application.objects.create(student_id=student_id, research_opportunity=research_opportunity)
#         serializer = ApplicationSerializer(application)
#         return Response({"message": "Application submitted successfully", "application": serializer.data}, status=status.HTTP_201_CREATED)

class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})



# # Using JWT tokens for authentication

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, permissions
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from .models import Student
# from .serializers import (
#     StudentSerializer,
#     StudentRegistrationSerializer,
#     StudentLoginSerializer,
# )
# from .utils import get_tokens_for_student

# class StudentRegistrationView(APIView):
#     def post(self, request):
#         serializer = StudentRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             student = serializer.save()
#             return Response({
#                 "message": "Student registered successfully",
#                 "student_id": student.id
#             }, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentLoginView(APIView):
#     def post(self, request):
#         serializer = StudentLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             student = serializer.validated_data

#             # Generate JWT tokens
#             tokens = get_tokens_for_student(student)

#             return Response({
#                 "message": "Login successful",
#                 "student_email": student.email,
#                 "access_token": tokens['access'],
#                 "refresh_token": tokens['refresh'],
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDashboardView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def get(self, request):
        
#         # Extract email from JWT token payload
#         # email = request.auth.get('email')
#         email = request.user.email


#         try:
#             student = Student.objects.get(email=email)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

#         # Return student data
#         serializer = StudentSerializer(student)
#         return Response({
#             "message": f"Welcome, {student.first_name}!",
#             "data": serializer.data
#         }, status=status.HTTP_200_OK)




import os
from docx import Document
from PyPDF2 import PdfReader
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, StudentApplication
from professor.models import ResearchOpportunity


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

class ApplyResearchOpportunityView(APIView):
    def post(self, request):
        student_id = request.session.get('student_id')
        if not student_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        opportunity_id = request.data.get('research_opportunity')
        resume_file = request.FILES.get('resume') 
        if not opportunity_id:
            return Response({"error": "Research opportunity ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            research_opportunity = ResearchOpportunity.objects.get(id=opportunity_id)
        except ResearchOpportunity.DoesNotExist:
            return Response({"error": "Research opportunity not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if student has already applied
        if StudentApplication.objects.filter(student_id=student_id, research_opportunity=research_opportunity).exists():
            return Response({"error": "You have already applied for this research opportunity."}, status=status.HTTP_400_BAD_REQUEST)

        
        # Validate resume upload
        if not resume_file:
            return Response({"error": "Resume upload is required to apply."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the uploaded resume temporarily
        student = Student.objects.get(id=student_id)
        application = StudentApplication.objects.create(
            student=student,
            research_opportunity=research_opportunity,
            resume=resume_file
        )
        # Analyze the resume
        resume_path = application.resume.path
        required_keywords = research_opportunity.required_skills.split(",")  # Assuming skills are comma-separated
        score = ResumeAnalyzer.analyze_resume(resume_path, required_keywords)

        # Validate the score threshold
        threshold = 70  # Example threshold
        if score < threshold:
            application.delete()  # Cleanup if the resume doesn't meet the threshold
            return Response({"error": f"Resume score too low ({score:.2f}%). Minimum required: {threshold}%."}, status=status.HTTP_400_BAD_REQUEST)

        # Save the score to the application
        application.resume_score = score
        application.save()

        return Response({
            "message": "Application submitted successfully",
            "application_id": application.id,
            "score": score
        }, status=status.HTTP_201_CREATED)

from rest_framework import viewsets

class StudentView(viewsets.ModelViewSet):
    # research_opportunities = ResearchOpportunity.objects.filter(is_active=True)
    # research_serializer = ResearchOpportunityStudentSerializer(research_opportunities, many=True)

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentApplicationView(viewsets.ModelViewSet):
    # research_opportunities = ResearchOpportunity.objects.filter(is_active=True)
    # research_serializer = ResearchOpportunityStudentSerializer(research_opportunities, many=True)

    queryset = StudentApplication.objects.all()
    serializer_class = ApplicationSerializer

class AllResearchOpportunitiesView(APIView):
    def get(self, request):
        research_opportunities = ResearchOpportunity.objects.filter(is_active=True)  # Show only active opportunities
        serializer = ResearchOpportunityStudentSerializer(research_opportunities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# for ats score
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

class ApplyResearchOpportunityView(APIView):
    def post(self, request):
        # student_id = request.session.get('student_id')
        # if not student_id:
        #     return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        # opportunity_id = request.data.get('research_opportunity')
        # resume = request.FILES.get('resume') 
        # if not opportunity_id:
        #     return Response({"error": "Research opportunity ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     research_opportunity = ResearchOpportunity.objects.get(id=opportunity_id)
        # except ResearchOpportunity.DoesNotExist:
        #     return Response({"error": "Research opportunity not found."}, status=status.HTTP_404_NOT_FOUND)

        # # Check if student has already applied
        # if StudentApplication.objects.filter(student_id=student_id, research_opportunity=research_opportunity).exists():
        #     return Response({"error": "You have already applied for this research opportunity."}, status=status.HTTP_400_BAD_REQUEST)

        
        # Validate resume upload
        # if not resume:
        #     return Response({"error": "Resume upload is required to apply."}, status=status.HTTP_400_BAD_REQUEST)
        
        required_keywoards_front_end = request.data.get('required_keywoards_front_end')
        resume_path_front_end = request.data.get('resume_path_front_end')

        # Save the uploaded resume temporarily
        # student = Student.objects.get(id=student_id)
        # application = StudentApplication.objects.create(
        #     student=student,
        #     research_opportunity=research_opportunity,
        #     resume=resume
        # )
        # Analyze the resume
        # resume_path = application.resume.path
        required_keywords = required_keywoards_front_end.split(",")  # Assuming skills are comma-separated
        score = ResumeAnalyzer.analyze_resume(resume_path_front_end, required_keywords)

        # Validate the score threshold
        threshold = 70  # Example threshold
        if score < threshold:
            # application.delete()  # Cleanup if the resume doesn't meet the threshold
            return Response({"error": f"Resume score too low ({score:.2f}%). Minimum required: {threshold}%."}, status=status.HTTP_400_BAD_REQUEST)

        # Save the score to the application
        application.resume_score = score
        application.save()

        return Response({
            "message": "Application submitted successfully",
            "application_id": application.id,
            "score": score
        }, status=status.HTTP_201_CREATED)