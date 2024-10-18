from django import forms
from .models import ResearchPosition

class ResearchPositionForm(forms.ModelForm):
    class Meta:
        model = ResearchPosition
        fields = ['title', 'description', 'eligibility_criteria', 'deadline']