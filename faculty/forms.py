from django import forms
from .models import Faculty

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
            'established': forms.SelectDateWidget(),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "About"})
        }