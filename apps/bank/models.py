from django.db import models
from apps.shared.models import TimeStampedBaseModel
from django.utils import timezone
from datetime import timedelta


class Bank(TimeStampedBaseModel):
    class Period(models.TextChoices):
        WEEK = "W", "Semanal"
        BIWEENLY = "B", "Quincenal"
        MONTH = "M", "Mensual"
        OTRO = "O", "Otro"

    name = models.CharField(verbose_name="Nombre de banco", null=False, max_length=350)
    logo = models.URLField(verbose_name="Url Logo", null=True, blank=True)
    limit_amount = models.DecimalField(
        verbose_name="Monto Limite", max_digits=10, decimal_places=2
    )
    period = models.CharField(
        verbose_name="Frecuencia dia",
        null=False,
        choices=Period.choices,
        default=Period.WEEK,
        max_length=2,
    )
    start_date = models.DateField(verbose_name="Fecha Inicio", null=True)
    end_date = models.DateField(verbose_name="Fecha Fin", null=True)

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.name
