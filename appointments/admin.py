from django.contrib import admin
from appointments.models import AppointmentsSchedule,User_App
# Register your models here.

admin.site.register(AppointmentsSchedule)
admin.site.register(User_App)