from django.contrib import admin
from .models import Professor, ResearchOpportunity, StudentApplication

# test
from django.core.exceptions import ValidationError

# Register your models here.
# admin.site.register(Professor)


# test admin panel
from django.contrib import admin

admin.site.register(ResearchOpportunity)
admin.site.register(StudentApplication)



class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'title')
    fields = ('first_name', 'last_name', 'email', 'password', 'department', 'title', 
              'office_location', 'phone_number', 'research_interests', 'profile_picture', 
              'publications', 'posted_opportunities_count')
    readonly_fields = ('posted_opportunities_count',)

# test binod gpt
# @admin.register(Professor)
# class ProfessorAdmin(admin.ModelAdmin):
#     list_display = ['user', 'department', 'phone_number', 'office_location']
#     search_fields = ['user__first_name', 'user__last_name', 'department']
# test ends

admin.site.register(Professor, ProfessorAdmin)


# def save_model(self, request, obj, form, change):
#         # Check for existing email
#         if Professor.objects.filter(email=obj.email).exclude(pk=obj.pk).exists():
#             raise ValidationError(f"A professor with email {obj.email} already exists.")
#         # Hash the password before saving
#         if 'password' in form.changed_data:
#             obj.set_password(form.cleaned_data['password'])
#         super().save_model(request, obj, form, change)
