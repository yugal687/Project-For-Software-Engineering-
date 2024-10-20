from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    major = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.user.username

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# COI Staff Model
class COIStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_role = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

# Super Admin Model
class SuperAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class ResearchOpportunity(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Resume(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username}'s Resume"

class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.student.user.username} applied for {self.research_opportunity.title}"
