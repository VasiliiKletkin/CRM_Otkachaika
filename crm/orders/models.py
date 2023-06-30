import random

from addresses.models import Address
from clients.models import Client
from companies.models import Company
from django.contrib.auth import get_user_model
from django.db import models, transaction
from employees.models import Dispatcher, Driver
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField

from .tasks import send_order_to_driver

User = get_user_model()


class Order(models.Model):
    CONFIRMATION = "CONFIRMATION"
    CONFIRMED = "CONFIRMED"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

    STATUS = Choices(
        (CONFIRMATION, "Подтверждение"),
        (CONFIRMED, "Подтвержден"),
        (INPROGRESS, "Выполняется"),
        (COMPLETED, "Выполнен"),
        (CANCELED, "Отменен"),
    )

    CASH = "CASH"
    CREDIT_CARD = "CREDIT_CARD"
    ONLINE_TRANSFER = "ONLINE_TRANSFER"

    TYPES_PAYMENT = Choices(
        (CASH, "Наличные"),
        (CREDIT_CARD, "Картой"),
        (ONLINE_TRANSFER, "Онлайн перевод"),
    )

    company = models.ForeignKey(
        Company,
        verbose_name="Компания",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="orders",
    )
    status = StatusField("Статус", default=CONFIRMED)
    driver = models.ForeignKey(
        Driver,
        verbose_name="Водитель",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="orders",
    )
    address = models.ForeignKey(
        Address, verbose_name="Адрес", on_delete=models.PROTECT, related_name="orders"
    )
    client = models.ForeignKey(
        Client,
        verbose_name="Клиент",
        on_delete=models.PROTECT,
        related_name="orders",
    )
    created_by = models.ForeignKey(
        Dispatcher,
        verbose_name="Диспетчер",
        on_delete=models.PROTECT,
        related_name="created_orders",
    )
    description = models.TextField("Описание", blank=True, null=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    type_payment = models.CharField(
        "Тип оплаты", max_length=20, choices=TYPES_PAYMENT, default=ONLINE_TRANSFER
    )
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_planned = models.DateTimeField(
        "Планируемая дата выполнения", null=True, blank=True
    )
    date_started = MonitorField(
        "Дата начала выполнения",
        monitor="status",
        when=[INPROGRESS],
        null=True,
        blank=True,
        default=None,
    )
    date_completed = MonitorField(
        "Дата конца выполнения",
        monitor="status",
        when=[COMPLETED],
        null=True,
        blank=True,
        default=None,
    )
    date_canceled = MonitorField(
        "Дата отмены выполнения",
        monitor="status",
        when=[CANCELED],
        null=True,
        blank=True,
        default=None,
    )
    is_sent = models.BooleanField("Отправлен водителю", default=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

        indexes = [
            models.Index(name="order_status_idx", fields=["status"]),
            models.Index(name="order_date_created_idx", fields=["date_created"]),
            models.Index(name="order_is_sent_idx", fields=["is_sent"]),
        ]

    def __str__(self):
        return f"Заказ N{self.id}, {self.address} - {self.get_status_display()}"

    def send_to_driver(self):
        transaction.on_commit(lambda: send_order_to_driver.delay(self.id))

    def start(self):
        self.status = Order.INPROGRESS
        self.save()

    def complete(self):
        self.status = Order.COMPLETED
        self.save()

    def cancel(self):
        self.status = Order.CANCELED
        self.save()


# for Subscriprion
# if not instance.company:
#     instance.company = instance.get_company_with_active_subscription()
#     instance.status = instance.CONFIRMATION

# def get_company_with_active_subscription(self):
#     if companies := Company.objects.filter(
#         # streets=self.address.street,
#         subscriptions__is_active=True
#     ):
#         return random.choice(companies)
