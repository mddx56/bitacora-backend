from django.contrib import admin
from .models import Transaction, Category

admin.site.register(Category)
# admin.site.register(Transaction)


@admin.register(Transaction)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "merchant")
