# Generated by Django 4.0.3 on 2023-06-23 06:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0035_project_collected_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statuses', to='ecom.project')),
            ],
            options={
                'verbose_name': 'project status',
                'verbose_name_plural': 'project statuses',
            },
        ),
    ]
