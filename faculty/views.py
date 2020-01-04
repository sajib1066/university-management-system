from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty

def add_faculty(request):
    forms = FacultyForm()
    if request.method == 'POST':
        forms = FacultyForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('faculty-list')

    context = {
        'forms': forms
    }
    return render(request, 'faculty/add-faculty.html', context)

def faculty_list(request):
    faculty = Faculty.objects.all()
    context = {
        'faculty': faculty
    }
    return render(request, 'faculty/faculty-list.html', context)
