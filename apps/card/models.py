from django.db import models
from django.utils import timezone
from apps.shared.models import TimeStampedBaseModel
from apps.bank.models import Bank


class Card(TimeStampedBaseModel):
    class Status(models.TextChoices):
        ACTIVE = "A", "Active"
        INACTIVE = "I", "Inactive"

    class TypeC(models.TextChoices):
        DEBIT = "D", "Debit"
        CREDIT = "C", "Credit"

    card_number = models.CharField(
        verbose_name="Número de tarjeta.", null=False, unique=True, max_length=16
    )
    holder = models.CharField(
        verbose_name="Titular de la tarjeta", null=False, max_length=600
    )
    expiration_date = models.CharField(
        verbose_name="Fecha de expiracion", null=False, max_length=8
    )
    cvv = models.CharField(verbose_name="CVV", null=False, max_length=3)
    type = models.CharField(
        verbose_name="Tipo de tarjeta",
        blank=True,
        null=True,
        choices=TypeC,
        default=TypeC.CREDIT,
        max_length=2,
    )
    current_balance = models.DecimalField(
        verbose_name="Saldo actual",
        blank=True,
        null=True,
        max_digits=10,
        decimal_places=2,
    )
    status = models.CharField(
        verbose_name="Estado de la tarjeta",
        blank=True,
        null=True,
        max_length=1,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    bank = models.ForeignKey(Bank, verbose_name="Banco", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tarjeta de credito"
        verbose_name_plural = "Tarjetas de credito"

    def __str__(self) -> str:
        return f"{self.holder}"

    def get_inf_name(self):
        return f"{self.holder} {self.status}"
