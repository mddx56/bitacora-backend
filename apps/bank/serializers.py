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


class BankUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        exclude_fields = kwargs.pop("exclude_fields", None)
        super().__init__(*args, **kwargs)

        if exclude_fields:
            for field in exclude_fields:
                self.fields.pop(field, None)
