from django.contrib import admin
from .models import Card


@admin.register(Card)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "holder", "card_number", "current_balance", "status","deleted_at")
