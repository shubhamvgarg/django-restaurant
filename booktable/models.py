from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Booking(models.Model):
    name=models.CharField(max_length=20)
    phone = models.CharField(
        max_length=15, 
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        )]
    )
    email = models.EmailField(max_length=100)
    persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField(null=True)
    accept = models.BooleanField(default=False)

    def __str__(self):
        return self.name