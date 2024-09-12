from django.db import models
from django.contrib.auth import get_user_model
from apps.shared.models import TimeStampedBaseModel
from apps.card.models import Card

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        verbose_name="Nombre de categoria", unique=True, max_length=350
    )
    description = models.TextField(verbose_name="Descripcion", blank=True)

    class Meta:
        verbose_name = "Categoria de transaccion"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return f"{self.name}"


class Transaction(TimeStampedBaseModel):
    class TypeTr(models.TextChoices):
        DEBIT = "D", "Debit"
        CREDIT = "C", "Credit"

    amount = models.DecimalField(verbose_name="Monto", max_digits=10, decimal_places=2)
    description = models.TextField(verbose_name="Descripcion", blank=True)
    merchant = models.CharField(verbose_name="Comercio", max_length=450)
    category = models.ForeignKey(
        Category, verbose_name="Categoria", on_delete=models.CASCADE
    )
    type = models.CharField(
        verbose_name="Tipo", max_length=1, choices=TypeTr.choices, default=TypeTr.DEBIT
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactiones"

    def __str__(self) -> str:
        return f"{self.amount}"
