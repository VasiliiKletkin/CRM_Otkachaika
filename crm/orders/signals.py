from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order


@receiver(post_save, sender=Order)
def post_order_save(sender, **kwargs):
    print("post_order_save")