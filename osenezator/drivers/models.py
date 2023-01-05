from django.db import models

from companies.models import Company
from phonenumber_field.modelfields import PhoneNumberField

class Car(models.Model):
    name = models.CharField("Car Name", max_length=255)
    number = models.CharField("Car Number", max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.name} Num car {self.number}"


class Driver(models.Model):
    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    phone_number = PhoneNumberField(blank=True)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    telegram_id = models.PositiveIntegerField("Telegram ID")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
