from rest_framework import serializers
from .models import COIStaff
from django.contrib.auth.hashers import check_password


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
