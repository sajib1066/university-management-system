from django import forms
from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'faculty': forms.Select(attrs={'class': 'form-control'}),
            'name_of_head': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Head of Department'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'opening_date': forms.SelectDateWidget()
        }
