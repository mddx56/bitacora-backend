from rest_framework import serializers
from .models import Bank


class Bankerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"
