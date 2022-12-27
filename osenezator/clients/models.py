from django.db import models


class Address(models.Model):
    address1 = models.CharField("Address line 1", max_length=255)
    address2 = models.CharField("Address line 2", max_length=255, blank=True)
    city = models.CharField("City", max_length=255)
    country = models.CharField("Country", max_length=50)
    volume = models.DecimalField("Volume", max_digits=2, decimal_places=1)
    description = models.TextField("Description", max_length=255, blank=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.address1} {self.city} {self.address2},vol{self.volume}"


class Client(models.Model):
    first_name = models.CharField("First Name", max_length=200,  blank=True)
    last_name = models.CharField("Last Name", max_length=200,  blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.address}"
