from django.db import models
from drivers.models import Driver
from clients.models import Address


class Order(models.Model):
    CONFIRMATION = 'CONFIRMATION'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    STATUSES = [
        (CONFIRMATION, 'Confirmation'),
        (INPROGRESS, 'Inprogress'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    ]

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price = models.DecimalField("Price", max_digits=8, decimal_places=2)
    created = models.DateTimeField("Date created", auto_now_add=True)
    updated = models.DateTimeField("Date updated", auto_now=True)
    status = models.CharField("Status", max_length=20,
                              choices=STATUSES, default=CONFIRMATION)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.id}, address {self.address}'
