from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from django.db import transaction


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


@api_view(["POST"])
def DebitCard(request):
    with transaction.atomic():
        data = request.data 
       # if data.se


@api_view(["POST"])
def CreditCard(request):
    with transaction.atomic():
        pass
