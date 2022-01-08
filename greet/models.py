from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('O', 'Others',),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(max_length=50, unique=True)
    pincode = models.CharField(max_length=6)
    phone = models.BigIntegerField(max_length=10)
