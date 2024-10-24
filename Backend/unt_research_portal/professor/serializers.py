from rest_framework import serializers
from .models import Professor, ResearchOpportunity

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class ResearchOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchOpportunity
        fields = '__all__'