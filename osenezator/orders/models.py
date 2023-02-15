from clients.models import Address
from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices

user_model = get_user_model()

class Order(models.Model):
    CONFIRMATION = 'CONFIRMATION'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    ORDER_STATUSES = Choices(
        (CONFIRMATION, 'Подтверждение'),
        (INPROGRESS, 'Выполняется'),
        (COMPLETED, 'Выполнен'),
        (CANCELED, 'Отменен'),
    )

    driver = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')
    dispatcher = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='orders_dispatcher')
    description = models.TextField("Описание",blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_completed = models.DateTimeField("Дата завершения", auto_now_add=True)
    updated = models.DateTimeField("Последняя дата обновления", auto_now=True)
    status = models.CharField("Статус", max_length=20, choices=ORDER_STATUSES, default=CONFIRMATION)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders')


    class Meta:
        verbose_name ='Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order id:{self.id} {self.address} {self.price} - {self.status}'
