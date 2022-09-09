from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class RestaurantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantProfile
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RestaurantProfileSerializer, self).create(validated_data)


class LoginSerializer(serializers.Serializer):
    userid = serializers.CharField()
    password = serializers.CharField()



