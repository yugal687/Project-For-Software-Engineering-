from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.hashers import make_password
from students.models import Student
from professor.models import ResearchOpportunity

class COIStaff(models.Model):
    email = models.EmailField(unique=True)  # Unique email for authentication
    password = models.CharField(max_length=128)  # Store hashed passwords
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    position = models.CharField(max_length=100, default="COI Staff")  # Staff position or title
    office_location = models.CharField(max_length=255, null=True, blank=True)  # Office location on campus
    profile_picture = models.ImageField(upload_to='coi_staff_pics/', null=True, blank=True)  # Staff profile picture
    date_joined = models.DateField(auto_now_add=True)  # Date when the staff member joined
    is_active = models.BooleanField(default=True)  # Active/inactive status
    responsibilities = models.TextField(null=True, blank=True)  # Description of responsibilities
    managed_departments = models.TextField(null=True, blank=True)  # Departments managed by the staff (comma-separated)
    notifications_enabled = models.BooleanField(default=True)  # Notification preferences
    # last_login = models.DateTimeField(null=True, blank=True)  # Last login timestamp
    # created_by = models.CharField(max_length=100, null=True, blank=True)  # Name of admin who created the account
    
    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    def toggle_active_status(self):
        """Activate or deactivate staff account."""
        self.is_active = not self.is_active
        self.save()
        
        
class CoiDocuments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="coi_documents")
    research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE, related_name="coi_documents")
    
    # # Documentation Fields
    # consent_form = models.TextField(null=True, blank=True)  # Filled by COI staff
    # nda_acknowledged = models.BooleanField(default=False)  # Student acknowledgment
    student_unt_id = models.FileField(upload_to='coi_documents/student_ids/', null=True, blank=True)
    transcript = models.FileField(upload_to='coi_documents/transcripts/', null=True, blank=True)
    recommendation_letter = models.FileField(upload_to='coi_documents/recommendation_letters/', null=True, blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    onboarding_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Track overall status
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"COI Documents for {self.student.first_name} - {self.research_opportunity.title}"

    
