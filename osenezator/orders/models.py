from django.db import models
from drivers.models import Driver
from clients.models import Client
from companies.models import Company
from model_utils import Choices


class Order(models.Model):
    CONFIRMATION = 'CONFIRMATION'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    ORDER_STATUSES = Choices(
        (CONFIRMATION, 'Confirmation'),
        (INPROGRESS, 'Inprogress'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Canceled'),
    )

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='orders')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    price = models.DecimalField("Price", max_digits=8, decimal_places=2)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    date_complited = models.DateTimeField("Date complited", auto_now_add=True)
    updated = models.DateTimeField("Date updated", auto_now=True)
    status = models.CharField("Status", max_length=20, choices=ORDER_STATUSES, default=CONFIRMATION)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders')


    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order {self.driver}, {self.client}, {self.price}, {self.status}'
