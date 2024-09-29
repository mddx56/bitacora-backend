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
    actions = ("mark_reset", "mark_avalible", "mark_disable")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    @admin.action(description="Restablecer monto Tarjetas seleccionado/s")
    def mark_reset(modeladmin, request, queryset):
        for card in queryset:
            card.current_balance = card.bank.limit_amount
            card.status = Card.Status.ACTIVE
            card.save()
        modeladmin.message_user(request, "Monto de tarjetas restablecidos")

    @admin.action(description="Deshavilitar Tarjetas seleccionado/s")
    def mark_disable(modeladmin, request, queryset):
        queryset.update(deleted_at=True)
        modeladmin.message_user(request, "Tarjetas deshavilitadas correctamente")

    @admin.action(description="Havilitar Tarjetas seleccionado/s")
    def mark_avalible(modeladmin, request, queryset):
        queryset.update(deleted_at=False)
        modeladmin.message_user(request, "Tarjetas havilitadas correctamente")

    def get_bank_name(self, obj):
        return obj.bank.name

    get_bank_name.short_description = "Banco"
