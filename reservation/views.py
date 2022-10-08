from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from reservation.models import User
from reservation.serializers import UserSerializer


# Create your views here.
class UserViewset(ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter()
