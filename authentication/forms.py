from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    username = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control'
    })))
    password = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control'
    })))
    confirm_password = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control'
    })))
    email = forms.EmailField(widget=(forms.TextInput(attrs={
        'class': 'form-control'
    })))
    confirm_email = forms.EmailField(widget=(forms.TextInput(attrs={
        'class': 'form-control'
    })))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError('Username already exists!')
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise ValidationError('Password don`t match!')
        return confirm_password

    def clean_confirm_email(self):
        email = self.cleaned_data['email'].lower()
        confirm_email = self.cleaned_data['confirm_email'].lower()
        if email and confirm_email and email != confirm_email:
            raise ValidationError('Email don`t match!')
        r = User.objects.filter(email=confirm_email)
        if r.count():
            raise ValidationError('Email already exists!')
        return confirm_email

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['confirm_password'],
            self.cleaned_data['confirm_email']
        )
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=(forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'your username',
        'title': "Please enter you username"
    })))
    password = forms.CharField(widget=(forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': '********',
        'title': "Please enter you password"
    })))
