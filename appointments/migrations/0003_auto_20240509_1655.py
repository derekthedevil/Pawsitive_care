# Generated by Django 3.1 on 2024-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20240509_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_9AM_to_10AM',
            field=models.TextField(choices=[('available', 'available'), ('not_available', 'not_available')]),
        ),
    ]
