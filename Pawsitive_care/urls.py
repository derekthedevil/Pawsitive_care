"""Pawsitive_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from products import product_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.user_login),
    path('register', views.user_register),
    path('logout/', views.user_logout),
    path('cart/', views.cart),
    path('products/', include('products.product_urls')),
    path('cart/delete/<cart_id>', views.delete),
    path('cart/update/<update>/<cart_id>', views.cart_update),
    path('appointments/', include('appointments.appointment_urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)