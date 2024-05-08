from django.shortcuts import render
from products.models import ProductTable

# Create your views here.
products = ProductTable.objects.filter(is_available =True)
def products(request):
    data = {}
    products = ProductTable.objects.filter(is_available =True)
    data['products'] = products
    return render(request,'products/products.html',context=data)