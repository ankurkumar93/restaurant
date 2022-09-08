from rest_framework import serializers
from .models import *

class RestaurantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantProfile
        fields = '__all__'


