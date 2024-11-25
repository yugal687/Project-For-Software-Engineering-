from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class Professor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile', default="")
    email = models.EmailField(max_length=100, unique=True, default="", blank=False)
    password = models.CharField(max_length=128)  # Store hashed passwords
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100)
    title = models.CharField(max_length=50)  # e.g., Professor, Assistant Professor
    office_location = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    research_interests = models.TextField(null=True, blank=True)  # List of research interests
    profile_picture = models.ImageField(upload_to='professors_pics/', null=True, blank=True)  # Profile picture upload
    publications = models.TextField(null=True, blank=True)  # List of publications
    posted_opportunities_count = models.IntegerField(default=0)  # Track the number of research opportunities posted
    

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} ({self.email})"

    def increment_opportunity_count(self):
        """Call this method whenever a professor posts a new research opportunity."""
        self.posted_opportunities_count += 1
        self.save()
    
    # def set_password(self, raw_password):
    #     self.password = make_password(raw_password)
    
    # def check_password(self, raw_password):
    #     return check_password(raw_password, self.password)

    @property
    def research_posts(self):
        """Return all research opportunities created by this professor."""
        return self.research_opportunities.all()

   

class ResearchOpportunity(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='research_opportunities')
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()  # Add a deadline field
    is_active = models.BooleanField(default=True)  # Flag to mark if opportunity is still active
    required_skills = models.TextField(null=True, blank=True)  # List of required skills for students
    research_tags = models.CharField(max_length=255, null=True, blank=True)  # Tags for the research (comma-separated)
    max_applications = models.IntegerField(default=10)  # Limit the number of applications
    current_applications = models.IntegerField(default=0)  # Track current applications
    

    def __str__(self):
        return self.title

    def has_passed_deadline(self):
        return timezone.now() > self.deadline

    def increment_application_count(self):
        """Call this method whenever a student applies."""
        if self.current_applications < self.max_applications:
            self.current_applications += 1
            self.save()
        else:
            self.is_active = False
            self.save()

    def tag_list(self):
        """Return the tags as a list."""
        return self.research_tags.split(",") if self.research_tags else []
