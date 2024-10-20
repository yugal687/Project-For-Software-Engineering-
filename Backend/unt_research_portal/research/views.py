from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm, StudentRegistrationForm, ProfessorRegistrationForm, COIStaffRegistrationForm, SuperAdminRegistrationForm

def home(request):
    return render(request, 'home.html')

# Student Registration View
def register_student(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        student_form = StudentRegistrationForm()
    return render(request, 'register_student.html', {'user_form': user_form, 'student_form': student_form})

# Professor Registration View
def register_professor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        professor_form = ProfessorRegistrationForm(request.POST)
        if user_form.is_valid() and professor_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            professor = professor_form.save(commit=False)
            professor.user = user
            professor.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        professor_form = ProfessorRegistrationForm()
    return render(request, 'register_professor.html', {'user_form': user_form, 'professor_form': professor_form})

# COI Staff Registration View
def register_coi_staff(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        staff_form = COIStaffRegistrationForm(request.POST)
        if user_form.is_valid() and staff_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            staff = staff_form.save(commit=False)
            staff.user = user
            staff.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        staff_form = COIStaffRegistrationForm()
    return render(request, 'register_coi_staff.html', {'user_form': user_form, 'staff_form': staff_form})

# Super Admin Registration View
def register_super_admin(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        admin_form = SuperAdminRegistrationForm(request.POST)
        if user_form.is_valid() and admin_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.is_superuser = True  # Super Admin has superuser privileges
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
        admin_form = SuperAdminRegistrationForm()
    return render(request, 'register_super_admin.html', {'user_form': user_form, 'admin_form': admin_form})






# from .text_processing import process_text, extract_entities

# # Create your views here.

# def analyze_text_view(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('text')  # Get the text input from the form

#         tokens = process_text(input_text)  # Process the text for tokens
#         entities = extract_entities(input_text)  # Extract entities from the text

#         return render(request, 'research/results.html', {
#             'tokens': tokens,
#             'entities': entities,
#             'input_text': input_text
#         })
    
#     return render(request, 'research/text_input.html')
    
#     return render(request, 'text_input.html')

