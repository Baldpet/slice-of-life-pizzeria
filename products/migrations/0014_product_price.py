# Generated by Django 3.1.4 on 2021-02-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_dough_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
