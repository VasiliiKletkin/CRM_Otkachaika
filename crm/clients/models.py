from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    name = models.CharField('Название', max_length=255)
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, verbose_name="Cтрана", related_name="regions")

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    name = models.CharField('Название', max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, verbose_name="Регион", related_name="cities")

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f"{self.name}, {self.region}"


class Street(models.Model):
    name = models.CharField('Название', max_length=255)
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Улица", related_name="streets")

    class Meta:
        verbose_name = "Улицу"
        verbose_name_plural = "Улицы"

    def __str__(self):
        return f"ул. {self.name}, {self.city.name}"


class Address(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город", related_name="addresses")
    street = models.ForeignKey(
        Street, on_delete=models.PROTECT, verbose_name="Улица", related_name="addresses")
    home = models.CharField("Дом", max_length=255)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адресa"

        indexes = [
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
