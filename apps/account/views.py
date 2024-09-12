from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import rest_framework.status as status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class UserAccountView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [IsAdminUser]
