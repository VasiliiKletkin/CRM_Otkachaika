# Generated by Django 4.1.4 on 2023-07-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Полное название адреса')),
                ('uid', models.CharField(max_length=100, unique=True, verbose_name='Уникальный номер адреса')),
                ('country', models.CharField(blank=True, max_length=120, null=True, verbose_name='Страна')),
                ('country_iso_code', models.CharField(blank=True, max_length=2, null=True, verbose_name='ISO-код страны')),
                ('region_fias_id', models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код региона')),
                ('region_with_type', models.CharField(blank=True, max_length=131, null=True, verbose_name='Регион с типом')),
                ('region_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип региона (сокращенный)')),
                ('region_type_full', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип региона ')),
                ('region', models.CharField(blank=True, max_length=120, null=True, verbose_name='Регион')),
                ('city_fias_id', models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код города')),
                ('city_with_type', models.CharField(blank=True, max_length=131, null=True, verbose_name='Город с типом')),
                ('city_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип города (сокращенный)')),
                ('city_type_full', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип города')),
                ('city', models.CharField(blank=True, max_length=120, null=True, verbose_name='Город')),
                ('street_fias_id', models.CharField(blank=True, max_length=36, null=True, verbose_name='ФИАС-код улицы')),
                ('street_with_type', models.CharField(blank=True, max_length=131, null=True, verbose_name='Улица с типом')),
                ('street_type', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тип улицы (сокращенный)')),
                ('street_type_full', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип улицы')),
                ('street', models.CharField(blank=True, max_length=120, null=True, verbose_name='Улица')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.AddIndex(
            model_name='address',
            index=models.Index(fields=['uid'], name='address_uid_idx'),
        ),
    ]
