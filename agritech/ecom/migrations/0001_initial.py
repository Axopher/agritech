# Generated by Django 4.0.3 on 2023-05-07 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mob_no', models.IntegerField(max_length=10)),
            ],
        ),
    ]
