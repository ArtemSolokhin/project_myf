from rest_framework import serializers
from .models import MyfUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyfUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')