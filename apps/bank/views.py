from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Bank
from .serializers import Bankerializer


class BankCreateAPIView(CreateAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()


class BankUpdateAPIView(UpdateAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()


class BankListAPIView(ListAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()


class BankRetrieveAPIView(RetrieveAPIView):
    serializer_class = Bankerializer
    queryset = Bank.objects.all()
