from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'home.html')

def user_register(request):
    data={}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        uname=request.POST['username']
        upass=request.POST['password']
        uconf_pass=request.POST['password2']
        if(uname=='' or upass=='' or uconf_pass==''):
            data['error_msg']="fields cant be empty"
            return render(request,'user/register.html',context=data)
        elif(upass!=uconf_pass):
            data['error_msg']="passwords does not matched"
            return render(request,'user/register.html',context=data)
        elif(User.objects.filter(username=uname).exists()):
            data['error_msg']=uname + " alredy exist"
            return render(request,'user/register.html',context=data)
        else:  
            new_user=User.objects.create(username=uname)
            new_user.set_password(upass)
            new_user.save()
            return redirect('/')
    return render(request,'user/register.html')

def user_login(request):
    data={}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        uname=request.POST['username']
        upass=request.POST['password']
        if(uname=='' or upass==''):
            data['error_msg']="fields cant be empty"
            return render(request,'user/login.html',context=data)
        elif(not User.objects.filter(username=uname).exists()):
            data['error_msg']=uname + " does not exist"
            return render(request,'user/login.html',context=data)
        else:  
            user=authenticate(username=uname,password=upass)
            print(user)
            if user is None:
                data['error_msg']="Invalid passowrd"
                return render(request,'user/login.html',context=data)
            else:
                login(request,user)
                return redirect('/')
    return render(request,'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')