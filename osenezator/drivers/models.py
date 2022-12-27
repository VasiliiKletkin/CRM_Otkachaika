from django.db import models


class Car(models.Model):
    name = models.CharField("Name", max_length=255)
    volume = models.DecimalField("Volume", max_digits=2, decimal_places=1)
    number = models.CharField("Number", max_length=255)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.name} Num car {self.number}"


class Driver(models.Model):
    first_name = models.CharField("First Name", max_length=200, null=True)
    last_name = models.CharField("Last Name", max_length=200, null=True)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
