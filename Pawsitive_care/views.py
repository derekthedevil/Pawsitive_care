from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from user.models import Cart_Table,User_info,Pets
from products.models import Order_history,Payment_history
from appointments.models import User_App
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random

def home(request):
    data ={}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    return render(request,'home.html',context=data)

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
            User_info.objects.create(user_id=new_user)
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
            if user is None:
                data['error_msg']="Invalid passowrd"
                return render(request,'user/login.html',context=data)
            else:
                login(request,user)
                if user.is_superuser :
                        return redirect('/adminpannel/admin')
                return redirect('/')
    return render(request,'user/login.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def find_cart_value(request):
    user_id = request.user.id
    cart=Cart_Table.objects.filter(uid=user_id)
    cart_count=cart.count()
    return cart_count


import razorpay
def cart(request):
    data1={}
    total_items = 0
    total_price = 0
    cart_count=find_cart_value(request)
    data1['cartvalue']=cart_count
    products_in_cart=Cart_Table.objects.filter(uid=request.user.id)
    data1['cartproducts']=products_in_cart
    for product in products_in_cart :
        total_items += product.quantity
        total_price += product.pid.price * product.quantity
    data1['total_items'] = total_items
    data1['total_price'] = total_price
    if total_price>1 :
        client = razorpay.Client(auth=("rzp_test_97GJ2rvcYmtUV6", "N0lPf0ifPlzeBdQRyueMNDOJ"))
        data = { "amount": int((total_price)*100), "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
    return render(request,'home/cart.html',context=data1)


def delete(request,cart_id):
    cart = Cart_Table.objects.get(id=cart_id)
    cart.delete()
    return redirect("/cart")

def cart_update(request,cart_id,update):
    cart = Cart_Table.objects.get(id=cart_id)
    if update == "inc" :
        cart.quantity += 1
        cart.save()
    else :
        if cart.quantity == 1 :
            cart.delete()
        else :
            cart.quantity -= 1 
            cart.save()
    return redirect("/cart")

def user_settings(request):
    return render(request,"user/user_setting.html")

def generel_settings(request):
    user_id = request.user.id 
    user = User.objects.get(id=user_id)
    data={}
    user_info = User_info.objects.get(user_id=user_id)
    data['user_info'] = user_info
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST['email']
        phone = request.POST['phone']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pincode = request.POST['pincode']
        address = request.POST['address']
        user.username = username
        user.email = email
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        user_info = User_info.objects.get(user_id=user_id)
        user_info.phone = phone
        user_info.pincode = pincode
        user_info.address = address
        if 'image' in request.FILES :
            user_info.image = request.FILES['image']
        user_info.save()
        data['user_info'] = user_info
    
    return render(request,"user/general_settings.html",context=data)

def addpets(request):
    data={}
    data['pets'] =Pets.objects.filter(owner_id=request.user.id)
    user_info = User_info.objects.get(user_id=request.user.id)
    data['user_info'] = user_info
    if request.method=="POST" :
        name = request.POST['name']
        gender = request.POST['gender']
        age = request.POST['age']
        type= request.POST['type']
        Pets.objects.create(pet_name=name,pet_type=type,age=age,gender=gender,owner_id=request.user)
    return render(request,"user/pets.html", context=data)

def app_history(request):
    data = {}
    data['apps'] = User_App.objects.filter(user_id=request.user.id).order_by('Booked_date')
    data['user_info'] = User_info.objects.get(user_id=request.user.id)
    return render(request,"user/app_history.html",context=data)


def updatepass(request):
    if not request.user.is_authenticated :
        return redirect("/login")
    else:
        data ={}
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
        if request.method == "POST" :
            oldpass = request.POST['old']
            newpass = request.POST['new']
            confnew = request.POST['conf_new']
            user=authenticate(username=request.user.username,password=oldpass)
            if user is None :
                data['error'] = "Old password is incorrect"
                return render(request,"user/editpassword.html",context=data)
            else :
                if newpass != confnew :
                    data['error'] = "new passwords do not match"
                    return render(request,"user/editpassword.html",context=data)
                else :
                    user.set_password(newpass)
                    user.save()
                    return render(request,"user/general_settings.html",context=data)
    return render(request,"user/editpassword.html",context=data)
    
    

def order_history(request):
    list1 = []
    data ={}
    payments = Payment_history.objects.filter(user_id=request.user.id)
    if payments != None :
        for i in payments :
            orders = Order_history.objects.filter(payment_id=i.id)
            list1.append(orders)
        data["orders"] = list1
    else :
        pass
    return render(request,"user/order_history.html",context=data)

def forgot_password(request):
    if request.method == "POST" :
        uname = request.POST['username']
        if User.objects.filter(username=uname).exists() :
            user = User.objects.get(username=uname)
            url = "forgotpassword/update/" + user.username
            global otp
            otp = random.randint(1111,9999)
            send_mail(
    "otp for password change - Pawsitive care" ,
    "Your otp is " + str(otp),
    settings.EMAIL_HOST_USER,
    [user.email],
    fail_silently=False,)
            return redirect(url)
    return render(request,"user/forgotpassword.html")


def passotp(request,uname):
    user = User.objects.get(username=uname)
    data = {}
    if request.method == "POST":
        uotp = request.POST['otp']
        uotp = int(uotp)
        password = request.POST['password']
        confpass = request.POST['confpass']
        global otp
        if uotp != otp :
            print(uotp,type(uotp),otp,type(otp))
            data['error'] = "otp does not match"
        elif password != confpass :
            data['error'] = "passwords do not match"
        elif uotp == otp and password == confpass : 
            user.set_password(password)
            user.save()
            otp = None 
            return redirect("/login")
    return render(request,"user/otppass.html",context=data)