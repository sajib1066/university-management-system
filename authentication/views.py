from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def user_registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    # forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Account created successfully!') # don`t sure how it works?
            return redirect('home')
    else:
        forms = RegistrationForm()
    context = {
        'forms': forms
    }
    return render(request, 'auth/registration.html', context)

def user_login(request):
    pass_err = ''
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                pass_err = 'Password don`t match!'
    else:
        forms = LoginForm()
    context = {
        'forms': forms,
        'pass_err': pass_err
    }
    return render(request, 'auth/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')
