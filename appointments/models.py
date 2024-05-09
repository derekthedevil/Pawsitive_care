from django.db import models

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