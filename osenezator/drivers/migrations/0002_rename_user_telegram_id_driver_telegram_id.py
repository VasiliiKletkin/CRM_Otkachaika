# Generated by Django 4.1.4 on 2023-01-01 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='user_telegram_id',
            new_name='telegram_id',
        ),
    ]
