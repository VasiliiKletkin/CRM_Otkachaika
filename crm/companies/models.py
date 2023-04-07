from addresses.models import City, Country
from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from model_utils import Choices
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField('Название компании', max_length=255)
    phone_number = PhoneNumberField('Телефонный номер')
    country = models.ForeignKey(
        Country, on_delete=models.PROTECT, verbose_name='Страна', related_name='companies')
    work_of_cities = models.ManyToManyField(
        City, verbose_name='Города или Населенные пункты из которых принимаются заказы', related_name='companies')
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    balance = MoneyField('Баланс', max_digits=10,
                         decimal_places=2, default_currency='RUB', default=0)
    is_active = models.BooleanField('Активный', default=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

        indexes = [
            models.Index(name="company_name_idx", fields=['name']),
        ]

    def __str__(self):
        return f"{self.name}"


class ServiceCompany(models.Model):
    MONTH = "ONE_MONTH"
    THREE_MONTHS = "THREE_MONTHS"
    SIX_MONTHS = "SIX_MONTHS"
    TWELVE_MONTHS = "TWELVE_MONTHS"

    PERIOD = Choices(
        (MONTH, '1 Месяц'),
        (THREE_MONTHS, '3 Месяца'),
        (SIX_MONTHS, '6 Месяцев'),
        (TWELVE_MONTHS, '12 Месяцев'),
    )

    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    period = models.CharField("Период", max_length=50,
                              choices=PERIOD, default=MONTH)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"{self.title} {self.get_period_display()}"


class SubscriptionCompany(models.Model):
    company = models.ForeignKey(Company, verbose_name="Компании",
                                on_delete=models.PROTECT, related_name='subscriptions')
    service = models.ForeignKey(ServiceCompany, verbose_name="Услуга",
                                on_delete=models.PROTECT, related_name='subscriptions')
    is_active = models.BooleanField("Активный", default=True)
    subscribed_on = models.DateTimeField(
        "Дата начала подписки", auto_now_add=True)
    expiring_on = models.DateTimeField("Дата истечения подписки")

    class Meta:
        verbose_name = "Подписка компании"
        verbose_name_plural = "Подписки компаний"

    indexes = [
        models.Index(name="subscription_company_is_active_idx",
                     fields=['is_active']),
    ]

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            if self.service.period == ServiceCompany.MONTH:
                self.expiring_on = timezone.now() + relativedelta(days=30)
            elif self.service.period == ServiceCompany.THREE_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=3)
            elif self.service.period == ServiceCompany.SIX_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=6)
            elif self.service.period == ServiceCompany.TWELVE_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=12)
        return super().save(*args, **kwargs)
