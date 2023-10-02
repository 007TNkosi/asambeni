from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=False)

class Learner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='learner_profile')
    ## -_-_ Add other learner-specific fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    school = models.CharField(max_length=30)
    age = models.IntegerField()
    grade = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Driver(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='driver_profile')
    ## -_-_ Add other driver-specific fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=50)
    start_destination = models.CharField(max_length=50, default='Vosloorus')
    end_destination = models.CharField(max_length=50, default='Germiston')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AreaOfOperation(models.Model):
    name = models.CharField(max_length=50, verbose_name='Pick Up Area', help_text='Enter your pick up point.')

    def __str__(self):
        return self.name
    
class EndOfOperationArea(models.Model):
    name = models.CharField(max_length=50, verbose_name='Drop Off Area', help_text='Enter your drop off point.')

    def __str__(self):
        return self.name