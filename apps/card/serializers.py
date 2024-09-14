from rest_framework import serializers
from .models import Card


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
        depth = 1


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
