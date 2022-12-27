from django.db import models


class Driver(models.Model):
    first_name = models.CharField("First Name", max_length=200, null=True)
    last_name = models.CharField("Last Name", max_length=200, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
