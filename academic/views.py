from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty

def add_faculty(request):
    forms = FacultyForm()
    if request.method == 'POST':
        forms = FacultyForm(request.POST)
        print(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            established = forms.cleaned_data['established']
            photo = forms.cleaned_data['photo']
            about = forms.cleaned_data['about']
            Faculty.objects.create(name=name, established=established, photo=photo, about=about, status=False)
            return redirect('home')

    context = {
        'forms': forms
    }
    return render(request, 'faculty/add-faculty.html', context)
