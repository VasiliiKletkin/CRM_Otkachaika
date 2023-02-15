from companies.models import Company
from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):

    OWNER = 'OWNER'
    DRIVER = 'DRIVER'
    DISPATCHER = 'DISPATCHER'

    USER_TYPES = Choices(
        (OWNER, 'Владелец'),
        (DRIVER, 'Водитель'),
        (DISPATCHER, 'Диспетчер'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(choices=USER_TYPES, max_length=20)
    phone_number = PhoneNumberField('Телефонный номер')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
