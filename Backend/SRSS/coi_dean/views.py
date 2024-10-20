from django.shortcuts import render
from .models import Student, Resume, ResearchOpportunity, COIDeanAction

def browse_resumes(request):
    resumes = Resume.objects.all()
    return render(request, 'coi_dean/browse_resumes.html', {'resumes': resumes})

def view_student_profile(request, student_id):
    student = Student.objects.get(id=student_id)
    research_opportunities = ResearchOpportunity.objects.filter(skills_required__icontains=student.program)
    COIDeanAction.objects.create(dean=request.user, action_type="Viewed Resume", student=student)
    return render(request, 'coi_dean/student_profile.html', {'student': student, 'research_opportunities': research_opportunities})

def search_research_opportunities(request):
    opportunities = ResearchOpportunity.objects.all()
    if request.method == 'POST':
        keyword = request.POST['keyword']
        opportunities = opportunities.filter(title__icontains=keyword)
        COIDeanAction.objects.create(dean=request.user, action_type="Searched Opportunities")
    return render(request, 'coi_dean/search_opportunities.html', {'opportunities': opportunities})
