from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import COIStaff, CoiDocuments
from .serializers import COIStaffSerializer
from django.contrib.auth.hashers import make_password, check_password
from django.middleware.csrf import get_token

from professor.models import ResearchOpportunity, Student_Application
from students.models import StudentApplication
from professor.serializers import ResearchOpportunitySerializer, ApplicationSerializer
from students.serializers import StudentApplicationSerializer
from .serializers import CoiDocumentsSerializer
from django.core.mail import send_mail
from django.conf import settings
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
        accepted_applications = Student_Application.objects.filter(status='accepted').count()
        rejected_applications = Student_Application.objects.filter(status='rejected').count()

        return Response({
            "overview": {
                "total_opportunities": total_opportunities,
                "total_applications": total_applications,
                "pending_applications": pending_applications,
                "accepted_applications": accepted_applications,
                "rejected_applications": rejected_applications,
            },
            "opportunities": opportunities_serializer.data,
            "applications": applications_serializer.data,
        }, status=status.HTTP_200_OK)

        

class CSRFTokenView(APIView):
    def get(self, request):
        csrf_token = get_token(request)
        return Response({"csrfToken": csrf_token})
    
    

# class ManageDocumentsView(APIView):
#     def get(self, request):
#         """Retrieve documentation status for all accepted applications."""
#         accepted_applications = Student_Application.objects.filter(status="accepted")
#         coi_documents = CoiDocuments.objects.filter(student__in=[app.student for app in accepted_applications])

#         serializer = CoiDocumentsSerializer(coi_documents, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         """Create or update documentation for a student."""
#         serializer = CoiDocumentsSerializer(data=request.data)
#         if serializer.is_valid():
#             # Create or update the document record
#             document, created = CoiDocuments.objects.update_or_create(
#                 student_id=serializer.validated_data['student'].id,
#                 research_opportunity_id=serializer.validated_data['research_opportunity'].id,
#                 defaults=serializer.validated_data
#             )
            
#         # Send notification if status is 'pending'
#             if serializer.validated_data.get('status') == 'pending':
#                 student_email = document.student.email
#                 self.send_email_notification(
#                     email=student_email,
#                     student_name=f"{document.student.first_name} {document.student.last_name}",
#                     opportunity_title=document.research_opportunity.title
#                 )    
#             return Response({"message": "Documentation updated successfully"}, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#     @staticmethod
#     def send_email_notification(email, student_name, opportunity_title):
#         """Send an email notification to the student."""
#         subject = "Reminder: Submit Required Documents"
#         message = f"""
#         Dear {student_name},

#         This is a reminder to submit your required documents for the research opportunity titled "{opportunity_title}".

#         Please ensure you submit the following documents:
#         - Consent Form
#         - Student Identification
#         - Transcript
#         - Recommendation Letters
#         - Non-Disclosure Agreement (NDA)

#         You can upload these documents through your student dashboard.

#         Thank you,
#         COI Staff
#         """
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[email],
#             fail_silently=False
#         )


class ViewSubmittedDocumentsView(APIView):
    def get(self, request):
        """View all documents submitted for accepted applications."""
        accepted_applications = StudentApplication.objects.filter(status="accepted")
        serializer = StudentApplicationSerializer(accepted_applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
