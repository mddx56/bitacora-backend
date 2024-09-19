from datetime import datetime, timedelta


def get_current_week():
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def get_current_biweek():
    today = datetime.now()
    if today.day <= 15:
        start_of_biweek = today.replace(day=1)
        end_of_biweek = today.replace(day=15)
    else:
        start_of_biweek = today.replace(day=16)
        end_of_biweek = (today.replace(day=1) + timedelta(days=31)).replace(
            day=1
        ) - timedelta(days=1)
    return start_of_biweek, end_of_biweek


def get_current_month():
    today = datetime.now()
    start_of_month = today.replace(day=1)
    end_of_month = (today.replace(day=28) + timedelta(days=4)).replace(
        day=1
    ) - timedelta(days=1)
    return start_of_month, end_of_month
