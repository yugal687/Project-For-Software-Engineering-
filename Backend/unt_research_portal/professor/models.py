from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from unt_research_portal import settings


from students.models import Student



# class ProfessorManager(BaseUserManager):
#     def create_professor(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username must be set')
#         professor = self.model(username=username, **extra_fields)
#         professor.set_password(password)
#         professor.save(using=self._db)
#         return professor



class Professor(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile', default=1)
    # username = models.CharField(max_length=255, unique=True, null=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile', default="")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
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
    
    # objects = ProfessorManager()
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    # USERNAME_FIELD = 'email'

    # objects = ProfessorManager()

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name} ({self.email})"

    def increment_opportunity_count(self):
        """Call this method whenever a professor posts a new research opportunity."""
        self.posted_opportunities_count += 1
        self.save()
    
    # def set_password(self, password):
    #     self.password = make_password(password)
    
    # def check_password(self, password):
    #     return check_password(password, self.password)

    @property
    def research_posts(self):
        """Return all research opportunities created by this professor."""
        return self.research_opportunities.all()
    
    

   

class ResearchOpportunity(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='research_opportunities')
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=100, default="")
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()  # Add a deadline field
    is_active = models.BooleanField(default=True)  # Flag to mark if opportunity is still active
    required_skills = models.TextField(null=True, blank=True)  # List of required skills for students
    research_tags = models.CharField(max_length=255, null=True, blank=True)  # Tags for the research (comma-separated)
    max_applications = models.IntegerField(default=10)  # Limit the number of applications
    current_applications = models.IntegerField(default=0)  # Track current applications
    

    @property
    def students_applied(self):
        """Return all applications applied by this students."""
        return self.applications.all()
    

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

# class Student_Application_For_Professor(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_applications_for_professors")
#     research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE, related_name="applications")
#     applied_at = models.DateTimeField(auto_now_add=True)
#     resume = models.FileField(upload_to='student_resumes/', null=True, blank=True)  # Resume upload
    

#     def __str__(self):
#         return f"{self.student.first_name} {self.student.last_name} applied for {self.research_opportunity.title}"

class StudentApplication(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_applications_for_professors")
    research_opportunity = models.ForeignKey(ResearchOpportunity, on_delete=models.CASCADE, related_name="applications")
    applied_at = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='student_resumes/', null=True, blank=True)  # Resume upload
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )
    

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} applied for {self.research_opportunity.title}"
    
   



