from rest_framework import viewsets
# from .models import Professor, ResearchOpportunity
# from .serializers import ProfessorSerializer, ResearchOpportunitySerializer
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.decorators import permission_classes

# # @permission_classes([IsAuthenticated])
# class ProfessorView(viewsets.ModelViewSet):
#     queryset = Professor.objects.all()
#     serializer_class = ProfessorSerializer


# # @permission_classes([IsAuthenticated])
# class ResearchOpportunityViewSet(viewsets.ModelViewSet):
#     queryset = ResearchOpportunity.objects.all()
#     serializer_class = ResearchOpportunitySerializer


# from rest_framework import generics
# from .models import Professor, ResearchOpportunity
# from .serializers import ProfessorSerializer, ResearchOpportunitySerializer

# class ProfessorListView(generics.ListCreateAPIView):
#     queryset = Professor.objects.all()
#     serializer_class = ProfessorSerializer

# class ProfessorDetailView(generics.RetrieveAPIView):
#     queryset = Professor.objects.all()
#     serializer_class = ProfessorSerializer
#     lookup_field = 'id'

# class ResearchOpportunityListView(generics.ListCreateAPIView):
#     queryset = ResearchOpportunity.objects.all()
#     serializer_class = ResearchOpportunitySerializer

# class ResearchOpportunityDetailView(generics.RetrieveAPIView):
#     queryset = ResearchOpportunity.objects.all()
#     serializer_class = ResearchOpportunitySerializer
#     lookup_field = 'id'


from rest_framework import viewsets
from .models import Professor, ResearchOpportunity
from .serializers import ProfessorSerializer, ResearchOpportunitySerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ResearchOpportunityViewSet(viewsets.ModelViewSet):
    queryset = ResearchOpportunity.objects.all()
    serializer_class = ResearchOpportunitySerializer


