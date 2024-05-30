from django.urls import path
from . import views


urlpatterns = [
    path('admin/',views.admin),
    path('product/add/', views.add_product),
    path('product/view/', views.view_products),
    path('product/edit_product/<int>', views.edit_product,),
    path('product/delete/<productid>', views.delete_product),
]