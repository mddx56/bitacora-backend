from apps.shared.utils import get_current_week, get_current_biweek, get_current_month
from apps.bank.models import Bank
from datetime import datetime

def handle_period(option):
    if option == Bank.Period.BIWEENLY:
        return get_current_biweek()
    elif option == Bank.Period.MONTH:
        return get_current_month()
    else:
        return get_current_week()

def my_cron_job():
    banks = Bank.objects.all()
    fecha_actual = datetime.now()
    for bk in banks:
        fecha_limite=bk.end_date
        start_date, end_date = handle_period(bk.period)
        if fecha_actual >= fecha_limite:
            Bank.objects.filter(id=bk.id).update(
            start_date=start_date, end_date=end_date
        )