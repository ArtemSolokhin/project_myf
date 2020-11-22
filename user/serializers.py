from rest_framework import serializers
from .models import MyfUser, Field, Culture, DatesCults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyfUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class DatesCultsSerializer(serializers.ModelSerializer):
    culture = CultureSerializer()

    class Meta:
        model = DatesCults
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    culture_desc = DatesCultsSerializer(read_only=True, source='cultures')
    owner_desc = UserSerializer(read_only=True, source='owner')

    class Meta:
        model = Field
        fields = '__all__'
