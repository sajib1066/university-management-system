from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            email = forms.cleaned_data['email']
            confirm_email = forms.cleaned_data['confirm_email']
            if password == confirm_password and email == confirm_email:
                User.objects.create_user(
                    username=username,
                    password=password,
                    email = email
                )
                user = authenticate(username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
            else:
                print('Data not matched!')
    context = {
        'forms': forms
    }
    return render(request, 'auth/registration.html', context)

def user_login(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {
        'forms': forms
    }
    return render(request, 'auth/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
