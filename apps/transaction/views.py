from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from apps.card.models import Card
from .models import Transaction, Category
from .serializers import (
    TransactionSerializer,
    CategorySerializer,
    TransactionListSerializer,
)
from django.db import transaction


class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TransactionView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionListSerializer
    queryset = Transaction.objects.all()


"""
@api_view(["POST"])
def CreditCard(request):
    with transaction.atomic():
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data["amount"]
            card = serializer.validated_data["card"]
            user = serializer.validated_data["user"]
            category = serializer.validated_data["category"]
            merchant = serializer.validated_data["merchant"]
            description = serializer._validated_data["description"]
            cards = Card.objects.select_for_update().get(id=card.id)

            if cards.status != cards.Status.ACTIVE:
                return Response(
                    {"detail": "Tarjeta no activa."}, status=status.HTTP_400_BAD_REQUEST
                )

            if amount <= 0:
                return Response(
                    {"detail": "Monto deve ser mayor a cero."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if amount > cards.credit_limit:
                return Response(
                    {"detail": "El monto excede el límite máximo de depósito."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            cards.current_balance += amount
            cards.save()
            transac = Transaction.objects.create(
                amount=amount,
                merchant=merchant,
                description=description,
                user=user,
                type="D",
                category=category,
                card=cards,
            )
            serializer_transaction = TransactionSerializer(transac)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data=serializer_transaction.data, status=status.HTTP_201_CREATED
        )
"""


@api_view(["POST"])
def DevitCard(request):
    with transaction.atomic():
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data["amount"]
            card = serializer.validated_data["card"]
            user = serializer.validated_data["user"]
            description = serializer._validated_data["description"]
            category = serializer.validated_data["category"]
            merchant = serializer.validated_data["merchant"]
            cards = Card.objects.select_for_update().get(id=card.id)

            if cards.status != cards.Status.ACTIVE:
                print("Tarjeta no activa")

            if amount <= 0:
                print("Monto deve ser mayor a cero")

            if cards.current_balance < amount:
                print("Fondos insuficientes.")

            cards.current_balance -= amount
            cards.save()
            transac = Transaction.objects.create(
                amount=amount,
                merchant=merchant,
                description=description,
                user=user,
                type="C",
                category=category,
                card=cards,
            )
            serializer_transaction = TransactionSerializer(transac)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            data=serializer_transaction.data, status=status.HTTP_201_CREATED
        )
