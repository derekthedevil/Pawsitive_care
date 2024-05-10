from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_info(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class Pets(models.Model):
    pet_choice = (
        ("Dog","Dog"),
        ("Cat","Cat"),
        ("Bird","Bird"),
        ("Hamster","Hamster"),
    )
    gender_choice = (
        ("Male","Male"),
        ("Female","Female"),
    )
    pet_id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE,db_column="owner_id")
    pet_name = models.CharField(max_length=10)
    pet_type = models.CharField(max_length=10,choices=pet_choice)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=gender_choice)