from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from companies.models import Company


class Address(models.Model):
    address1 = models.CharField("Address line 1", max_length=255)
    address2 = models.CharField("Address line 2", max_length=255, null=True, blank=True)
    city = models.CharField("City", max_length=255)
    country = models.CharField("Country", max_length=50)
    volume = models.DecimalField("Volume", max_digits=2, decimal_places=1)
    description = models.TextField("Description", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.address1} {self.city} {self.address2},vol{self.volume}"


class Client(models.Model):
    first_name = models.CharField("First Name", max_length=200,  null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=200,  null=True, blank=True)
    phone_number = PhoneNumberField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='clients')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.address}"
