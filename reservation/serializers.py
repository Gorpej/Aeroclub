from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Pilot, Aircraft, Slot


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PilotSerializer(ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'


class AircraftSerializer(ModelSerializer):
    class Meta:
        model = Aircraft
        fields = ['id', 'model']


class SlotSerializer(ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'
