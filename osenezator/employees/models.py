from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models

user_model = get_user_model()


class Driver(user_model):
    class Meta:
        proxy = True
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    name = models.CharField("Название машины", max_length=255)
    number = models.CharField("Номер авто", max_length=255)
    driver = models.OneToOneField(
        user_model, on_delete=models.SET_NULL, related_name='car', null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='cars')

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return f"{self.name}, {self.number}"


class Dispatcher(user_model):
    class Meta:
        proxy = True
        verbose_name = "Диспетчер"
        verbose_name_plural = "Диспетчеры"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Owner(user_model):
    class Meta:
        proxy = True
        verbose_name = "Владелец"
        verbose_name_plural = "Владельцы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
