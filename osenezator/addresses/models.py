from django.db import models


class Address(models.Model):
    name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024)
    zip_code = models.CharField("ZIP / Postal code", max_length=12)
    city = models.CharField("City", max_length=1024)
    country = models.CharField("Country", max_length=50)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
    def __str__(self):
        return self.name+self.country