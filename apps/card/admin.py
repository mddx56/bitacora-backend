from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "holder",
        "card_number",
        "current_balance",
        "get_bank_name",
        "status",
        "deleted_at",
    )
    exclude = ("current_balance",)

    def get_bank_name(self, obj):
        return obj.bank.name

    get_bank_name.short_description = "Banco"
