from rest_framework import serializers
from .models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    def validate_amount(self, value):
        print(value)
        if value <= 0:
            raise serializers.ValidationError("deve ser mayor a cero")
        return value

    class Meta:
        model = Transaction
        fields = "__all__"
