from crm.celery import app
from .models import Client
from datetime import datetime, timedelta
from django.db.models import F


@app.task
def check_active_clients():
    dead_datetime = datetime.now() - timedelta(weeks=24)
    Client.objects.filter(
        is_active=True, statistics__last_completed_order__date_completed__lt=dead_datetime
    ).update(is_active=False)


# @app.task
# def send_active_clients_for_billing():
#     end_datetime = datetime.now() - timedelta(days=7)
#     clients = Client.objects.filter(
#         active=True,
#         statistics__last_order__date_completed__gt=end_datetime
#         - timedelta(days=F("statistics__average_days_orders")),
#     )
#     # for client in clients:
#     #     client.send
