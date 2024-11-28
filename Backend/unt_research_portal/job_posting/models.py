from django.db import models

# Create your models here.
class JobPosting(models.Model):
    opportunity_id = models.AutoField(primary_key=True)
    professor_id = models.IntegerField() 
    title = models.CharField(max_length=200)
    description = models.TextField()
    department = models.CharField(max_length=100)
    eligibility_criteria = models.TextField()
    required_skills = models.TextField()
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title