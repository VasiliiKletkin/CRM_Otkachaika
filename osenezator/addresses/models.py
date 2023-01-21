from django.db import models
from companies.models import Company

# Create your models here.

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