from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Card
from .serializers import CardSerializer
from django.db import transaction


class CardView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


@api_view(["GET"])
def AddSaldoCard(request, id):
    pass


@api_view(["POST"])
def AddSaldoCard(request):
    pass


@api_view(["POST"])
def AddSaldoCard(request):
    with transaction.atomic():
        pass
