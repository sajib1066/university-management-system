from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.state_name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.city_name
