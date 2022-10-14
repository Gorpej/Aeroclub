from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

from reservation.models import Pilot, Aircraft, Slot
from reservation.serializers import PilotSerializer, AircraftSerializer, SlotSerializer, UserSerializer

# Create your views here.
class UserViewset(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class PilotViewset(ReadOnlyModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = PilotSerializer

    def get_queryset(self):
        return Pilot.objects.all()


class AircraftViewset(ReadOnlyModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = AircraftSerializer

    def get_queryset(self):
        return Aircraft.objects.all()


class SlotViewset(ReadOnlyModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = SlotSerializer

    def get_queryset(self):
        return Slot.objects.all()



"""@api_view(['POST'])
def slotCreate(request):
    serializer = SlotSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    print(serializer.data)
    return Response(serializer.data)
"""