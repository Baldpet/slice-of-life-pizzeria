# Generated by Django 3.1.4 on 2021-02-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210216_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='dough',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
