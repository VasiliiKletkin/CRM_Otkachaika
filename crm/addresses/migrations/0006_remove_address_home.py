# Generated by Django 4.1.4 on 2023-07-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0005_address_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='home',
        ),
    ]