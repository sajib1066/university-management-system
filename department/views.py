from django.shortcuts import render, redirect
from .forms import DepartmentForm
from .models import Department

def add_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('department-list')
    context = {
        'form': forms
    }
    return render(request, 'department/add-department.html', context)

def department_list(request):
    department = Department.objects.all()
    context = {
        'department': department
    }
    return render(request, 'department/department-list.html', context)

def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    forms = DepartmentForm(instance=department)
    if request.method == 'POST':
        forms = DepartmentForm(request.POST, instance=department)
        if forms.is_valid():
            forms.save()
            return redirect('department-list')
    context = {
        'form': forms
    }
    return render(request, 'department/edit-department.html', context)
