from companies.models import Company
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .consts import ONE_MONTH, PERIOD


class AbstractBaseService(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", null=True, blank=True)
    period = models.CharField("Период", max_length=50,
                              choices=PERIOD, default=ONE_MONTH)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    subscriptions = GenericRelation(Company)

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"
        abstract = True

    def __str__(self):
        return f"{self.title} {self.get_period_display()}"


class CompanyServiceCRM(AbstractBaseService):
    class Meta:
        verbose_name = "Услугу CRM"
        verbose_name_plural = "Услуги CRM"


class CompanyServiceAggregation(AbstractBaseService):    
    class Meta:
        verbose_name = "Услугу Агрегатора"
        verbose_name_plural = "Услуги Агрегатора"
