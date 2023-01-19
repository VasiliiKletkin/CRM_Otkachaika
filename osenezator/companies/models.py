from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField('Name Company', max_length=255)
    phone_number = PhoneNumberField()
    city = models.CharField('City', max_length=255)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"
