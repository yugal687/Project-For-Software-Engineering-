from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
from rest_framework import serializers
from .models import Student

class StudentLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Directly compare raw passwords (for testing purposes)
        if student.password != password:
            raise serializers.ValidationError("Invalid email or password")

        return student

