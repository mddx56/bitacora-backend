from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from apps.card.models import Card
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer, SaldoSerializer
from django.db import transaction


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


@api_view(["POST"])
def DebitCard(request):
    with transaction.atomic():
        serializer = SaldoSerializer(data=request.data)
        if serializer.is_valid():
            _id = serializer.validated_data["id"]
            amount = serializer.validated_data["amount"]
            card = Card.objects.select_for_update().get(id=_id)
            # Transaction.objects.create(account=account, amount=Decimal(amount),
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(_id, status=status.HTTP_200_OK)


@api_view(["POST"])
def CreditCard(request):
    with transaction.atomic():
        pass
        # account = Card.objects.select_for_update().get(user=user)
        # Transaction.objects.create(
        ##    account=account, amount=Decimal(amount), transaction_type="credit"
        # )
        # account.balance += Decimal(amount)
        # account.save()
