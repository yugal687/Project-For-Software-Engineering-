from django import forms
from .models import ResearchOpportunity, Professor
from django.contrib.auth.models import User

class ResearchOpportunityForm(forms.ModelForm):
    class Meta:
        model = ResearchOpportunity
        fields = ['title', 'description', 'deadline', 'is_active', 'required_skills', 'research_tags', 'max_applications']



class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['department', 'title', 'office_location'] 


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfessorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['first_name', 'title', 'department', 'office_location', 'phone_number', 'research_interests']

