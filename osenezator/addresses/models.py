from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    street = models.CharField("Street", max_length=255)
    home = models.CharField("Home", max_length=255)
    city = models.CharField("City", max_length=255)
    country = models.CharField("Country", max_length=50)
    description = models.TextField("Description", max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.home}, {self.city}"


class Client(models.Model):
    first_name = models.CharField("First Name", max_length=200,  null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=200,  null=True, blank=True)
    phone_number = PhoneNumberField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='clients')
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"id:{self.id}, {self.phone_number}"
