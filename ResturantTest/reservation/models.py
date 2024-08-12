from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(max_length=254, default=None)
    phone = models.CharField(max_length=11, default=None)
    number = models.IntegerField(default=None)
    date = models.DateField(default=None)
    time = models.TimeField(default=None)

    def __str__(self) -> str:
        return self.name