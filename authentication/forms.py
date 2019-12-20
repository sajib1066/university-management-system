from django import forms

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
