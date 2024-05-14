# Generated by Django 3.1 on 2024-05-09 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0006_auto_20240509_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_10AM_to_11AM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_2', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_11AM_to_12PM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_3', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_1PM_to_2PM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_4', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_2PM_to_3PM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_5', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_4PM_to_5PM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_6', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_5PM_to_6Pm',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_7', default='available', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointmentsschedule',
            name='slot_9AM_to_10AM',
            field=models.CharField(choices=[('available', 'available'), ('not_available', 'not_available')], db_column='slot_1', default='available', max_length=20),
        ),
    ]
