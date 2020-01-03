from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    established = models.DateField()
    photo = models.ImageField(upload_to='faculty/')
    about = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
