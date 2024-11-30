from rest_framework import serializers
from .models import COIStaff

class COIStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = COIStaff
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'position', 'office_location']
