# Generated by Django 2.2 on 2020-01-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20200130_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeappliance',
            name='color',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='homeappliance',
            name='weight',
            field=models.SmallIntegerField(null=True),
        ),
    ]