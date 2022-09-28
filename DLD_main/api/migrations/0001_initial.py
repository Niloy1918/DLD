# Generated by Django 4.1.1 on 2022-09-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.CharField(blank=True, max_length=1000)),
                ('inflow', models.CharField(blank=True, max_length=1000)),
                ('outflow', models.CharField(blank=True, max_length=1000)),
                ('inPressure', models.CharField(blank=True, max_length=1000)),
                ('outPressure', models.CharField(blank=True, max_length=1000)),
                ('temperature', models.CharField(blank=True, max_length=1000)),
                ('differential', models.CharField(blank=True, max_length=1000)),
                ('offset', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Device Informations',
            },
        ),
    ]
