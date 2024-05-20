from django.urls import path
from . import views 

urlpatterns = [
    path('',views.products),
    path('addtocart/<product_id>',views.add_to_cart),
    path('category/<str>', views.filter_category),
]