from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True, default="")
    year = models.CharField(max_length=20, default="")  # E.g., 'Sophomore', 'Graduate'
    skills = models.TextField(max_length=20, default="")  # Use JSONField if storing structured skills data
    resume = models.FileField(upload_to='resumes/', default="", blank=True, null=True)  # For resume uploads

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

