from django.contrib import admin
from .models import Student, ResearchOpportunity, Resume,Application, Professor, COIStaff, SuperAdmin


# Register your models here.

admin.site.register(Student)
admin.site.register(ResearchOpportunity)
admin.site.register(Resume)
admin.site.register(Application)
admin.site.register(Professor)
admin.site.register(COIStaff)
admin.site.register(SuperAdmin)



