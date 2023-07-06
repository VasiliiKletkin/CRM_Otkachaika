from datetime import datetime, timedelta

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import (Company, CompanyAccounting, CompanySubscription,
                     CompanyWorkPlace)


@receiver(post_save, sender=Company)
def post_create_company(sender, instance, created, **kwargs):
    if created:
        CompanyAccounting.objects.create(company=instance)
        CompanyWorkPlace.objects.create(company=instance)


@receiver(post_save, sender=Company)
def post_save_company(sender, instance, **kwargs):
    pass

@receiver(pre_save, sender=CompanySubscription)
def pre_create_subscription(sender, instance, **kwargs):
    if not instance.id:
        instance.date_subscribed_off = datetime.now() + timedelta(days=int(instance.service.period))