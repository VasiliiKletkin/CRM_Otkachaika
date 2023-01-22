from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField

user_model = get_user_model()


class Profile(models.Model):

    OWNER = 'OWNER'
    DRIVER = 'DRIVER'
    DISPATCHER = 'DISPATCHER'

    USER_TYPES = Choices(
        (OWNER, 'Owner'),
        (DRIVER, 'Driver'),
        (DISPATCHER, 'Dispatcher'),
    )

    user = models.OneToOneField(user_model, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(choices=USER_TYPES, max_length=20)
    phone_number = PhoneNumberField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.id} - {self.user_type}"
