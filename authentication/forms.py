from django import forms

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
