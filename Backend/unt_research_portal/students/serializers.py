# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
        
# from rest_framework import serializers
# from .models import Student

# class StudentLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
#         try:
#             student = Student.objects.get(email=email)
#         except Student.DoesNotExist:
#             raise serializers.ValidationError("Invalid email or password")

#         # Directly compare raw passwords (for testing purposes)
#         if student.password != password:
#             raise serializers.ValidationError("Invalid email or password")

#         return student


# Using Session Authentication

from rest_framework import serializers
from .models import Student
from django.contrib.auth.hashers import make_password, check_password
from professor.models import ResearchOpportunity


class StudentSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'email', 'first_name', 'last_name', 'full_name', 'major', 'gpa']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Validate password
        if not check_password(password, student.password):
            raise serializers.ValidationError("Invalid email or password")

        return student

class StudentRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in the API response

    class Meta:
        model = Student
        fields = ['email', 'password', 'first_name', 'last_name', 'major', 'gpa']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        return super().create(validated_data)
    
class ResearchOpportunityStudentSerializer(serializers.ModelSerializer):
    professor_name = serializers.SerializerMethodField()

    class Meta:
        model = ResearchOpportunity
        fields = ['id', 'title', 'description', 'deadline', 'required_skills', 'research_tags', 'professor_name']

    def get_professor_name(self, obj):
        return f"{obj.professor.first_name} {obj.professor.last_name}"
    
    

class StudentResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'resume']  # Include resume field


