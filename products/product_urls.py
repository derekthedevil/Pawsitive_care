from django.urls import path
from . import views 

urlpatterns = [
    path('',views.products),
    path('addtocart/<product_id>',views.add_to_cart),
    path('order/<payment_id>/<amount>',views.order),
    path('category/<str>', views.filter_category),
]