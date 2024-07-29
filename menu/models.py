from django.db import models

# Create your models here.

class Menu(models.Model):
    name=models.CharField(max_length=20)
    description =models.CharField(max_length=100)
    image =models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    price =models.IntegerField()

    def __str__(self):
        return self.name