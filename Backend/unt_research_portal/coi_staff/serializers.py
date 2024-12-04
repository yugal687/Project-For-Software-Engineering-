from rest_framework import serializers
from .models import COIStaff
from django.contrib.auth.hashers import check_password
from .models import CoiDocuments


class COIStaffLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            staff = COIStaff.objects.get(email=email)
        except COIStaff.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        # Validate password using check_password
        if not check_password(password, staff.password):
            raise serializers.ValidationError("Invalid email or password")

        return staff

class COIStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = COIStaff
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'position', 'office_location']
        
        


class CoiDocumentsSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    research_opportunity_title = serializers.CharField(source='research_opportunity.title', read_only=True)

    class Meta:
        model = CoiDocuments
        fields = [
            'id', 'student', 'student_name', 'research_opportunity', 'research_opportunity_title',
            'consent_form', 'nda_acknowledged', 'student_unt_id', 'transcript', 'recommendation_letter',
            'onboarding_status', 'updated_at'
        ]
        read_only_fields = ['updated_at', 'student_name', 'research_opportunity_title']

    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"

