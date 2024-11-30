from rest_framework import serializers
from .models import Professor, ResearchOpportunity, Student_Application
# from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# test
class ApplicationSerializer(serializers.ModelSerializer):
    # students_applied = ResearchOpportunitySerializer(many=True, read_only=True)
    # test
    student_name = serializers.SerializerMethodField()
    class Meta:
        model = Student_Application
        fields = '__all__'

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

class ResearchOpportunitySerializer(serializers.ModelSerializer):
    students_applied = ApplicationSerializer(many=True, read_only=True)

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
            # user = User.objects.get(email=email)
        except professor.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")
        
        if not professor.check_password(password):
            raise serializers.ValidationError("Invalid email or password")

        # if not hasattr(professor, 'professor_profile'):
        #     raise serializers.ValidationError("User is not a professor")


        # if not professor.check_password(password):
        #     raise serializers.ValidationError("Invalid email or password")
        # test
        # if professor.password != password:
        #     raise serializers.ValidationError("Invalid email or password")

        # return user
        return professor
    
    
class ProfessorDashboardSerializer(serializers.ModelSerializer):
    """
    Serializer for dashboard data of the professor.
    """
    # research_opportunities = serializers.SerializerMethodField()
    # research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

    class Meta:
        model = Professor
        fields = "__all__"

    # def get_research_opportunities(self, obj):
    #     opportunities = obj.research_opportunities.all()
    #     return [{
    #         "title": opp.title,
    #         "description": opp.description,
    #         "deadline": opp.deadline,
    #         "applications": opp.current_applications
    #     } for opp in opportunities]

# class ProfessorDetailSerializer(serializers.ModelSerializer):
#     research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

#     class Meta:
#         model = Professor
#         fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     # Add professor email to the token payload
    #     professor = Professor.objects.get(email=self.user.email)
    #     data['professor_email'] = professor.email
    #     return data

    def validate(self, attrs):
        data = super().validate(attrs)
        email = attrs.get("email")

        try:
            professor = Professor.objects.get(email=email)
        except Professor.DoesNotExist:
            # raise AuthenticationFailed("Invalid professor credentials.")
            print('No Professor')
        # Add professor_email to the token payload
        data['professor_email'] = professor.email
        return data