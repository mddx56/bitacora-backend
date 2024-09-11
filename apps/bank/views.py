from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Bank
from .serializers import Bankerializer


class BankView(viewsets.ModelViewSet):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()
