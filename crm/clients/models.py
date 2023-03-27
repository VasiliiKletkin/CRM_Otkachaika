from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    street = models.CharField("Улица", max_length=255)
    home = models.CharField("Дом", max_length=255)
    city = models.CharField("Город", max_length=255)
    country = models.CharField("Страна", max_length=50)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адресa"

        indexes = [
            models.Index(name="address_street_idx", fields=['street']),
            models.Index(name="address_home_idx", fields=['home']),
        ]

    def __str__(self):
        return f"{self.street} {self.home}, {self.city}"


class Client(models.Model):
    first_name = models.CharField(
        "Имя", max_length=200,  null=True, blank=True)
    last_name = models.CharField(
        "Фамилия", max_length=200,  null=True, blank=True)
    phone_number = PhoneNumberField('Телефонный номер')
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, related_name='clients')
    is_active = models.BooleanField('Активный', default=True)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name='clients')
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"id:{self.id}, {self.phone_number}"
