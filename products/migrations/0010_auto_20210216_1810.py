# Generated by Django 3.1.4 on 2021-02-16 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210216_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_orignal',
            new_name='is_original',
        ),
    ]
