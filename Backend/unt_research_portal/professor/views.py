from rest_framework import viewsets
from .models import Professor, ResearchOpportunity
from .serializers import ProfessorSerializer, ResearchOpportunitySerializer
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes

# @permission_classes([IsAuthenticated])
class ProfessorView(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


# @permission_classes([IsAuthenticated])
class ResearchOpportunityViewSet(viewsets.ModelViewSet):
    queryset = ResearchOpportunity.objects.all()
    serializer_class = ResearchOpportunitySerializer
