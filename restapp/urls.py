from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('addrestaurant', RestaurantProfileView.as_view(), name='addrestaurant'),
    path('getrestaurant/', RestaurantProfileView.as_view(), name='getrestaurant'),

    path('login', LoginAPIView.as_view(), name='login'),

]