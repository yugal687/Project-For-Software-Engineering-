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

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from professor.models import ResearchOpportunity, Student_Application
from professor.serializers import ResearchOpportunitySerializer, ApplicationSerializer

class COIStaffDashboardView(APIView):
    def get(self, request):
        # Query parameters for filtering
        status_filter = request.query_params.get('status', None)
        opportunity_id = request.query_params.get('opportunity_id', None)

        # Research opportunities overview
        opportunities = ResearchOpportunity.objects.all()
        opportunities_serializer = ResearchOpportunitySerializer(opportunities, many=True)

        # Applications filtering logic
        applications = Student_Application.objects.all()
        if status_filter:
            applications = applications.filter(status=status_filter)
        if opportunity_id:
            applications = applications.filter(research_opportunity_id=opportunity_id)

        applications_serializer = ApplicationSerializer(applications, many=True)

        # Statistics
        total_opportunities = ResearchOpportunity.objects.count()
        total_applications = Student_Application.objects.count()
        pending_applications = Student_Application.objects.filter(status='pending').count()

        return Response({
            "overview": {
                "total_opportunities": total_opportunities,
                "total_applications": total_applications,
                "pending_applications": pending_applications,
            },
            "opportunities": opportunities_serializer.data,
            "applications": applications_serializer.data,
        }, status=status.HTTP_200_OK)

        

class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})
