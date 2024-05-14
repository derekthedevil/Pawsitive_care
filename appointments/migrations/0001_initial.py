# Generated by Django 3.1 on 2024-05-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentsSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('slot_9AM_to_10AM', models.BooleanField(default=True)),
                ('slot_10AM_to_11AM', models.BooleanField(default=True)),
                ('slot_11AM_to_12PM', models.BooleanField(default=True)),
                ('slot_1PM_to_2PM', models.BooleanField(default=True)),
                ('slot_2PM_to_3PM', models.BooleanField(default=True)),
                ('slot_4PM_to_5PM', models.BooleanField(default=True)),
                ('slot_5PM_to_6Pm', models.BooleanField(default=True)),
            ],
        ),
    ]