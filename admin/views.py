from django.shortcuts import render,redirect
from products.models import ProductTable
from appointments.models import User_App,AppointmentsSchedule
import datetime 
from datetime import timedelta

# Create your views here.
def admin(request):
    data = {}
    apps = User_App.objects.filter(Booked_date = datetime.date.today() )
    appointments = AppointmentsSchedule.objects.get(date = datetime.date.today()  )
    data['apps'] = apps
    data['appointment'] = appointments
    return render(request,"admin/home.html",context=data)



def add_product(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        quantity=request.POST.get('quantity')
        category=request.POST.get('category')
        image = request.FILES.get('image')
        is_available=(request.POST.get('is_available',False)) and ('is_available' in request.POST)
        
        product=ProductTable.objects.create(name=name,price=price,description=description,quantity=quantity,category=category,image=image,is_available=is_available)
        
        product.save()
        
        return redirect("/adminpannel/product/view/")
    return render(request,'admin/add_product.html')

def view_products(request):
    data={}
    products=ProductTable.objects.all()
    # print(products.count())
    data['products']=products
    return render(request,'admin/view_product.html',context=data)

def delete_product(request,productid):
    product=ProductTable.objects.get(id=productid)
    product.delete()
    return redirect("/adminpannel/product/view/")

def edit_product(request,int):
    data = {}
    product = ProductTable.objects.get(id=int)
    data['product'] = product
    if request.method=='POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description=request.POST.get('description')
        product.quantity=request.POST.get('quantity')
        product.category=request.POST.get('category')
        if 'image' in request.FILES:
            product.images = request.FILES['image']
        product.save()
        return redirect('/adminpannel/product/view')
    return render(request, 'admin/edit_product.html',context=data)