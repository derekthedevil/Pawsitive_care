from django.shortcuts import render,redirect
from products.models import ProductTable,Payment_history,Order_history
from user.models import Cart_Table,User_info
from django.contrib import messages
from django.db.models import Q

# Create your views here.
products = ProductTable.objects.filter(is_available =True)
def products(request):
    data={}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    global filtered_products
    products=ProductTable.objects.filter(is_available=True)
    filtered_products=products
    data['products']=products
    return render(request,'products/products.html',context=data)


def add_to_cart(request,product_id):
    
    if request.user.is_authenticated:
        user = request.user
        product = ProductTable.objects.get(id=product_id)
        q1 = Q(uid=user.id)
        q2 = Q(pid=product_id)
        cart_value = Cart_Table.objects.filter(q1 & q2)
        if (cart_value.count()>0):
            messages.error(request,"Product is already in the cart ")
        else:
            cart = Cart_Table.objects.create(uid=user,pid=product,quantity=1)
            cart.save()
            messages.success(request,"Product is added to the cart ")
        return redirect('/products')
    else:
        return redirect("/login") 
    


def filter_by_category(request,category_value):
    data={}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    q1 = Q(is_available=True)
    q2 = Q(category=category_value)
    # global products
    global filtered_products
    filtered_products=ProductTable.objects.filter(q1 & q2)
    data['products']=filtered_products
    return render(request,'products/products.html',context=data)

def sort_by_price(request,sort_value):
    data={}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    global filtered_products
    if(sort_value=='asc'):
        sorted_products=filtered_products.filter(is_available=True).order_by('price')
    else:
        sorted_products=filtered_products.filter(is_available=True).order_by('-price')
    data['products']=sorted_products
    return render(request,'products/products.html',context=data)

def search_by_price_range(request):
    print("in search")
    data={}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    min=request.POST['min']
    max=request.POST['max']
    q1 = Q(is_available=True)
    q2 = Q(price__gte=min)
    q3 = Q(price__lte=max)
    searched_products = filtered_products.filter(q1 & q2 & q3)
    data['products']=searched_products
    return render(request,'products/products.html',context=data)


def order(request,payment_id,amount):
    pay = Payment_history.objects.create(id=payment_id,user_id=request.user,amount=amount)
    cart = Cart_Table.objects.filter(uid =request.user.id )
    user_info = User_info.objects.get(user_id=request.user.id)
    for i in cart :
        order = Order_history.objects.create(payment_id=pay,uid=request.user,product_id=i.pid,address=user_info.address,quantity=i.quantity,price=i.quantity * i.pid.price)
    cart.delete()
    return redirect("/user/general")