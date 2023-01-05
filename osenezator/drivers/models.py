from django.db import models

from companies.models import Company
from phonenumber_field.modelfields import PhoneNumberField

class Car(models.Model):
    name = models.CharField("Car Name", max_length=255)
    number = models.CharField("Car Number", max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='cars')

    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.name} Num car {self.number}"


class Driver(models.Model):
    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    phone_number = PhoneNumberField()
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='driver')
    is_active = models.BooleanField(default=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='drivers')


    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
