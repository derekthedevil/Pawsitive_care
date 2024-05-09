from django.shortcuts import render,redirect
from appointments.models import AppointmentsSchedule
import datetime
from django.db.models import Q


# Create your views here.
# appointments  = AppointmentsSchedule.objects.none()
last_date =  datetime.date.today() + datetime.timedelta(days=6)
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
    if request.method == "POST":
        date_time_slot = request.POST['date-time-slot']
        slot_list = date_time_slot.split(":")
        app = AppointmentsSchedule.objects.get(date=datetime.datetime.strptime(slot_list[0] ,"%B %d, %Y"))
        
    return render(request,'appointments/appointments.html',context=data)

def next_week(request):
    data = {} 
    date_start = last_date
    data['appointments']=week_fun(date_start)
    if request.method == "POST":
        print("Post method")
    return render(request,'appointments/appointments.html',context=data)

def last_week(request):
    data = {} 
    date_start = last_date - datetime.timedelta(days=14)
    if date_start < datetime.date.today():
        return redirect("/appointments")
    data['appointments']=week_fun(date_start)
    # rand(request)
    if request.method == "POST":
        date_time_slot = request.POST['date-time-slot']
        slot_list = date_time_slot.split(":")
        print(slot_list[1])
        # app = AppointmentsSchedule.objects.get(date=slot_list[1])
        # print(app)
        # print("Post method")
    return render(request,'appointments/appointments.html',context=data)

def rand(request):
    # pet_type = request.POST['pet-type']
    # service = request.POST['service']
    # add_info = request.POST['add-info']
    date_time_slot = request.POST['date-time-slot']
    slot_list = date_time_slot.split(":")
    print(slot_list[1])
    # app = AppointmentsSchedule.objects.get(date=slot_list[1].strftime("%Y-%m-%d"))
    # print(app)
    pass