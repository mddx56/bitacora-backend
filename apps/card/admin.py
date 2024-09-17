from django.contrib import admin
from .models import Card

from unfold.admin import ModelAdmin


@admin.register(Card)
class CustomAdminClass(ModelAdmin):
    list_display = ("id", "holder", "card_number", "current_balance", "status")


# @admin.register(Card)
# class MusicianAdmin(admin.ModelAdmin):
#    list_display = ("id", "holder", "card_number", "current_balance", "status")
