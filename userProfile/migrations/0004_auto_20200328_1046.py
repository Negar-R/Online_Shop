# Generated by Django 2.2 on 2020-03-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0003_delete_userprofileadvance'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('pelak', models.SmallIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.ManyToManyField(related_name='addresses', related_query_name='add', to='userProfile.UserAddress'),
        ),
    ]
