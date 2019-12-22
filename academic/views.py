from django.shortcuts import render

def add_faculty(request):
    return render(request, 'faculty/add-faculty.html')
