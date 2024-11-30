from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

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
    last_login = models.DateTimeField(null=True, blank=True)  # Last login timestamp
    created_by = models.CharField(max_length=100, null=True, blank=True)  # Name of admin who created the account
    
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

    def update_last_login(self):
        """Update last login timestamp."""
        self.last_login = timezone.now()
        self.save()
