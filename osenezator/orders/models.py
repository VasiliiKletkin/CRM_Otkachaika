from django.utils import timezone
from clients.models import Address
from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField

user_model = get_user_model()

class Order(models.Model):
    CONFIRMATION = 'CONFIRMATION'
    CONFIRMED = 'CONFIRMED'
    INPROGRESS = 'INPROGRESS'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'

    STATUS = Choices(
        (CONFIRMATION, 'Подтверждение'),
        (CONFIRMED, 'Подтвержден'),
        (INPROGRESS, 'Выполняется'),
        (COMPLETED, 'Выполнен'),
        (CANCELED, 'Отменен'),
    )

    status = StatusField("Статус", default=CONFIRMED)
    driver = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders')
    dispatcher = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='orders_dispatcher')
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_planned = models.DateTimeField("Планируемая дата выполнения", null=True, blank=True, default=timezone.now)
    date_start = MonitorField("Дата начала выполнения", monitor='status', when=[INPROGRESS], null=True, blank=True, default=None, editable=False)
    date_completed = MonitorField("Дата завершения", monitor='status', when=[COMPLETED], null=True, blank=True, default=None, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders')


    class Meta:
        verbose_name ='Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order id:{self.id} {self.address} {self.price} - {self.get_status_display()}'
