# Generated by Django 3.1.6 on 2021-02-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210211_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geolocation',
            name='ip_address',
            field=models.CharField(max_length=100, unique=True, verbose_name='API adress or URL'),
        ),
    ]
