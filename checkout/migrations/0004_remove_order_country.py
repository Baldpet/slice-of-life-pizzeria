# Generated by Django 3.1.4 on 2021-02-16 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210214_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
    ]
