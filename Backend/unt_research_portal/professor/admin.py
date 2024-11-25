from django.contrib import admin
from .models import Professor, ResearchOpportunity

# test
from django.core.exceptions import ValidationError

# Register your models here.
# admin.site.register(Professor)
admin.site.register(ResearchOpportunity)

# test admin panel
from django.contrib import admin
from .models import Professor

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'title')
    fields = ('first_name', 'last_name', 'email', 'password', 'department', 'title', 
              'office_location', 'phone_number', 'research_interests', 'profile_picture', 
              'publications', 'posted_opportunities_count')
    readonly_fields = ('posted_opportunities_count',)

# def save_model(self, request, obj, form, change):
#         # Check for existing email
#         if Professor.objects.filter(email=obj.email).exclude(pk=obj.pk).exists():
#             raise ValidationError(f"A professor with email {obj.email} already exists.")
#         # Hash the password before saving
#         if 'password' in form.changed_data:
#             obj.set_password(form.cleaned_data['password'])
#         super().save_model(request, obj, form, change)

admin.site.register(Professor, ProfessorAdmin)