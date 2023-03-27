from companies.models import Company
from django.db import models
from django.db.models import Count, Sum
from employees.models import Driver
from orders.models import Order
from clients.models import Client, Address


class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date_start = models.DateField("Дата начала отчета")
    date_end = models.DateField("Дата конца отчета")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    profit = models.DecimalField("Прибыль", max_digits=10, decimal_places=2, blank=True, null=True)
    count_orders = models.IntegerField("Количество заказов", blank=True, null=True)
    count_new_addresses = models.IntegerField("Количество новых адресов", blank=True, null=True)
    count_new_clients = models.IntegerField("Количество новых клиентов", blank=True, null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return f'{self.id}, Date: {self.date_start} - {self.date_end}'

    @property
    def orders(self):
        return Order.objects.filter(company=self.company,
                                    date_created__gte=self.date_start,
                                    date_created__lte=self.date_end)

    @property
    def drivers(self):
        return Driver.objects.filter(profile__company=self.company,
                                    date_created__gte=self.date_start,
                                    date_created__lte=self.date_end
                                     ).annotate(count_orders=Count('orders')
                                                ).annotate(sum_orders=Sum('orders__price'))
    
    def calculate(self):
        # self.profit = self.orders.aggregate(Sum('price'))
        self.count_orders = self.orders.count()
        self.count_new_addresses = Address.objects.filter(clients__company=self.company,
                                                        date_created__gte=self.date_start,
                                                        date_created__lte=self.date_end
                                                        ).count()
        self.count_new_clients = Client.objects.filter(company=self.company,
                                                        date_created__gte=self.date_start,
                                                        date_created__lte=self.date_end
                                                        ).count()
    def save(self, *args, **kwargs):
        self.calculate()
        return super().save(*args, **kwargs)
