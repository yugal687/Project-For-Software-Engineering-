# from rest_framework import serializers
# from .models import Professor, ResearchOpportunity

# class ProfessorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Professor
#         fields = '__all__'

# class ResearchOpportunitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResearchOpportunity
#         fields = '__all__'


# from rest_framework import serializers
# from .models import Professor, ResearchOpportunity

# class ResearchOpportunitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ResearchOpportunity
#         fields = '__all__'

# class ProfessorSerializer(serializers.ModelSerializer):
#     research_opportunities = ResearchOpportunitySerializer(many=True, read_only=True)

#     class Meta:
#         model = Professor
#         fields = '__all__'


from rest_framework import serializers
from .models import Professor, ResearchOpportunity

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class ResearchOpportunitySerializer(serializers.ModelSerializer):
    professor_name = serializers.CharField(source='professor.__str__', read_only=True)

    class Meta:
        model = ResearchOpportunity
        fields = '__all__'
