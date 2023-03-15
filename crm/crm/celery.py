import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')

app = Celery('crm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat Settings

# app.conf.beat_schedule = {

#     "periodic_add_numbers": {

#         "task": "orders.tasks.add_numbers",
#         "schedule": crontab(minute="*\1"),

#     },
# }

@app.task(bind=True)
def debug_task(self):
    print(f"HELLO FROM DEBUG")