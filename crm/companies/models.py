from addresses.models import City, Country, Region, Street
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
    countries = models.ManyToManyField(
        Country,
        verbose_name="Страны из которых принимаются заказы",
        related_name="work_places",
        blank=True,
    )
    regions = models.ManyToManyField(
        Region,
        verbose_name="Регионы из которых принимаются заказы",
        related_name="work_places",
        blank=True,
    )
    cities = models.ManyToManyField(
        City,
        verbose_name="Города или Населенные пункты из которых принимаются заказы",
        related_name="work_places",
        blank=True,
    )
    streets = models.ManyToManyField(
        Street,
        verbose_name="Улицы из которых принимаются заказы",
        related_name="work_places",
        blank=True,
    )

    class Meta:
        verbose_name = "Рабочее пространство для заказов"
        verbose_name_plural = "Рабочее пространство для заказов"

    def __str__(self):
        return f"{self.id}"


class CompanyAccounting(models.Model):
    company = models.OneToOneField(
        Company,
        related_name="accounting",
        on_delete=models.CASCADE,
    )
    balance = MoneyField(
        "Баланс",
        max_digits=10,
        decimal_places=2,
        default_currency="RUB",
        default=0,
    )

    class Meta:
        verbose_name = "Аккаунтинг"
        verbose_name_plural = "Аккаунтинг"

    def __str__(self):
        return f"{self.id}"


# class CompanyService(models.Model):
#     MONTH = "ONE_MONTH"
#     THREE_MONTHS = "THREE_MONTHS"
#     SIX_MONTHS = "SIX_MONTHS"
#     TWELVE_MONTHS = "TWELVE_MONTHS"

#     PERIOD = Choices(
#         (MONTH, "1 Месяц"),
#         (THREE_MONTHS, "3 Месяца"),
#         (SIX_MONTHS, "6 Месяцев"),
#         (TWELVE_MONTHS, "12 Месяцев"),
#     )

#     title = models.CharField("Название", max_length=50)
#     description = models.TextField("Описание", null=True, blank=True)
#     period = models.CharField("Период", max_length=50, choices=PERIOD, default=MONTH)
#     price = models.DecimalField("Цена", max_digits=10, decimal_places=2)

#     class Meta:
#         verbose_name = "Услугу"
#         verbose_name_plural = "Услуги"

#     def __str__(self):
#         return f"{self.title} {self.get_period_display()}"


# class CompanySubscription(models.Model):
#     company = models.ForeignKey(
#         Company,
#         verbose_name="Компании",
#         on_delete=models.PROTECT,
#         related_name="subscriptions",
#     )
#     service = models.ForeignKey(
#         ServiceCompany,
#         verbose_name="Услуга",
#         on_delete=models.PROTECT,
#         related_name="subscriptions",
#     )
#     is_active = models.BooleanField("Активный", default=True)
#     date_subscribed_on = models.DateTimeField("Дата начала подписки", auto_now_add=True)
#     date_subscribed_off = models.DateTimeField("Дата истечения подписки")

#     class Meta:
#         verbose_name = "Подписка компании"
#         verbose_name_plural = "Подписки компаний"

#     indexes = [
#         models.Index(name="subscription_company_is_active_idx", fields=["is_active"]),
#     ]

#     def __str__(self):
#         return f"{self.id}"

#     def save(self, *args, **kwargs):
#         if not self.id:
#             if self.service.period == ServiceCompany.MONTH:
#                 self.date_subscribed_off = timezone.now() + relativedelta(days=30)
#             elif self.service.period == ServiceCompany.THREE_MONTHS:
#                 self.date_subscribed_off = timezone.now() + relativedelta(month=3)
#             elif self.service.period == ServiceCompany.SIX_MONTHS:
#                 self.date_subscribed_off = timezone.now() + relativedelta(month=6)
#             elif self.service.period == ServiceCompany.TWELVE_MONTHS:
#                 self.date_subscribed_off = timezone.now() + relativedelta(month=12)
#         return super().save(*args, **kwargs)
