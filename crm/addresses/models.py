from django.db import models


class Country(models.Model):
    uid = models.CharField("Уникальный номер региона", max_length=255, unique=True)
    name = models.CharField("Название", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Страну"
        verbose_name_plural = "Страны"
        indexes = [
            models.Index(name="country_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name}"


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="Страна", related_name="regions")
    uid = models.CharField("Уникальный номер региона", max_length=255, unique=True)
    name = models.CharField("Название", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        indexes = [
            models.Index(name="region_name_idx", fields=["name"]),
        ]
        
    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="Регион", related_name="cities")
    uid = models.CharField("Уникальный номер города", max_length=255, unique=True)
    name = models.CharField("Название", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        indexes = [
            models.Index(name="city_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"{self.region}, {self.name}," if self.region.name else f"{self.name},"


class Street(models.Model):
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Город", related_name="streets")
    uid = models.CharField("Уникальный номер улицы", max_length=255, unique=True)
    name = models.CharField("Название", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Улицу"
        verbose_name_plural = "Улицы"
        indexes = [
            models.Index(name="street_name_idx", fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name}, {self.city.name}, {self.city}"


class Address(models.Model):
    street = models.ForeignKey(Street, on_delete=models.PROTECT, verbose_name="Улица", related_name="addresses", null=True, blank=True)
    title = models.CharField("Полное название адреса", max_length=255, null=True, blank=True)
    uid = models.CharField("Уникальный номер адреса", max_length=255, unique=True)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        indexes = [
            models.Index(name="address_uid_idx", fields=["uid"]),
        ]

    def __str__(self):
        return f"{self.title}"
