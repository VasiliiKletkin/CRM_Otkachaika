# Generated by Django 4.1.4 on 2023-03-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceproduct',
            options={'verbose_name': 'Услуги для компании', 'verbose_name_plural': 'Услуги для компаний'},
        ),
        migrations.AlterModelOptions(
            name='subscriptioncompany',
            options={'verbose_name': 'Подписка компании', 'verbose_name_plural': 'Подписки компаний'},
        ),
        migrations.AlterField(
            model_name='serviceproduct',
            name='period',
            field=models.CharField(choices=[('ONE_MONTH', '1 Месяц'), ('THREE_MONTHS', '3 Месяца'), ('SIX_MONTHS', '6 Месяцев'), ('TWELVE_MONTHS', '12 Месяцев')], default='ONE_MONTH', max_length=50, verbose_name='Период'),
        ),
        migrations.AlterField(
            model_name='serviceproduct',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='serviceproduct',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subscriptioncompany',
            name='expiring_on',
            field=models.DateTimeField(verbose_name='Дата истечения подписки'),
        ),
        migrations.AlterField(
            model_name='subscriptioncompany',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='subscriptioncompany',
            name='subscribed_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата начала подписки'),
        ),
    ]