# Generated by Django 4.1.4 on 2023-04-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_sent',
            field=models.BooleanField(default=False, verbose_name='Отправлен'),
        ),
    ]
