# Generated by Django 5.0.6 on 2024-05-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_info_address_alter_user_info_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='images'),
        ),
    ]