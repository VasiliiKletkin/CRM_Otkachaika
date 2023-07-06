from datetime import datetime

from crm.celery import app

from .models import CompanySubscription


@app.task
def check_company_subscriptions():
    subscription = CompanySubscription.objects.filter(date_subscribed_off__lte=datetime.now()).update(is_active=False)
