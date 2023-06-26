from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Company, CompanyAccounting, CompanyWorkPlace


@receiver(post_save, sender=Company)
def create_client(sender, instance, created, **kwargs):
    if created:
        CompanyAccounting.objects.create(company=instance)
        CompanyWorkPlace.objects.create(company=instance)


@receiver(post_save, sender=Company)
def save_client(sender, instance, **kwargs):
    pass
