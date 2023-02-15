from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


class Company(models.Model):
    name = models.CharField('Название компании', max_length=255)
    phone_number = PhoneNumberField('Телефонный номер',)
    city = models.CharField('Город', max_length=255, null=True, blank=True)
    country = models.CharField('Страна', max_length=255, null=True, blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    balance = MoneyField('Баланс',max_digits=12, decimal_places=2, default_currency='RUB', default=0)
    is_active = models.BooleanField('Активный',default=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"
