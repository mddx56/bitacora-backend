from django.db import models
from apps.shared.models import TimeStampedBaseModel


# Create your models here.
class Bank(TimeStampedBaseModel):
    name = models.CharField(verbose_name="Nombre de banco", null=False, max_length=350)
    logo = models.URLField(verbose_name="Url Logo")

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self) -> str:
        return f"{self.name}"
