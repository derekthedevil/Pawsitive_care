from django.urls import path
from . import views 

urlpatterns = [
    path('',views.products),
    path('addtocart/<product_id>',views.add_to_cart),
    path('order/<payment_id>/<amount>',views.order),
    #  seacrh and sort functions 
    path('category/<category_value>', views.filter_by_category),
    path('sort/<sort_value>', views.sort_by_price),
    path('search/', views.search_by_price_range),
]