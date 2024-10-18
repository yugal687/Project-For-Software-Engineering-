from django.db import models
from django.contrib.auth.models import User

class ResearchPosition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title