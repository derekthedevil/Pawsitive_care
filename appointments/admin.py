from django.contrib import admin
from appointments.models import AppointmentsSchedule,UserApp
# Register your models here.

admin.site.register(AppointmentsSchedule)
admin.site.register(UserApp)