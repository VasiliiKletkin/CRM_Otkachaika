from addresses.models import Address
from companies.mixins import CompanyMixin
from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(CompanyMixin, models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        verbose_name="Компания",
        related_name="clients",
    )
    first_name = models.CharField("Имя", max_length=200, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField("Телефонный номер")
    address = models.ForeignKey(
        Address, on_delete=models.PROTECT, verbose_name="Адрес", related_name="clients"
    )
    is_active = models.BooleanField("Активный", default=True)

    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        client_display = f"{self.phone_number}"
        if self.first_name:
            client_display += f" {self.first_name}"
        if self.last_name:
            client_display += f" {self.last_name}"
        return client_display
