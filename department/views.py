from django.shortcuts import render

def add_department(request):
    context = {
        
    }
    return render(request, 'department/add-department.html', context)
