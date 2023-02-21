from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models
from users.models import Profile

user_model = get_user_model()


class Driver(user_model):
    class Meta:
        proxy = True
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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


class Car(models.Model):
    name = models.CharField("Название", max_length=255)
    number = models.CharField("Регистрационный номер", max_length=255)
    driver = models.OneToOneField(
        user_model, on_delete=models.SET_NULL, related_name='car', null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='cars')

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return f"{self.name}, {self.number}"


class Telegram(models.Model):
    telegram_id = models.CharField("Telegram id", max_length=50)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Telegram"
        verbose_name_plural = "Telegram"

    def __str__(self):
        return f"{self.telegram_id}, {self.profile}"
