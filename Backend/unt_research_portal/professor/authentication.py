# test by new gpt code()
from django.contrib.auth.backends import BaseBackend
from .models import Professor

class ProfessorBackend(BaseBackend):
    def authenticate(self, request=None, email=None, password=None, **kwargs):
        try:
            professor = Professor.objects.get(email=email)
            # if Professor.check_password('sharad@123'):
            if professor.password == password:
                return professor
        except Professor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Professor.objects.get(pk=user_id)
        except Professor.DoesNotExist:
            return None
# test by new gpt code(ends)