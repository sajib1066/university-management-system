from django.db import models
from department.models import Department
from address.models import Country, State, City

class Designation(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='professor/')
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    postcode = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    about = models.TextField()
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(choices=gender_choice, max_length=6)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    website = models.URLField(blank=True, null=True)
    join_date = models.DateField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
