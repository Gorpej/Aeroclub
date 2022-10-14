from django.conf import settings
from django.db import models


class Pilot(models.Model):
    avatar = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name



class Aircraft(models.Model):
    registration = models.CharField(max_length=70, blank=False)
    model = models.CharField(max_length=70, blank=False)
    aircraft_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.model


class Slot(models.Model):
    date = models.DateField(blank=True)
    start_times = models.IntegerField(blank=True)
    end_times = models.IntegerField(blank=True)
