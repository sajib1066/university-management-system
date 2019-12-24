from django.shortcuts import render
from .forms import FacultyForm

def add_faculty(request):
    forms = FacultyForm()
    context = {
        'forms': forms
    }
    return render(request, 'faculty/add-faculty.html', context)
