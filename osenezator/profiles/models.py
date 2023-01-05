from django.db import models
from django.contrib.auth.models import User
from companies.models import Company
from django.db.models.signals import post_save
from django.dispatch import receiver
from model_utils import Choices



class Profile(models.Model):

    ADMIN='OWNER'
    DRIVER='DRIVER'
    DISPETCHER='DISPETCHER'

    USER_TYPES = Choices(
        (ADMIN, 'Owner'),
        (DRIVER, 'Driver'),
        (DISPETCHER, 'Dispetcher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type =  models.CharField(choices=USER_TYPES, max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True) 

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.company} - {self.user} - {self.user_type}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.is_superuser = True
        instance.save()
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()