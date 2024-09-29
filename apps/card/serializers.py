from rest_framework import serializers
from .models import Card


class CardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
        depth = 2


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"


class CardIdSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    deleted_at = serializers.BooleanField()
