from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    ats_score = models.FloatField()

    def __str__(self):
        return self.name

class Resume(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name}'s Resume"

class ResearchOpportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.TextField()
    posted_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class COIDeanAction(models.Model):
    dean = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)  # e.g., 'Viewed Resume', 'Matched Opportunity'
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dean.username} - {self.action_type}"

