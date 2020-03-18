from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('clear_counter', views.clr_cntr)
]