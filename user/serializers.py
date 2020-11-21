from rest_framework import serializers
from .models import MyfUser, Field, Culture, DatesCults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyfUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class DatesCultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatesCults
        fields = '__all__'
