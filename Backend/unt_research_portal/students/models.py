from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True, default="")
    year = models.CharField(max_length=20, default="")  # E.g., 'Sophomore', 'Graduate'
    skills = models.TextField(max_length=20, default="")  # Use JSONField if storing structured skills data
    resume = models.FileField(upload_to='resumes/', default="")  # For resume uploads

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# class Student(models.Model):
#     first_name = models.CharField(max_length=100, default="")
#     last_name = models.CharField(max_length=100, default="")
#     address = models.CharField(max_length=100, default="")
#     department = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     research_interests = models.TextField(null=True, blank=True)  # List of research interests
#     profile_picture = models.ImageField(upload_to='professors_pics/', null=True, blank=True)  # Profile picture upload
#     key_words = models.CharField(max_length=100, default="Machine Learning")