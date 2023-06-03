import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

app = Celery('crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# # Celery Beat Settings

# app.conf.beat_schedule = {

#     "auto_send_oreders": {
#         "task": "",
#         "schedule": crontab(minute="15"),
#     },
# }