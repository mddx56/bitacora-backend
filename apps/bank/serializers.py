from rest_framework import serializers
from .models import Bank


class ConfigSerializer(serializers.Serializer):
    period = serializers.ChoiceField(choices=Bank.Period.choices)
    limit_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_limit_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto límite debe ser mayor a 0.")
        return value


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"
