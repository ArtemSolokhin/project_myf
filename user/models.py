from django.db import models
from django.contrib.auth.models import AbstractUser


class MyfUser(AbstractUser):
    pass


class Culture(models.Model):
    name = models.CharField(max_length=255)
    harvest_time = models.TimeField()

    def __str__(self):
        return self.name


class DatesCults(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    harvest_date = models.DateField()


class Field(models.Model):
    owner = models.ForeignKey(MyfUser, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    cultures = models.ForeignKey(DatesCults, on_delete=models.CASCADE)
