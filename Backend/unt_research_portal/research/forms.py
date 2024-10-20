from django import forms
from django.contrib.auth.models import User
from .models import Student, Professor, COIStaff, SuperAdmin

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['major', 'year']

class ProfessorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['department']

class COIStaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = COIStaff
        fields = ['staff_role']

class SuperAdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = SuperAdmin
        fields = []