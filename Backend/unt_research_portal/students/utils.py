from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_student(student):
    refresh = RefreshToken()
    refresh['email'] = student.email
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
