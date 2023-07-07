# Generated by Django 4.1.4 on 2023-07-07 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Дата начала отчета')),
                ('date_end', models.DateField(verbose_name='Дата конца отчета')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Прибыль')),
                ('count_orders', models.IntegerField(blank=True, null=True, verbose_name='Количество заказов')),
                ('count_new_addresses', models.IntegerField(blank=True, null=True, verbose_name='Количество новых адресов')),
                ('count_new_clients', models.IntegerField(blank=True, null=True, verbose_name='Количество новых клиентов')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.company')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
