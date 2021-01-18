# Generated by Django 3.1.4 on 2021-01-18 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210118_1844'),
        ('offers', '0002_auto_20210117_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='offer',
            name='item1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Category_item1', to='products.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(default='test', max_length=254),
            preserve_default=False,
        ),
    ]