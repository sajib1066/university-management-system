from django.shortcuts import render, redirect
from .forms import DepartmentForm

def add_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'department/add-department.html', context)
