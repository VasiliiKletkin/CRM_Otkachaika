from django.db import models


class Country(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"
        indexes = [
            models.Index(name="country_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, verbose_name="Страна", related_name="regions"
    )
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        indexes = [
            models.Index(name="region_name_idx", fields=["name"]),
        ]
        

    def __str__(self):
        return f"{self.name}, {self.country}"


class City(models.Model):
    region = models.ForeignKey(
        Region, on_delete=models.PROTECT, verbose_name="Регион", related_name="cities"
    )
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        indexes = [
            models.Index(name="city_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"г.{self.name}, {self.region}"


class Street(models.Model):
    city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="Город", related_name="streets"
    )
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Улицу"
        verbose_name_plural = "Улицы"
        indexes = [
            models.Index(name="street_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"ул. {self.name}, {self.city.name}, {self.city.region.name}"


class Address(models.Model):
    street = models.ForeignKey(
        Street, on_delete=models.PROTECT, verbose_name="Улица", related_name="addresses"
    )
    home = models.CharField("Дом", max_length=255)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        indexes = [
            models.Index(name="address_home_idx", fields=["home"]),
        ]

    def __str__(self):
        return f"{self.home}, ул. {self.street.name}, {self.street.city.name}"
