# Generated by Django 4.0.3 on 2023-06-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0036_projectstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='title',
            field=models.CharField(default='Status Update', max_length=100),
        ),
    ]