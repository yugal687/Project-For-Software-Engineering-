from rest_framework import serializers
from .models import Professor, ResearchOpportunity, Student_Application
from django.contrib.auth.hashers import make_password, check_password


# test
class ApplicationSerializer(serializers.ModelSerializer):
    # students_applied = ResearchOpportunitySerializer(many=True, read_only=True)
    student_name = serializers.SerializerMethodField()
    research_opportunity_title = serializers.CharField(source='research_opportunity.title', read_only=True)


    class Meta:
        model = Student_Application
        fields = ['id', 'student', 'student_name', 'research_opportunity', 'research_opportunity_title', 'applied_at', 'status']
        read_only_fields = ['id', 'applied_at', 'status']
    
    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

class ResearchOpportunitySerializer(serializers.ModelSerializer):
    students_applied = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = ResearchOpportunity
        fields = '__all__'
        
class ResearchOpportunityStudentSerializer(serializers.ModelSerializer):
    # students_applied = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = ResearchOpportunity
        fields = ['id', "title", "description", "posted_on", "deadline", "required_skills"]

# class ProfessorSerializer(serializers.ModelSerializer):
#     research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

#     class Meta:
#         model = Professor
#         fields = 
class ProfessorSerializer(serializers.ModelSerializer):
    # research_posts = ResearchOpportunitySerializer(many=True, read_only=True)
    # full_name = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = '__all__'
    # def get_full_name(self, obj):
        # return f"{obj.first_name} {obj.last_name}"

# Using session
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

        # Validate password
        if not check_password(password, professor.password):
            raise serializers.ValidationError("Invalid email or password")
        
        # # test
        # if professor.password != password:
        #     raise serializers.ValidationError("Invalid email or password")

        return professor

# class ProfessorDetailSerializer(serializers.ModelSerializer):
#     research_posts = ResearchOpportunitySerializer(many=True, read_only=True)

#     class Meta:
#         model = Professor
#         fields = '__all__'