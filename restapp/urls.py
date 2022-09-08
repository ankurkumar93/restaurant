from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('addrestaurant', RestaurantProfileView.as_view(), name='addrestaurant'),
]