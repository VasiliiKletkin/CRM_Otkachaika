# Generated by Django 4.1.4 on 2022-12-29 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('drivers', '0003_alter_driver_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Last Name'),
        ),
    ]