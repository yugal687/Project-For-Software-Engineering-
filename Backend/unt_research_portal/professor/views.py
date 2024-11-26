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

# test
class ApplicationView(viewsets.ModelViewSet):
    queryset = Student_Application.objects.all()
    serializer_class = ApplicationSerializer


# test
class ProfessorLoginView(APIView):
    def post(self, request):
        serializer = ProfessorLoginSerializer(data=request.data)
        if serializer.is_valid():
            professor = serializer.validated_data
            # research_posts = ResearchOpportunitySerializer(many=True, read_only=True)
            research_posts = ResearchOpportunity.objects.filter(professor=professor).values(
                'id', 'title', 'description', 'posted_on', 'deadline', 
                'is_active', 'required_skills', 'research_tags', 
                'max_applications', 'current_applications'
            )
            professor_data = {
                "id": professor.id,
                "first_name": professor.first_name,
                "last_name": professor.last_name,
                "email": professor.email,
                "department": professor.department,
                "title": professor.title,
                "office_location": professor.office_location,
                "phone_number": professor.phone_number,
                "research_interests": professor.research_interests,
                "profile_picture": professor.profile_picture.url if professor.profile_picture else None,
                "publications": professor.publications,
                "posted_opportunities_count": professor.posted_opportunities_count,
                "research_posts": list(research_posts),
            }
            return Response({
                "message": "Login successful",
                "professor_id": professor.id,
                "data" : professor_data,
                "email": professor.email,
                "first_name": professor.first_name,
                "last_name": professor.last_name,
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class ProfessorLogoutView(APIView):
    def post(self, request):
        if 'professor_id' in request.session:
            del request.session['professor_id']
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    

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
