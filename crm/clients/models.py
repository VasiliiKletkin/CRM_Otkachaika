from addresses.models import Address
from companies.mixins import CompanyMixin
from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(CompanyMixin, models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        verbose_name="Компания",
        related_name="clients",
    )
    first_name = models.CharField("Имя", max_length=200, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField("Телефонный номер")
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        verbose_name="Адрес",
        related_name="clients",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField("Активный", default=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        client_display = f"{self.phone_number}"
        if self.first_name:
            client_display += f" {self.first_name}"
        if self.last_name:
            client_display += f" {self.last_name}"
        return client_display

    def update_client_statistics(self):
        self.client_statistics.update_statistics()


from orders.models import Order


class ClientStatistics(models.Model):
    client = models.OneToOneField(
        Client,
        verbose_name="Клиент",
        related_name="client_statistics",
        on_delete=models.PROTECT,
    )
    first_order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        verbose_name="Первый выполненный заказ",
        related_name="first_client_statistics",
        null=True,
        blank=True,
    )
    last_order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        verbose_name="Последний выполненный заказ",
        related_name="last_client_statistics",
        null=True,
        blank=True,
    )

    count_completed_orders = models.IntegerField(
        "Колл-во выполненных заказов", null=True, blank=True
    )

    average_date_orders = models.IntegerField(
        "Среднее колл-во дней для одного заказа", null=True, blank=True
    )

    class Meta:
        verbose_name = "Данные o клиенте"
        verbose_name_plural = "Данные o клиенте"

    def __str__(self):
        return f"Инфо {self.client}"

    def update_statistics(self):
        completed_orders = self.client.orders.filter(status=Order.COMPLETED)
        self.last_order = completed_orders.last()
        self.first_order = completed_orders.first()
        self.count_completed_orders = completed_orders.count()
        if self.count_completed_orders > 1:
            all_date = self.last_order.date_completed - self.first_order.date_completed
            self.average_date_orders = all_date.days / (self.count_completed_orders - 1)
        self.save()
