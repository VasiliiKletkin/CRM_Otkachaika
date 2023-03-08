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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = PhoneNumberField('Телефонный номер')
    telegram_id = models.CharField('telegram_id', max_length=20)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural ='Профили'

    def __str__(self):
        return f'{self.get_user_type_display()}-{self.company}'