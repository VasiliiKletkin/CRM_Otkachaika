from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    date_created = models.DateTimeField("Date created", auto_now_add=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"
