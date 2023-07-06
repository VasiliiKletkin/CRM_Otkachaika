from datetime import timedelta

from addresses.models import Address
from companies.models import Company
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Компания", related_name="clients")
    first_name = models.CharField("Имя", max_length=200, null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=200, null=True, blank=True)
    phone_number = PhoneNumberField("Телефонный номер")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name="Адрес", related_name="clients")
    is_active = models.BooleanField("Активный", default=True)
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        indexes = [
            models.Index(name="client_is_active_idx", fields=["is_active"]),
        ]

    def __str__(self):
        client_display = f"{self.phone_number}"
        if self.first_name:
            client_display += f" {self.first_name}"
        if self.last_name:
            client_display += f" {self.last_name}"
        return client_display

    def get_url_phone_number(self):
        return f"tel:{self.phone_number}"

    def update_data(self):
        self.statistics.update_statistics()
        self.analytics.update_analytics()


class ClientBilling(Client):
    class Meta:
        proxy = True
        verbose_name = "Биллинг Клиента"
        verbose_name_plural = "Биллинг Клиентов"


from orders.models import Order


class ClientStatistics(models.Model):
    client = models.OneToOneField(Client, verbose_name="Клиент", related_name="statistics", on_delete=models.CASCADE)
    first_completed_order = models.ForeignKey(Order, on_delete=models.SET_NULL, verbose_name="Первый выполненный заказ", related_name="first_statistics", null=True, blank=True)
    last_completed_order = models.ForeignKey(Order, on_delete=models.SET_NULL, verbose_name="Последний выполненный заказ", related_name="last_statistics", null=True, blank=True)
    count_completed_orders = models.IntegerField("Колл-во выполненных заказов", null=True, blank=True)

    class Meta:
        verbose_name = "Статистика клиента"
        verbose_name_plural = "Статистика клиентов"

    def __str__(self):
        return f"{self.client}"

    def update_statistics(self):
        completed_orders = self.client.orders.filter(status=Order.COMPLETED)
        self.last_completed_order = completed_orders.last()
        self.first_completed_order = completed_orders.first()
        self.count_completed_orders = completed_orders.count()
        self.save()


class ClientAnalytics(models.Model):
    client = models.OneToOneField(Client, verbose_name="Клиент", related_name="analytics", on_delete=models.CASCADE)
    average_quantity_days_for_order = models.IntegerField("Среднее колл-во дней для одного заказа", null=True, blank=True)
    date_planned_next_order = models.DateTimeField("Планируемая дата следующего заказа", null=True, blank=True)

    class Meta:
        verbose_name = "Аналитика клиента"
        verbose_name_plural = "Аналитика клиентов"

    def __str__(self):
        return f"{self.client}"

    def update_analytics(self):
        statistics = self.client.statistics
        if statistics.count_completed_orders > 1:
            last_completed_order = statistics.last_completed_order
            first_completed_order = statistics.first_completed_order

            # old version
            # completed_orders = self.client.orders.filter(status=Order.COMPLETED)
            # last_completed_order = completed_orders.last()
            # first_completed_order = completed_orders.first()

            all_date = (
                last_completed_order.date_completed
                - first_completed_order.date_completed
            )
            self.average_quantity_days_for_order = all_date.days // (
                statistics.count_completed_orders - 1
            )
            self.date_planned_next_order = (
                last_completed_order.date_completed
                + timedelta(days=self.average_quantity_days_for_order)
            )
            self.save()
