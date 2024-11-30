from rest_framework import viewsets
from .models import Professor, ResearchOpportunity, Student_Application
from .serializers import ProfessorSerializer, ResearchOpportunitySerializer, ApplicationSerializer, ProfessorDashboardSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# test
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse
from .models import Professor
from django.core.exceptions import ObjectDoesNotExist


# @permission_classes([IsAuthenticated])
class ProfessorView(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]


    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return ProfessorDetailSerializer
    #     return super().get_serializer_class()


# @permission_classes([IsAuthenticated])
class ResearchOpportunityViewSet(viewsets.ModelViewSet):
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
    
    queryset = ResearchOpportunity.objects.all()
    serializer_class = ResearchOpportunitySerializer

# test
class ApplicationView(viewsets.ModelViewSet):
    queryset = Student_Application.objects.all()
    serializer_class = ApplicationSerializer


# # test from binod gpt
# class ProfessorLoginView(APIView):
    
#     def post(self, request):
#     #     email = request.data.get('email')
#     #     password = request.data.get('password')

#     #     professor = Professor.objects.filter(email=email).first()

#     #     # serializer = ProfessorLoginSerializer(data=request.data)

#     #     if serializer.is_valid():
#     #         professor = serializer.validated_data
#     #         # test
#     #         # user = serializer.validated_data

#     #         # Generate JWT tokens
#     #         refresh = RefreshToken.for_user(professor)
#     #         # refresh = RefreshToken.for_user(professor)


#     #         return Response({
#     #             "access": str(refresh.access_token),
#     #             "refresh": str(refresh),
                
#     #         }, status=status.HTTP_200_OK)

#             # test ends

#             # research_posts = ResearchOpportunitySerializer(many=True, read_only=True)
#             # research_posts = ResearchOpportunity.objects.filter(professor=professor).values(
#             #     'id', 'title', 'description', 'posted_on', 'deadline', 
#             #     'is_active', 'required_skills', 'research_tags', 
#             #     'max_applications', 'current_applications'
#             # )
#             # professor_data = {
#             #     "id": professor.id,
#             #     "first_name": professor.first_name,
#             #     "last_name": professor.last_name,
#             #     "email": professor.email,
#             #     "department": professor.department,
#             #     "title": professor.title,
#             #     "office_location": professor.office_location,
#             #     "phone_number": professor.phone_number,
#             #     "research_interests": professor.research_interests,
#             #     "profile_picture": professor.profile_picture.url if professor.profile_picture else None,
#             #     "publications": professor.publications,
#             #     "posted_opportunities_count": professor.posted_opportunities_count,
#             #     "research_posts": list(research_posts),
#             # }
#             # return Response({
#             #     "message": "Login successful",
#             #     "professor_id": professor.id,
#             #     "data" : professor_data,
#             #     "email": professor.email,
#             #     "first_name": professor.first_name,
#             #     "last_name": professor.last_name,
#             # }, status=status.HTTP_200_OK)

#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
#     # just test
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         professor = Professor.objects.filter(email=email)
#         if professor and professor:
#             refresh = RefreshToken.for_user(professor)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
        
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    


# class ProfessorLoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

#         # Check if the professor exists
#         try:
#             professor = Professor.objects.get(email=email)
#         except Professor.DoesNotExist:
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

#         # Validate password (if passwords are hashed, use a hashing function)
#         if professor.password != password:  # Replace with `check_password` if using hashed passwords
#             return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

#         # Generate JWT tokens
#         refresh = RefreshToken.for_user(professor)

#         # request.session['professor_email'] = professor.email

#         # Return the professor's email and tokens
#         return Response({
#             "message": "Login successful",
#             "professor_email": professor.email,
#             "professor_department": professor.title,
#             "professor_id": professor.id,
#             "access": str(refresh.access_token),
#             "refresh": str(refresh),
#         }, status=status.HTTP_200_OK)

        
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


    # def get(self, request):
        
        
        

        # try:
            
           
        #     serializer = ProfessorSerializer
        # # professor = Professor.objects.get(all)
        #     return Response({
        #         # "message": f"Welcome, ",
        #         # 'message': professor.email
        #         "data": serializer.data
        #     })
        
        # except Professor.DoesNotExist:
        #     return Response({"error": "Professor profile not found"}, status=404)
        
#         # professor = Professor.objects.all()
#         # serializer = ProfessorSerializer(professor)
#         # # professor = Professor.objects.get(all)
#         # return Response({
#         #     "message": f"Welcome, {professor.email}!",
#         #     "data": serializer.data
#         # })

class ProfessorLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate email and password
            professor = Professor.objects.get(email=email)
            if professor.password != password:  # Replace with `check_password` if using hashed passwords
                raise AuthenticationFailed("Invalid email or password")
            
            # Store email in session (or generate token)
            request.session['professor_email'] = professor.email

            return Response({
                "message": "Login successful",
                "email": professor.email,
                "name": f"{professor.first_name} {professor.last_name}",
            }, status=status.HTTP_200_OK)

        except Professor.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)





class ProfessorDashboardAPIView(APIView):
    def get(self, request):
        # Retrieve professor email from session
        professor_email = request.session.get('professor_email')

        if not professor_email:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            # Fetch professor's information
            professor = Professor.objects.get(email=professor_email)
            serializer = ProfessorSerializer(professor)

            return Response({
                "message": f"Welcome, {professor.first_name}!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({"error": "Professor not found."}, status=status.HTTP_404_NOT_FOUND)

class ProfessorLogoutView(APIView):
    def post(self, request):
        if 'professor_id' in request.session:
            del request.session['professor_id']
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})