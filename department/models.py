from django.db import models
from faculty.models import Faculty

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name_of_head = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    status_choice = (
        ('active', 'Active'),
        ('disabled', 'Disabled'),
        ('paused', 'Paused')
    )
    status = models.CharField(choices=status_choice, max_length=20)
    opening_date = models.DateField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
