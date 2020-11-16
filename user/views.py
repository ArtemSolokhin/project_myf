from .models import MyfUser
from .serializers import UserSerializer
from rest_framework import generics

class UserListCreate(generics.ListCreateAPIView):
    queryset = MyfUser.objects.all()
    serializer_class = UserSerializer