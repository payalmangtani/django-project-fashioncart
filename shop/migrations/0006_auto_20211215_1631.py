# Generated by Django 3.2.5 on 2021-12-15 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=111),
        ),
    ]
