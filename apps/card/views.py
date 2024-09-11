from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Card
from .serializers import CardSerializer


class CardView(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
