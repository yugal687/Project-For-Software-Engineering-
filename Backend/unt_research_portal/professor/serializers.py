from rest_framework import serializers
from .models import Professor, ResearchOpportunity

class ResearchOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchOpportunity
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            professor = Professor.objects.get(email=email)
        except Professor.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # if not professor.check_password(password):
        #     raise serializers.ValidationError("Invalid email or password")
        # test
        if professor.password != password:
            raise serializers.ValidationError("Invalid email or password")

        return professor

# class ProfessorDetailSerializer(serializers.ModelSerializer):
#     research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

#     class Meta:
#         model = Professor
#         fields = '__all__'