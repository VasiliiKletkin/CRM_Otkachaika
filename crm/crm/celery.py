import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

app = Celery('crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Settings

app.conf.beat_schedule = {

    "check_active_clients": {
        "task": "check_active_clients",
        "schedule": crontab(day_of_week=6, minute=0, hour=0),
    },

    "check_company_subscriptions":{
        "task": "check_company_subscriptions",
        "schedule": crontab(minute=0, hour=0),
    }
}