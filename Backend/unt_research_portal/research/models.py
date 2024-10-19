from django.db import models

# Create your models here.

# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name
    

# Research Opportunity model
class ResearchOpportunity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    professor = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


# Resume model
class Resume(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name}'s Resume"
    
# Application model
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} applied for {self.research_opportunity.title}"