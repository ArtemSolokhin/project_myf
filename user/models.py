from django.db import models
from django.contrib.auth.models import AbstractUser


class MyfUser(AbstractUser):

    def __str__(self):
        return self.username


class Culture(models.Model):
    name = models.CharField(max_length=255, unique=True)
    harvest_days = models.IntegerField()

    def __str__(self):
        return self.name


class Field(models.Model):
    owner = models.ForeignKey(MyfUser, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    normal_temperature = models.IntegerField()
    normal_earth_weat = models.IntegerField()
    real_state = models.DecimalField(null=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.owner}'s field"


class DatesCults(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    harvest_date = models.DateField()
    length = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    coordinates = models.CharField(null=True, max_length=255)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.culture
