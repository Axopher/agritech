# Generated by Django 4.0.3 on 2023-06-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_remove_vendor_vendor_name'),
        ('orders', '0009_order_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmorder',
            name='vendors',
            field=models.ManyToManyField(blank=True, to='vendor.vendor'),
        ),
    ]
