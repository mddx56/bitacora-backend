from rest_framework import serializers
from .models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class SaldoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_id(self, value):
        print("validate_title method")
        if "_" in value:
            raise serializers.ValidationError("illegal char")
        return value
