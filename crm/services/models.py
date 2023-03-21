from companies.models import Company
from dateutil.relativedelta import relativedelta
from django.db import models
from django.utils import timezone
from model_utils import Choices


class ServiceProduct(models.Model):
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
        verbose_name = "Услуги для компании"
        verbose_name_plural = "Услуги для компаний"

    def __str__(self):
        return f"{self.title} {self.get_period_display()}"


class SubscriptionCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE)
    is_active = models.BooleanField("Активный", default=True)
    subscribed_on = models.DateTimeField(
        "Дата начала подписки", auto_now_add=True)
    expiring_on = models.DateTimeField("Дата истечения подписки")

    class Meta:
        verbose_name = "Подписка компании"
        verbose_name_plural = "Подписки компаний"

    def __str__(self):
        return f"{self.id}"

    def save(self, *args, **kwargs):
        if not self.id:
            if self.service.period == ServiceProduct.MONTH:
                self.expiring_on = timezone.now() + relativedelta(days=30)
            elif self.service.period == ServiceProduct.THREE_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=3)
            elif self.service.period == ServiceProduct.SIX_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=6)
            elif self.service.period == ServiceProduct.TWELVE_MONTHS:
                self.expiring_on = timezone.now() + relativedelta(month=12)
        return super().save(*args, **kwargs)
