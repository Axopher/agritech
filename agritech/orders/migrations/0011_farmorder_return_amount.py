# Generated by Django 4.0.3 on 2023-06-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_farmorder_vendors'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmorder',
            name='return_amount',
            field=models.IntegerField(default=0),
        ),
    ]
