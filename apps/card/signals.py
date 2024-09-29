from django.dispatch import receiver
from django.db.models.signals import post_save
from apps.bank.models import Bank
from .models import Card


@receiver(post_save, sender=Card)
def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        bank = Bank.objects.get(id=instance.bank.id)
        print("llegue")
        Card.objects.filter(id=instance.id).update(current_balance=bank.limit_amount)
