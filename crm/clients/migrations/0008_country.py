# Generated by Django 4.1.4 on 2023-03-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_city_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Страну',
                'verbose_name_plural': 'Страны',
            },
        ),
    ]