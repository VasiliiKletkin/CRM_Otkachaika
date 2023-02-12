from django.db import models
from companies.models import Company


class Report(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'report:{self.id}, company:{self.company}'