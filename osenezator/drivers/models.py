from django.db import models

from companies.models import Company


class Driver(models.Model):
    first_name = models.CharField("First Name", max_length=200)
    last_name = models.CharField("Last Name", max_length=200)
    user_telegram_id = models.PositiveIntegerField("Telegram ID")
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
