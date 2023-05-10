from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RegistationCenterAdmin(models.Model):
    center_name = models.CharField(max_length = 100)
    area = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)

    def __str__(self):
        return self.center_name

class Owner(models.Model):
    fullname = models.CharField(max_length = 180)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 180)
    phone = models.CharField(max_length = 20)
    indenty = models.CharField(max_length = 20)
    birthday = models.DateTimeField(auto_now = True, blank = True)
    accommodation = models.CharField(max_length = 100)
    place_of_birth = models.CharField(max_length = 100)

    def __str__(self):
        return self

class Car(models.Model):
    type = models.CharField(max_length = 255)
    producer = models.CharField(max_length = 180)
    code = models.CharField(max_length = 180)
    registation_day = models.DateTimeField(auto_now = True, blank = True)
    plate = models.CharField(max_length = 20)
    registation_area = models.CharField(max_length = 100)
    uses = models.CharField(max_length = 100)
    owner_id = models.ForeignKey(Owner, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.code
        
class RegistationDoc(models.Model):
    code = models.CharField(max_length = 180)
    start_day = models.DateTimeField(auto_now = True, blank = True)
    start_day = models.DateTimeField(auto_now = True, blank = True)
    car_id = models.ForeignKey(Car, on_delete = models.CASCADE, blank = True, null = True)
    center_id = models.ForeignKey(RegistationCenterAdmin, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.code