from companies.models import Company
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices


class Profile(models.Model):

    OWNER='OWNER'
    DRIVER='DRIVER'
    DISPATCHER='DISPATCHER'

    USER_TYPES = Choices(
        (OWNER, 'Owner'),
        (DRIVER, 'Driver'),
        (DISPATCHER, 'Dispatcher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type =  models.CharField(choices=USER_TYPES, max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True) 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()