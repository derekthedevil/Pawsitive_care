from django.shortcuts import render,redirect
from products.models import ProductTable
from user.models import Cart_Table,User_info
from django.contrib import messages
from django.db.models import Q

# Create your views here.
products = ProductTable.objects.filter(is_available =True)
def products(request):
    data = {}
    if request.user.is_authenticated :
        user_info = User_info.objects.get(user_id=request.user.id)
        data['user_info'] = user_info
    products = ProductTable.objects.filter(is_available =True)
    data['products'] = products
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
    

def filter_category(request,str=None):
    data ={}
    q1 = Q(is_available=True)
    q2 = Q(category=str)
    products = ProductTable.objects.filter(is_available =True)
    global filtered_products
    filtered_products = products.filter(q1 & q2)
    data['products'] = filtered_products
    return render(request,"products/products.html",context=data)


def sort_by_price(request,sort_value):
    data ={}
    if sort_value == 'asc' :
        sorted_products = filtered_products.filter(is_available=True).order_by('price')
    else :
        sorted_products = filtered_products.filter(is_available=True).order_by('-price')
    data['products'] = sorted_products
    return render(request,"products/products.html",context=data)