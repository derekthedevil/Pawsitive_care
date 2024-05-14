# Generated by Django 3.1 on 2024-05-10 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('pincode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('pet_id', models.AutoField(primary_key=True, serialize=False)),
                ('pet_name', models.CharField(max_length=10)),
                ('pet_type', models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Hamster', 'Hamster')], max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('owner_id', models.ForeignKey(db_column='owner_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
