from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField('Название компании', max_length=255)
    phone_number = PhoneNumberField()
    city = models.CharField('Город', max_length=255, null=True, blank=True)
    country = models.CharField('Страна', max_length=255, null=True, blank=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"
