from .models import MyfUser, Field, Culture, DatesCults
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, FieldSerializer, CultureSerializer, DatesCultsSerializer
from rest_framework import generics


class UserViewSet(ModelViewSet):
    queryset = MyfUser.objects.all()
    serializer_class = UserSerializer


class FieldViewSet(ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class CultureViewSet(ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer


class DatesCultsViewSet(ModelViewSet):
    queryset = DatesCults.objects.all()
    serializer_class = DatesCultsSerializer
