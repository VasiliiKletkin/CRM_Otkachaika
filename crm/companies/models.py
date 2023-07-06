from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from djmoney.models.fields import MoneyField


class Company(models.Model):
    name = models.CharField("Название компании", max_length=255)
    is_active = models.BooleanField("Активный", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

        indexes = [
            models.Index(name="company_name_idx", fields=["name"]),
            models.Index(name="company_is_active_idx", fields=["is_active"]),
        ]

    def __str__(self):
        return f"{self.name}"


class CompanyWorkPlace(models.Model):
    company = models.OneToOneField(
        Company,
        related_name="work_place",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Область куда агрегатор будет добавлять заказы"
        verbose_name_plural = "Области куда агрегатор будет добавлять заказы"

    def __str__(self):
        return f"{self.id}"


class CompanyAccounting(models.Model):
    company = models.OneToOneField(Company, related_name="accounting", on_delete=models.CASCADE)
    balance = MoneyField("Баланс", max_digits=10, decimal_places=2, default_currency="RUB", default=0)

    class Meta:
        verbose_name = "Аккаунтинг"
        verbose_name_plural = "Аккаунтинг"

    def __str__(self):
        return f"{self.id}"


class CompanySubscription(models.Model):
    company = models.ForeignKey(Company, verbose_name="Компании", on_delete=models.PROTECT, related_name="subscriptions")
    is_active = models.BooleanField("Активный", default=True,)
    date_subscribed_on = models.DateTimeField("Дата начала подписки", auto_now_add=True)
    date_subscribed_off = models.DateTimeField("Дата истечения подписки")
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    service = GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = "Подписка компании"
        verbose_name_plural = "Подписки компаний"

    indexes = [
        models.Index(name="company_subscription_date_subscribed_off_idx", fields=["date_subscribed_off"]),
        models.Index(name="company_subscription_is_active_idx", fields=["is_active"]),
    ]

    def __str__(self):
        return f"{self.id}"
