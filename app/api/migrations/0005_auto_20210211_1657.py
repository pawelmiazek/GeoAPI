# Generated by Django 3.1.6 on 2021-02-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210211_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='continent',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Continent'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='ip_address',
            field=models.CharField(max_length=100, unique=True, verbose_name='IP adress'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='latitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='geolocation',
            name='longitude',
            field=models.FloatField(blank=True, null=True, verbose_name='Longitude'),
        ),
    ]