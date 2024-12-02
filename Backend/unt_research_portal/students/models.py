# Yugal's Code
# from django.db import models

# # Create your models here.
# class Student(models.Model):
#     first_name = models.CharField(max_length=50, default="")
#     last_name = models.CharField(max_length=50, default="")
#     email = models.EmailField(max_length=50, unique=True, default="", blank=False)
#     password = models.CharField(max_length=128, default="", blank=False) 
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     year = models.CharField(max_length=20, default="")  # E.g., 'Sophomore', 'Graduate'
#     address = models.TextField(null=True, blank=True)
#     resume = models.FileField(upload_to='student_resumes/', null=True, blank=True)  # Resume upload
#     profile_picture = models.ImageField(upload_to='student_profile_pics/', null=True, blank=True)  # Profile picture
#     skills = models.TextField(null=True, blank=True)  # Comma-separated skills
#     gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
#     major = models.CharField(max_length=100, null=True, blank=True)  # Student's field of study
#     graduation_year = models.IntegerField(null=True, blank=True)  # Expected graduation year
#     certifications = models.TextField(null=True, blank=True)  # Certifications (comma-separated)
#     linked_in_profile = models.URLField(null=True, blank=True)  # LinkedIn profile link
#     portfolio_website = models.URLField(null=True, blank=True)  # Personal portfolio link
#     github_profile = models.URLField(null=True, blank=True)  # GitHub profile link
#     # created_at = models.DateTimeField(auto_now_add=True, default="")  # Account creation date
#     # updated_at = models.DateTimeField(auto_now=True, default="")  # Last profile update

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}  ({self.email})"


# Binod's code
from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, unique=True, default="", blank=False)
    password = models.CharField(max_length=128, default="", blank=False) 
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    year = models.CharField(max_length=20, default="")  # E.g., 'Sophomore', 'Graduate'
    address = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='student_resumes/', null=True, blank=True)  # Resume upload
    profile_picture = models.ImageField(upload_to='student_profile_pics/', null=True, blank=True)  # Profile picture
    skills = models.TextField(null=True, blank=True)  # Comma-separated skills
    gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)  # Student's field of study
    graduation_year = models.IntegerField(null=True, blank=True)  # Expected graduation year
    certifications = models.TextField(null=True, blank=True)  # Certifications (comma-separated)
    linked_in_profile = models.URLField(null=True, blank=True)  # LinkedIn profile link
    portfolio_website = models.URLField(null=True, blank=True)  # Personal portfolio link
    github_profile = models.URLField(null=True, blank=True)  # GitHub profile link
    # created_at = models.DateTimeField(auto_now_add=True, default="")  # Account creation date
    # updated_at = models.DateTimeField(auto_now=True, default="")  # Last profile update
    
    def save(self, *args, **kwargs):
        # Hash the password if it's not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}  ({self.email})"
