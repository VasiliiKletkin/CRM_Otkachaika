from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def create_order(sender, instance, created, **kwargs):
    if created:
        instance.send_to_driver()


@receiver(post_save, sender=Order)
def save_order(sender, instance, **kwargs):
    instance.client.update_data()
