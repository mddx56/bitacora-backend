from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from apps.bank.models import Bank
from apps.card.models import Card
from apps.bank.cron import handle_period


def reset_cards(bank):
    try:
        cards = Card.objects.filter(bank=bank).update(current_balance=bank.limit_amount)
    except Bank.DoesNotExist:
        print("error")


class Command(BaseCommand):
    help = "Test only test"

    def handle(self, *args, **kwargs):
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
