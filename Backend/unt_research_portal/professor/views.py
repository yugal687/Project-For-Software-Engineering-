from rest_framework import viewsets
from .models import Professor, ResearchOpportunity, Student_Application
from .serializers import ProfessorSerializer, ResearchOpportunitySerializer, ApplicationSerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes

# test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import ProfessorLoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from students.models import Student


# @permission_classes([IsAuthenticated])
class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return ProfessorDetailSerializer
    #     return super().get_serializer_class()


# @permission_classes([IsAuthenticated])
class ResearchOpportunityViewSet(viewsets.ModelViewSet):
    queryset = ResearchOpportunity.objects.all()
    serializer_class = ResearchOpportunitySerializer
    
    @action(detail=True, methods=['post'], url_path='apply', url_name='apply')
    def apply(self, request, pk=None):
        """
        Custom action for students to apply for a research opportunity.
        """
        try:
            # Retrieve the specific research opportunity
            research_opportunity = ResearchOpportunity.objects.get(pk=pk)
        except ResearchOpportunity.DoesNotExist:
            return Response({"error": "Research opportunity not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the student has already applied
        student = request.user  # Assuming the logged-in user is a student
        if Student_Application.objects.filter(student=student, research_opportunity=research_opportunity).exists():
            return Response({"error": "You have already applied for this opportunity"}, status=status.HTTP_400_BAD_REQUEST)

        # Validate if the deadline has passed
        if research_opportunity.has_passed_deadline():
            return Response({"error": "The application deadline has passed"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new application and link it to the research opportunity
        application = Student_Application.objects.create(
            student=student,
            research_opportunity=research_opportunity,
        )

        # Increment application count on the research opportunity
        research_opportunity.increment_application_count()

        return Response(
            {"message": "Application submitted successfully", "application_id": application.id},
            status=status.HTTP_201_CREATED
        )

# test
class ApplicationView(viewsets.ModelViewSet):
    queryset = Student_Application.objects.all()
    serializer_class = ApplicationSerializer


# test
# class ProfessorLoginView(APIView):
#     def post(self, request):
#         serializer = ProfessorLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             professor = serializer.validated_data
#             # research_posts = ResearchOpportunitySerializer(many=True, read_only=True)
#             research_posts = ResearchOpportunity.objects.filter(professor=professor).values(
#                 'id', 'title', 'description', 'posted_on', 'deadline', 
#                 'is_active', 'required_skills', 'research_tags', 
#                 'max_applications', 'current_applications'
#             )
#             professor_data = {
#                 "id": professor.id,
#                 "first_name": professor.first_name,
#                 "last_name": professor.last_name,
#                 "email": professor.email,
#                 "department": professor.department,
#                 "title": professor.title,
#                 "office_location": professor.office_location,
#                 "phone_number": professor.phone_number,
#                 "research_interests": professor.research_interests,
#                 "profile_picture": professor.profile_picture.url if professor.profile_picture else None,
#                 "publications": professor.publications,
#                 "posted_opportunities_count": professor.posted_opportunities_count,
#                 "research_posts": list(research_posts),
#             }
#             return Response({
#                 "message": "Login successful",
#                 "professor_id": professor.id,
#                 "data" : professor_data,
#                 "email": professor.email,
#                 "first_name": professor.first_name,
#                 "last_name": professor.last_name,
#             }, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

# Using Session
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Professor
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ObjectDoesNotExist
from django.middleware.csrf import get_token



class ProfessorLoginView(APIView):
    def post(self, request):
        serializer = ProfessorLoginSerializer(data=request.data)
        if serializer.is_valid():
            professor = serializer.validated_data

            # Save professor info in session
            request.session['professor_id'] = professor.id
            request.session['professor_email'] = professor.email

            professor_data = ProfessorSerializer(professor).data
            return Response({
                "message": "Login successful",
                # "professor": professor_data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Using Session
# class ProfessorDashboardAPIView(APIView):
#     def get(self, request):
#         # Retrieve professor email from session
#         professor_email = request.session.get('professor_email')

#         if not professor_email:
#             return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             # Fetch professor's information
#             professor = Professor.objects.get(email=professor_email)
#             serializer = ProfessorSerializer(professor)

#             return Response({
#                 "message": f"Welcome, {professor.first_name}!",
#                 "data": serializer.data
#             }, status=status.HTTP_200_OK)

#         except ObjectDoesNotExist:
#             return Response({"error": "Professor not found."}, status=status.HTTP_404_NOT_FOUND)

class ProfessorDashboardView(APIView):
    def get(self, request):
        professor_id = request.session.get('professor_id')
        if not professor_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Fetch the authenticated professor
            professor = Professor.objects.get(id=professor_id)
            professor_serializer = ProfessorSerializer(professor)

            # Fetch all active research opportunities
            research_opportunities = ResearchOpportunity.objects.filter(is_active=True)
            research_serializer = ResearchOpportunitySerializer(research_opportunities, many=True)

            return Response({
                "message": f"Welcome, {professor.first_name}!",
                "professor_data": professor_serializer.data,
                "research_opportunities": research_serializer.data
            }, status=status.HTTP_200_OK)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ProfessorLogoutView(APIView):
    def post(self, request):
        if 'professor_id' in request.session:
            del request.session['professor_id']
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    
class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})
    

# class ProfessorLoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Validate email and password
#             professor = Professor.objects.get(email=email)
#             if professor.password != password:  # Replace with `check_password` if using hashed passwords
#                 raise AuthenticationFailed("Invalid email or password")
            
#             # Store email in session (or generate token)
#             request.session['professor_email'] = professor.email

#             return Response({
#                 "message": "Login successful",
#                 "email": professor.email,
#                 "name": f"{professor.first_name} {professor.last_name}",
#             }, status=status.HTTP_200_OK)

#         except Professor.DoesNotExist:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

# # Using JWT
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import Professor
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework.permissions import AllowAny


# class ProfessorLoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Validate professor credentials
#             professor = Professor.objects.get(email=email)
#             if professor.password != password:  # Replace with hashed password logic if applicable
#                 raise AuthenticationFailed("Invalid email or password")

#             # Generate JWT token for the professor
#             refresh = RefreshToken()
#             refresh['email'] = professor.email
#             refresh['is_professor'] = True  # Add custom claims if needed

#             # # Generate JWT tokens
#             # refresh = RefreshToken.for_user(professor)
#             access_token = str(refresh.access_token)

#             return Response({
#                 "message": "Login successful",
#                 "professor_email": professor.email,
#                 "access_token": access_token,
#                 "refresh_token": str(refresh),
#             }, status=status.HTTP_200_OK)

#         except Professor.DoesNotExist:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)


# # Using JWT

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated
# from .models import Professor
# from .serializers import ProfessorSerializer
# from rest_framework.exceptions import AuthenticationFailed

# class ProfessorDashboardAPIView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#           # Debugging code
#         auth = JWTAuthentication()
#         try:
#             validated_user, validated_token = auth.authenticate(request)
#             print(f"Validated User: {validated_user}")
#             print(f"Validated Token: {validated_token}")
#         except Exception as e:
#             print(f"Error during authentication: {e}")
#             return Response({"error": "Authentication error"}, status=status.HTTP_401_UNAUTHORIZED)

#         # Decode the token manually to extract email
#         auth = JWTAuthentication()
#         validated_user, validated_token = auth.authenticate(request)
#         # Retrieve professor_email from the token payload
#         professor_email = validated_token.get('email')
#         try:
#             professor = Professor.objects.get(email=professor_email)  # JWTAuthentication ensures request.user is set
#             serializer = ProfessorSerializer(professor)
#             return Response({
#                 "message": f"Welcome, {professor.first_name}!",
#                 "data": serializer.data,
#             }, status=status.HTTP_200_OK)

#         except Professor.DoesNotExist:
#             return Response({"error": "Professor profile not found."}, status=status.HTTP_404_NOT_FOUND)

#     # def get(self, request):
#     # # Decode the token manually to extract email
#     #     from rest_framework_simplejwt.authentication import JWTAuthentication
#     #     auth = JWTAuthentication()
#     #     validated_user, validated_token = auth.authenticate(request)

#     # # Use the email from the token payload to fetch the professor
#     #     professor_email = validated_token.get('email')  # Extract email from the token payload
#     #     try:
#     #         professor = Professor.objects.get(email=professor_email)
#     #         return Response({
#     #             "message": f"Welcome, {professor.first_name}!",
#     #             "data": {
#     #                 "email": professor.email,
#     #                 "department": professor.department,
#     #                 "title": professor.title,
#     #             },
#     #         }, status=200)
#     #     except Professor.DoesNotExist:
#     #         return Response({"error": "Professor not found."}, status=404)




# # View for listing research opportunities
# class ResearchOpportunityListView(APIView):
#     permission_classes = [AllowAny]
#     def get(self, request):
#         opportunities = ResearchOpportunity.objects.all()
#         serializer = ResearchOpportunitySerializer(opportunities, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
# # View for creating a new research opportunity
# class ResearchOpportunityCreateView(APIView):
#     # def get(self, request):
#     #     # If you want to display a specific form message for creating
#     #     return Response({"message": "Use POST to create a new research opportunity."}, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = ResearchOpportunitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(professor=request.user)  # Associate the logged-in professor if applicable
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # Using Session
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Professor
# from rest_framework.exceptions import AuthenticationFailed



# class ProfessorLoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Validate email and password
#             professor = Professor.objects.get(email=email)
#             if professor.password != password:  # Replace with `check_password` if using hashed passwords
#                 raise AuthenticationFailed("Invalid email or password")
            
#             # Store email in session (or generate token)
#             request.session['professor_email'] = professor.email

#             return Response({
#                 "message": "Login successful",
#                 "email": professor.email,
#                 "name": f"{professor.first_name} {professor.last_name}",
#             }, status=status.HTTP_200_OK)

#         except Professor.DoesNotExist:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Professor
from .serializers import ProfessorSerializer
from django.core.exceptions import ObjectDoesNotExist

# class ProfessorDashboardAPIView(APIView):
#     def get(self, request):
#         # Retrieve professor email from session
#         professor_email = request.session.get('professor_email')

#         if not professor_email:
#             return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             # Fetch professor's information
#             professor = Professor.objects.get(email=professor_email)
#             serializer = ProfessorSerializer(professor)

#             return Response({
#                 "message": f"Welcome, {professor.first_name}!",
#                 "data": serializer.data
#             }, status=status.HTTP_200_OK)

#         except ObjectDoesNotExist:
#             return Response({"error": "Professor not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ApplyResearchOpportunityView(APIView):
    def post(self, request):
        student_id = request.session.get('student_id')  # Get student from session
        if not student_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        opportunity_id = request.data.get('research_opportunity')
        if not opportunity_id:
            return Response({"error": "Research opportunity ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            research_opportunity = ResearchOpportunity.objects.get(id=opportunity_id)
        except ResearchOpportunity.DoesNotExist:
            return Response({"error": "Research opportunity not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if student has already applied
        if Student_Application.objects.filter(student_id=student_id, research_opportunity=research_opportunity).exists():
            return Response({"error": "You have already applied for this research opportunity."}, status=status.HTTP_400_BAD_REQUEST)

        # Create application
        application = Student_Application.objects.create(student_id=student_id, research_opportunity=research_opportunity)
        serializer = ApplicationSerializer(application)
        return Response({"message": "Application submitted successfully", "application": serializer.data}, status=status.HTTP_201_CREATED)



class ManageApplicationsView(APIView):
    def get(self, request):
        professor_id = request.session.get('professor_id')  # Get professor from session
        if not professor_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)
        print(f"Validated Professor ID: {professor_id}")

        applications = Student_Application.objects.filter(research_opportunity__professor_id=professor_id)
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, application_id):
        professor_id = request.session.get('professor_id')
        if not professor_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            application = Student_Application.objects.get(id=application_id, research_opportunity__professor_id=professor_id)
        except Student_Application.DoesNotExist:
            return Response({"error": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

        action = request.data.get('action')  # Accept or Reject
        if action == 'accept':
            application.status = 'accepted'
        elif action == 'reject':
            application.status = 'rejected'
        else:
            return Response({"error": "Invalid action."}, status=status.HTTP_400_BAD_REQUEST)

        application.save()
        return Response({"message": f"Application {action}ed successfully."}, status=status.HTTP_200_OK)


