from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, verbose_name="Cтрана", related_name="regions")
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"

    def __str__(self):
        return f"{self.name}, {self.country}"


class City(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, verbose_name="Регион", related_name="cities")
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        indexes = [
            models.Index(name="city_name_idx", fields=['name']),
        ]

    def __str__(self):
        return f"{self.name}, {self.region}"


class Street(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город", related_name="streets")
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = "Улицу"
        verbose_name_plural = "Улицы"
        indexes = [
            models.Index(name="street_name_idx", fields=['name']),
        ]

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
