from django.shortcuts import render,redirect
from appointments.models import AppointmentsSchedule,User_App
import datetime
from django.db.models import Q
from user.models import Pets


# Create your views here.

last_date =  datetime.date.today() + datetime.timedelta(days=7)

def set_appointment(request ,date_time_slot):
    user = request.user
    pet = request.POST['pet_type']
    pet = Pets.objects.get(pet_name=pet)
    service = request.POST['service']
    add_info = request.POST['add_info']
    slot_list = date_time_slot.split(":")
    slot_date= datetime.datetime.strptime(slot_list[0] ,"%B %d, %Y")
    app = AppointmentsSchedule.objects.get(date=slot_date)
    setattr(app,slot_list[1],"not_available")
    app.save()
    User_App.objects.create(user_id=user ,Booked_date=slot_date,Slot_time=slot_list[1],pet_id=pet,add_info=add_info)
    app = AppointmentsSchedule.objects.none()

def week_fun(date_start= datetime.date.today()):
    q1 = Q(date__gt = date_start)
    global last_date
    last_date =  date_start + datetime.timedelta(days=7)
    q2 = Q(date__lte =  last_date)
    appointments = AppointmentsSchedule.objects.filter( q1 & q2)
    return appointments

def appointments(request, date_start = datetime.date.today()):
    data = {}
    data['appointments']=week_fun(date_start)
    pets = Pets.objects.filter(owner_id=request.user.id)
    if pets == None :
        data["pet_error"] = "first add your pets to book appointment "
    else :
        data['pets'] = pets
    if request.method == "POST":
        date_time_slot = request.POST['date-time-slot']
        if request.user.is_authenticated :
            set_appointment(request,date_time_slot=date_time_slot)
        else:
            return redirect("/login")
    return render(request,'appointments/appointments.html',context=data)

def next_week(request):
    data = {} 
    date_start = last_date
    data['appointments']=week_fun(date_start)
    if request.method == "POST":
        date_time_slot = request.POST['date-time-slot']
        if request.user.is_authenticated :
            set_appointment(request,date_time_slot=date_time_slot)
        else:
            return redirect("/login")
    return render(request,'appointments/appointments.html',context=data)

def last_week(request):
    data = {} 
    date_start = last_date - datetime.timedelta(days=14)
    if date_start < datetime.date.today():
        return redirect("/appointments")
    data['appointments']=week_fun(date_start)
    if request.method == "POST":
        date_time_slot = request.POST['date-time-slot']
        if request.user.is_authenticated :
            set_appointment(request,date_time_slot=date_time_slot)
        else:
            return redirect("/login")
    return render(request,'appointments/appointments.html',context=data)

