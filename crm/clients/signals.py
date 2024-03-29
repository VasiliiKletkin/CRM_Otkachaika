from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Client, ClientStatistics, ClientAnalytics


@receiver(post_save, sender=Client)
def post_create_client(sender, instance, created, **kwargs):
    if created:
        ClientStatistics.objects.create(client=instance)
        ClientAnalytics.objects.create(client=instance)



@receiver(post_save, sender=Client)
def post_save_client(sender, instance, **kwargs):
    pass