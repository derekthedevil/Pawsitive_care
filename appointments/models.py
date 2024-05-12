from django.db import models
from django.contrib.auth.models import User
from user.models import Pets
from products.models import ProductTable

# Create your models here.
class AppointmentsSchedule(models.Model):
    date = models.DateField(unique=True)
    choices = (
        ('available','available'),
        ('not_available','not_available')
    )
    slot_9AM_to_10AM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_1")
    slot_10AM_to_11AM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_2")
    slot_11AM_to_12PM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_3")
    slot_1PM_to_2PM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_4")
    slot_2PM_to_3PM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_5")
    slot_4PM_to_5PM = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_6")
    slot_5PM_to_6Pm = models.CharField(max_length=20 ,choices=choices,default="available",db_column="slot_7")
    def __str__(self) :
        str_date = str(self.date)
        return str_date


class User_App(models.Model):
    slot_choice = (
        ("slot_9AM_to_10AM" ,"slot_9AM_to_10AM"),
        ("slot_10AM_to_11AM" ,"slot_10AM_to_11AM"),
        ("slot_11AM_to_12PM" ,"slot_11AM_to_12PM"),
        ("slot_1PM_to_2PM" ,"slot_1PM_to_2PM"),
        ("slot_2PM_to_3PM" ,"slot_2PM_to_3PM"),
        ("slot_4PM_to_5PM" ,"slot_4PM_to_5PM"),
        ("slot_5PM_to_6Pm" ,"slot_5PM_to_6Pm"),
    )
    pet_choice = (
        ("Dog","Dog"),
        ("Cat","Cat"),
        ("Bird","Bird"),
        ("Hamster","Hamster"),
    )
    
    services = (
        ("grooming","Grooming"),
        ("hair_cut","hair_cut"),
        ("nail_cutting","nail_cutting"),
        # ("grooming","Grooming"),
    )
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
    Booked_date = models.DateField()
    Slot_time = models.CharField(max_length=20,choices=slot_choice , db_column="slot_time")
    pet_id = models.ForeignKey(Pets,on_delete=models.CASCADE ,db_column="pet_id")
    add_info = models.CharField(max_length=50)
    

