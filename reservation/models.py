from django.db import models

# Create your models here.


class User(models.Model):

    last_name = models.CharField(max_length=70, blank=False)
    first_name = models.CharField(max_length=70, blank=False)
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name

"""class Aircraft(models.Model):

    registration = models.CharField(max_length=70, blank=False)
    model = models.CharField(max_length=70, blank=False)
    aircraft_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.model"""

"""class Reservation(models.Model):
    aircraft_id =
    user_id=
    date = models.DateField(blank=True)
    start_times = models.IntegerField(blank=True)
    end_times = models.IntegerField(blank=True)"""