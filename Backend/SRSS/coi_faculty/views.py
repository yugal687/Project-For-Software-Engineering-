# C:\Users\simmo\Downloads\Project-For-Software-Engineering-\backend\SRSS\coi_faculty\views.py
from django.shortcuts import render, redirect
from .models import ResearchPosition
from .forms import ResearchPositionForm

def position_list(request):
    positions = ResearchPosition.objects.all()
    return render(request, 'coi_faculty/position_list.html', {'positions': positions})

def post_position(request):
    if request.method == 'POST':
        form = ResearchPositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = ResearchPositionForm()
    return render(request, 'coi_faculty/post_position.html', {'form': form})