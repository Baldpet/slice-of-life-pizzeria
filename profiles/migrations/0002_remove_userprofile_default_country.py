# Generated by Django 3.1.4 on 2021-02-16 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_country',
        ),
    ]
