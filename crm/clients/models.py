from addresses.models import Address
from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, verbose_name='Компания', related_name='clients')
    first_name = models.CharField(
        "Имя", max_length=200,  null=True, blank=True)
    last_name = models.CharField(
        "Фамилия", max_length=200,  null=True, blank=True)
    phone_number = PhoneNumberField('Телефонный номер')
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, verbose_name='Адрес', related_name='clients')
    is_active = models.BooleanField('Активный', default=True)

    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"id:{self.id}, {self.phone_number}"
