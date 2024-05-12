from django.shortcuts import render,redirect
from products.models import ProductTable
from user.models import Cart_Table
from django.contrib import messages
from django.db.models import Q

# Create your views here.
products = ProductTable.objects.filter(is_available =True)
def products(request):
    data = {}
    products = ProductTable.objects.filter(is_available =True)
    data['products'] = products
    return render(request,'products/products.html',context=data)


def add_to_cart(request,product_id):
    if request.user.is_authenticated:
        user = request.user
        product = ProductTable.objects.get(id=product_id)
        q1 = Q(user_id=user.id)
        q2 = Q(product_id=product_id)
        cart_value = Cart_Table.objects.filter(q1 & q2)
        if (cart_value.count()>0):
            messages.error(request,"Product is already in the cart ")
        else:
            cart = Cart_Table.objects.create(user_id=user,product_id=product,quantity=1)
            cart.save()
            messages.success(request,"Product is added to the cart ")
        return redirect('/')
    else:
        return redirect("/login") 