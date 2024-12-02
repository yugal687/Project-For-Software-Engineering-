# test by new gpt code()
from django.contrib.auth.backends import BaseBackend
from .models import Student

class StudentBackend(BaseBackend):
    def authenticate(self, request=None, email=None, password=None, **kwargs):
        try:
            student = Student.objects.get(email=email)
            # if Professor.check_password('sharad@123'):
            if student.password == password:
                return student
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
# test by new gpt code(ends)