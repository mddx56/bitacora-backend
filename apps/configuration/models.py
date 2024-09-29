from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Bitacora(models.Model):
    action = models.CharField(max_length=355)
    details = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Bitacora"
        verbose_name_plural = "Bitacoras"

    def __str__(self):
        return self.action
