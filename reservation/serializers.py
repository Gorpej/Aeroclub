from rest_framework.serializers import ModelSerializer
from reservation.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'first_name', 'last_name', 'email']