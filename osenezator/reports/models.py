from django.db import models
from companies.models import Company


class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_summ  = models.DecimalField(max_digits=10, decimal_places=2)
    count_orders = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return f'report:{self.id}, company:{self.company}'