from apps.shared.utils import get_current_week, get_current_biweek, get_current_month
from apps.bank.models import Bank
from apps.card.models import Card
from apps.configuration.models import Bitacora
from django.db import transaction
from datetime import date
import platform


def handle_period(option):
    if option == Bank.Period.BIWEENLY:
        return get_current_biweek()
    elif option == Bank.Period.MONTH:
        return get_current_month()
    else:
        return get_current_week()


def reset_cards(bank):
    try:
        cards = Card.objects.filter(bank=bank).update(current_balance=bank.limit_amount)
        log = Bitacora.objects.create(
            action=f"Actualización exitosa {bank.name}",
            details=f"Tarjetas actualizadas current_balance. {bank.name}",
            user_agent=platform.platform(),
        )
    except Bank.DoesNotExist:
        log = Bitacora.objects.create(
            action=f"Error en la actualización {bank.name}",
            details=f"Ocurrió un error: Tarjetas no actualizadas current_balance. {bank.name}",
            user_agent=platform.platform(),
        )


def my_cron_job():
    try:
        with transaction.atomic():
            banks = Bank.objects.all()
            fecha_actual = date.today()
            for bk in banks:
                fecha_limite = bk.end_date
                start_date, end_date = handle_period(bk.period)
                if fecha_actual > fecha_limite:
                    Bank.objects.filter(id=bk.id).update(
                        start_date=start_date, end_date=end_date
                    )
                    reset_cards(bk)

            log = Bitacora.objects.create(
                action="Actualización exitosa",
                details="Bancos actualizados fechas.",
                user_agent=platform.platform(),
            )
    except Exception as e:
        error_message = str(e)
        log = Bitacora.objects.create(
            action="Error en la actualización",
            details=f"Ocurrió un error: {error_message}",
            user_agent=platform.platform(),
        )
