from django.apps import AppConfig


class CardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.card"
    verbose_name = "Gestion de Tarjetas"

    def ready(self):
        import apps.card.signals
