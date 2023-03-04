# Generated by Django 4.1.4 on 2023-02-16 17:40

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_completed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='Дата завершения', when={'COMPLETED'}),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=model_utils.fields.StatusField(choices=[('CONFIRMATION', 'Подтверждение'), ('INPROGRESS', 'Выполняется'), ('COMPLETED', 'Выполнен'), ('CANCELED', 'Отменен')], default='CONFIRMATION', max_length=100, no_check_for_status=True, verbose_name='Статус'),
        ),
    ]