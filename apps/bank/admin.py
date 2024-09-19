from django.contrib import admin
from .models import Bank
from django.utils.html import format_html

admin.site.site_header = "Panel Admin"
admin.site.site_title = "🚀"
admin.site.index_title = "Panel de control de Tarjetas"


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "limit_amount",
        "period",
        "start_date",
        "end_date",
        "show_image",
    )
    exclude = ("start_date", "end_date")

    def show_image(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="40" height="40"/>', obj.logo)
        return "No hay imagen"

    show_image.short_description = "Imagen"
