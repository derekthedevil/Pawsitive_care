# Generated by Django 3.1 on 2024-05-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_auto_20240509_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_9AM_to_10AM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_1', default='available', max_length=15),
        ),
    ]