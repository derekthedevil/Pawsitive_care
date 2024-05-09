from django.urls import path
from . import views


urlpatterns = [
    path("",views.appointments),
    path("next_week",views.next_week),
    path("last_week",views.last_week)
]