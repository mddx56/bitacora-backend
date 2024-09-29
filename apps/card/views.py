from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from apps.bank.models import Bank
from .models import Card
from .serializers import (
    CardSerializer,
    CardListSerializer,
    CardIdSerializer,
    CardDeletedSerializer,
)


class CardCreateAPIView(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardUpdateAPIView(UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardRetrieveAPIView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


@api_view(["GET"])
def CardListView(request):
    try:
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))
        offset = (page - 1) * page_size
        limit = page * page_size
        cards = Card.objects.all()[offset:limit]
        cards_data = CardListSerializer(cards, many=True).data
        return Response(data=cards_data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def CardDisableView(request):
    serializer = CardDeletedSerializer(data=request.data)
    try:
        if serializer.is_valid():
            card_id = serializer.validated_data["id"]
            deleted_at = serializer.validated_data["deleted_at"]
            card = Card.objects.get(id=card_id)
            card.deleted_at = deleted_at
            card.save()
            if deleted_at:
                return Response(
                    {"detail": "Tarjeta deshabilitada"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"detail": "Tarjeta habilitada"}, status=status.HTTP_200_OK
                )
        else:
            return Response(
                {"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
    except Card.DoesNotExist:
        return Response(
            {"detail": "Tarjeta no encontrada"}, status=status.HTTP_404_NOT_FOUND
        )


def reset_current_balance(card: Card):
    try:
        card.current_balance = card.bank.limit_amount
        card.status = Card.Status.ACTIVE
        card.save()
    except Bank.DoesNotExist:
        print("banco no existe")


@api_view(["POST"])
def CardResetBalanceView(request):
    serializer = CardIdSerializer(data=request.data)
    try:
        if serializer.is_valid():
            card_id = serializer.validated_data["id"]
            card = Card.objects.get(id=card_id)
            reset_current_balance(card)
            return Response(
                {"detail": "Tarjeta monto reiniciado"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )
    except Card.DoesNotExist:
        return Response(
            {"detail": "Tarjeta no encontrada"}, status=status.HTTP_404_NOT_FOUND
        )
