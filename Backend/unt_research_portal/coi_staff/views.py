from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import COIStaff
from .serializers import COIStaffSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.middleware.csrf import get_token


# Create your views here.



class COIStaffLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            staff = COIStaff.objects.get(email=email)
        except COIStaff.DoesNotExist:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Validate password
        if not check_password(password, staff.password):
            return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        request.session['coi_staff_id'] = staff.id
        return Response({
            "message": "Login successful",
            "staff_id": staff.id,
            "staff_name": f"{staff.first_name} {staff.last_name}"
        })

class COIStaffDashboardView(APIView):
    def get(self, request):
        staff_id = request.session.get('coi_staff_id')
        if not staff_id:
            return Response({"error": "Not authenticated. Please log in first."}, status=status.HTTP_401_UNAUTHORIZED)

        try:
            staff = COIStaff.objects.get(id=staff_id)
            serializer = COIStaffSerializer(staff)
            return Response({
                "message": f"Welcome, {staff.first_name}!",
                "staff_data": serializer.data
            }, status=status.HTTP_200_OK)
        except COIStaff.DoesNotExist:
            return Response({"error": "Staff not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})
