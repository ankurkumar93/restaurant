from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('addrestaurant', RestaurantProfileView.as_view(), name='addrestaurant'),
    path('getrestaurant/', RestaurantProfileView.as_view(), name='getrestaurant'),
    path('login', LoginAPIView.as_view(), name='login'),

    path('app/customer', CustomerView.as_view(), name='addcustomer'),
    path('app/getcustomer/', CustomerView.as_view(), name='getcustomer'),



]