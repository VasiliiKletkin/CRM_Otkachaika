# Generated by Django 4.1.4 on 2023-07-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0007_remove_region_country_remove_street_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='address',
            name='city_fias_id',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код города'),
        ),
        migrations.AddField(
            model_name='address',
            name='city_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип города (сокращенный)'),
        ),
        migrations.AddField(
            model_name='address',
            name='city_type_full',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип города'),
        ),
        migrations.AddField(
            model_name='address',
            name='city_with_type',
            field=models.CharField(blank=True, max_length=131, null=True, verbose_name='Город с типом'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='address',
            name='country_iso_code',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='ISO-код страны'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Регион'),
        ),
        migrations.AddField(
            model_name='address',
            name='region_fias_id',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код региона'),
        ),
        migrations.AddField(
            model_name='address',
            name='region_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип региона (сокращенный)'),
        ),
        migrations.AddField(
            model_name='address',
            name='region_type_full',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип региона '),
        ),
        migrations.AddField(
            model_name='address',
            name='region_with_type',
            field=models.CharField(blank=True, max_length=131, null=True, verbose_name='Регион с типом'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Улица'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_fias_id',
            field=models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код улицы'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип улицы (сокращенный)'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_type_full',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип улицы'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_with_type',
            field=models.CharField(blank=True, max_length=131, null=True, verbose_name='Улица с типом'),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(default='address1', max_length=500, verbose_name='Полное название адреса'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='address',
            name='uid',
            field=models.CharField(max_length=100, unique=True, verbose_name='Уникальный номер адреса'),
        ),
    ]
