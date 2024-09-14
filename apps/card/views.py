from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Card
from .serializers import CardSerializer, CardListSerializer
from django.db import transaction
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView


@api_view(["GET"])
def CardListView(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    offset = (page - 1) * page_size
    limit = page * page_size
    cards = Card.objects.all()[offset:limit]
    cards_data = CardListSerializer(cards, many=True).data
    return Response(data=cards_data, status=status.HTTP_200_OK)


class CardCreateAPIView(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardUpdateAPIView(UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardRetrieveAPIView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


@api_view(["POST"])
def CreditSaldoCard(request):
    with transaction.atomic():
        pass


@api_view(["POST"])
def DevitSaldoCard(request):
    with transaction.atomic():
        pass
