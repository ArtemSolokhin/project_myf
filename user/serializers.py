from datetime import datetime, timedelta
import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import MyfUser, Field, Culture, DatesCults


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyfUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

    def save(self):
        user = super(UserSerializer, self).save()
        user.set_password(self.validated_data['password'])
        user.save()
        return user

    @staticmethod
    def validate_email(value):
        if not re.match(r"^[\w\-\\.]+@([\w-]+\.)+[\w-]{2,4}$", value):
            raise ValidationError("This is not an email!")
        return value

    


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'

    @staticmethod
    def validate_harvest_days(value):
        if value < 0:
            raise ValidationError("Can not be smaller than 1 day")
        return value


class DatesCultsSerializer(serializers.ModelSerializer):
    culture_desc = CultureSerializer(read_only=True, source='culture')

    class Meta:
        model = DatesCults
        fields = '__all__'

    @staticmethod
    def validate_harvest_date(value):
        if datetime.now().date() < value:
            raise ValidationError("Data can not be later than now")
        return value


class FieldSerializer(serializers.ModelSerializer):
    culture_desc = DatesCultsSerializer(read_only=True, source='cultures')
    owner_desc = UserSerializer(read_only=True, source='owner')

    class Meta:
        model = Field
        fields = '__all__'

    @staticmethod
    def validate_length(value):
        if value <= 0:
            raise ValidationError("Length can't be smaller than 1")
        return value

    @staticmethod
    def validate_width(value):
        if value <= 0:
            raise ValidationError("Width can't be smaller than 1")
        return value

