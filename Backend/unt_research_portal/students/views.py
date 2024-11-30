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
from .serializers import StudentLoginSerializer, StudentSerializer
from .models import Student
from django.middleware.csrf import get_token
from professor.models import ResearchOpportunity
from professor.serializers import ResearchOpportunitySerializer, ResearchOpportunityStudentSerializer


class StudentLoginView(APIView):
    def post(self, request):
        serializer = StudentLoginSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.validated_data

            # Save student info in session
            request.session['student_id'] = student.id
            request.session['student_email'] = student.email

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



