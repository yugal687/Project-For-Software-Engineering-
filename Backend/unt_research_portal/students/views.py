# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentLoginSerializer
# from professor.views import ResearchOpportunityViewSet
# # from professor.serializers import ResearchOpportunitySerializers
# from professor.models import ResearchOpportunity, Professor
# from rest_framework_simplejwt.tokens import RefreshToken
# from .authentication import StudentBackend

# class Apply(APIView):
#     def post(self, request):
#         serializer = StudentLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             student = serializer.validated_data
#             # professor = serializer.validated_data
#             research_posts = ResearchOpportunity.objects.values(
#                 'id', 'title', 'description', 'posted_on', 'deadline', 
#                 'is_active', 'required_skills', 'research_tags', 
#                 'max_applications', 'current_applications'
#             )
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
#                 "opportunities": research_posts
#             }, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



# class StudentLoginView(APIView):
#     def post(self, request):
#             email = request.data.get('email')
#             password = request.data.get('password')

#             user = StudentBackend.authenticate(request, email=email, password=password)

#             if user:
#                 # Generate JWT tokens
#                 refresh = RefreshToken.for_user(user)
#                 return Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                     'user': {
#                         'email': user.email,
#                         'name': user.first_name,
#                     },
#                     'id': user.id,
                    
#                 }, status=status.HTTP_200_OK)
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





#     # via serializer
#     # def post(self, request):
#     #     serializer = StudentLoginSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         student = serializer.validated_data
#     #         # professor = serializer.validated_data
#     #         research_posts = ResearchOpportunity.objects.values(
#     #             'id', 'title', 'description', 'posted_on', 'deadline', 
#     #             'is_active', 'required_skills', 'research_tags', 
#     #             'max_applications', 'current_applications'
#     #         )
#     #         # Prepare student profile data
#     #         student_data = {
#     #             "id": student.id,
#     #             "first_name": student.first_name,
#     #             "last_name": student.last_name,
#     #             "email": student.email,
#     #             "phone_number": student.phone_number,
#     #             "year": student.year,
#     #             "address": student.address,
#     #             "resume": student.resume.url if student.resume else None,
#     #             "profile_picture": student.profile_picture.url if student.profile_picture else None,
#     #             "skills": student.skills,
#     #             "gpa": student.gpa,
#     #             "major": student.major,
#     #             "graduation_year": student.graduation_year,
#     #             "certifications": student.certifications,
#     #             "linked_in_profile": student.linked_in_profile,
#     #             "portfolio_website": student.portfolio_website,
#     #             "github_profile": student.github_profile,
#     #         }

#     #         return Response({
#     #             "message": "Login successful",
#     #             "student": student_data,
#     #             "opportunities": research_posts
#     #         }, status=status.HTTP_200_OK)

#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Binod's Code for Student Views
# Using session and searilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import status
from .serializers import StudentLoginSerializer, StudentSerializer, ResearchOpportunityStudentSerializer
from .models import Student
from django.middleware.csrf import get_token
from professor.models import ResearchOpportunity
from professor.serializers import ResearchOpportunitySerializer


class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data

            # Save student info in session
            request.session['student_id'] = student.id
            request.session['student_email'] = student.email
            # request.session.save()

            student_data = StudentSerializer(student).data
            return Response({
                "message": "Login successful",
                "student": student_data
            }, status=status.HTTP_200_OK)
        
            # response.set_cookie(
            #     key='sessionid',
            #     value=request.session.session_key,
            #     httponly=True,  # Secure the cookie
            #     samesite='Lax',  # Adjust for frontend-backend domains
            # )
            # return response

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

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
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



class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "CSRF token set"})


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
