# Generated by Django 2.2 on 2020-03-28 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_auto_20200328_1046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='pelak',
        ),
    ]