# Generated by Django 4.1.1 on 2022-10-26 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_informationlog_deviceinformation_devicename'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InformationLog',
        ),
    ]
