from django.shortcuts import render
from rest_framework import generics
from .models import JobPosting
from .serializers import JobPostingSerializer
# Create your views here.
class JobPostingListCreateView(generics.ListCreateAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class JobPostingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer