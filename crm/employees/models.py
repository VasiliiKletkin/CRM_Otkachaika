from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Driver(User):
    class Meta:
        proxy = True
        verbose_name = "Водителя"
        verbose_name_plural = "Водители"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Dispatcher(User):
    class Meta:
        proxy = True
        verbose_name = "Диспетчера"
        verbose_name_plural = "Диспетчеры"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Owner(User):
    class Meta:
        proxy = True
        verbose_name = "Владельца"
        verbose_name_plural = "Владельцы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    name = models.CharField("Название", max_length=255)
    number = models.CharField("Регистрационный номер", max_length=255)
    driver = models.OneToOneField(
        User, on_delete=models.SET_NULL, related_name='car', null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.PROTECT, related_name='cars')

    class Meta:
        verbose_name = "Машину"
        verbose_name_plural = "Машины"

    def __str__(self):
        return f"{self.name}, {self.number}"
