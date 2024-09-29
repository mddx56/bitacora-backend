from django.contrib import admin
from .models import Bitacora


@admin.register(Bitacora)
class BitacoraAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "details",
        "timestamp",
        "user",
    )
