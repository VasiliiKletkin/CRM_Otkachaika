# Generated by Django 4.1.4 on 2023-02-16 19:42

from django.db import migrations, models
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_address_alter_order_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='updated',
        ),
        migrations.AddField(
            model_name='order',
            name='date_planned',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Планируемая дата выполнения'),
        ),
        migrations.AddField(
            model_name='order',
            name='date_start',
            field=model_utils.fields.MonitorField(blank=True, default=None, editable=False, monitor='status', null=True, verbose_name='Дата начала выполнения', when={'INPROGRESS'}),
        ),
    ]