from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Professor, ResearchOpportunity

admin.site.register(Professor)
admin.site.register(ResearchOpportunity)