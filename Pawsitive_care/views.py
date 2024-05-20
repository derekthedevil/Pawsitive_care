from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from user.models import Cart_Table,User_info

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