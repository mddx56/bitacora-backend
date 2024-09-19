from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.shared.utils import get_current_week, get_current_biweek, get_current_month
from .models import Bank


def handle_period(option):
    if option == Bank.Period.BIWEENLY:
        return get_current_biweek()
    elif option == Bank.Period.MONTH:
        return get_current_month()
    else:
        return get_current_week()


@receiver(post_save, sender=Bank)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    start_date, end_date = handle_period(instance.period)
    if instance.start_date != start_date or instance.end_date != end_date:
        Bank.objects.filter(id=instance.id).update(
            start_date=start_date, end_date=end_date
        )
