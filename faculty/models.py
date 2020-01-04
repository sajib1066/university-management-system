from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    established = models.DateField()
    about = models.TextField()
    status_choice = (
        ('active', 'Active'),
        ('disabled', 'Disabled'),
        ('paused', 'Paused')
    )
    status = models.CharField(choices=status_choice, max_length=15)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
